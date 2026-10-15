import urllib.request
import json
import subprocess
import sys

def get_git_token():
    p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, _ = p.communicate(input='protocol=https\nhost=github.com\n\n')
    creds = {}
    for line in out.splitlines():
        if '=' in line:
            k, v = line.split('=', 1)
            creds[k] = v
    return creds.get('password')

token = get_git_token()

class DropAuthOnRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # S3 pre-signed URL will fail if Authorization header is sent
        new_headers = {k: v for k, v in req.headers.items() if k.lower() != 'authorization'}
        return urllib.request.Request(newurl, headers=new_headers)

opener = urllib.request.build_opener(DropAuthOnRedirect)

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/vnd.github.v3+json",
}
if token:
    headers["Authorization"] = f"Bearer {token}"

runs_url = "https://api.github.com/repos/KazinMintori/StudyHub/actions/runs?per_page=1"
req = urllib.request.Request(runs_url, headers=headers)
with opener.open(req) as resp:
    run_data = json.loads(resp.read().decode('utf-8'))
latest_run = run_data['workflow_runs'][0]
run_id = latest_run['id']
print(f"Latest run: {run_id} ({latest_run['head_sha'][:7]}) -> {latest_run['conclusion']}")

jobs_url = f"https://api.github.com/repos/KazinMintori/StudyHub/actions/runs/{run_id}/jobs"
req = urllib.request.Request(jobs_url, headers=headers)
with opener.open(req) as resp:
    jobs_data = json.loads(resp.read().decode('utf-8'))

for job in jobs_data['jobs']:
    job_id = job['id']
    job_name = job['name']
    job_conclusion = job['conclusion']
    print(f"Job {job_id} ({job_name}): {job_conclusion}")
    if job_conclusion == 'failure':
        log_url = f"https://api.github.com/repos/KazinMintori/StudyHub/actions/jobs/{job_id}/logs"
        req = urllib.request.Request(log_url, headers=headers)
        try:
            with opener.open(req) as lresp:
                log_content = lresp.read().decode('utf-8', errors='replace')
                with open('build_failure.log', 'w', encoding='utf-8') as f:
                    f.write(log_content)
                lines = log_content.splitlines()
                # Find lines around error
                fail_indices = [i for i, l in enumerate(lines) if '##[error]' in l or 'error' in l.lower() or 'failed' in l.lower()]
                for i in fail_indices[:5]:
                    start = max(0, i - 5)
                    end = min(len(lines), i + 10)
                    print(f"\n--- FAILURE CONTEXT (line {i}) ---")
                    for idx in range(start, end):
                        print(lines[idx])
        except Exception as e:
            print("Error getting log:", e)
