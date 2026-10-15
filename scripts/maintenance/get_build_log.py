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

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new_req = urllib.request.Request(newurl)
        return new_req

opener = urllib.request.build_opener(NoRedirect)
build_id = "116400964833"
log_url = f"https://api.github.com/repos/KazinMintori/StudyHub/actions/jobs/{build_id}/logs"

req = urllib.request.Request(log_url, headers={
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {token}"
})

try:
    with opener.open(req) as resp:
        content = resp.read().decode('utf-8', errors='replace')
        with open("build_failure.log", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote {len(content)} chars to build_failure.log")
except Exception as e:
    print(f"Error: {e}")
