import urllib.request
import json
import sys

# Get workflow runs
runs_url = 'https://api.github.com/repos/KazinMintori/StudyHub/actions/runs?per_page=10'
req_runs = urllib.request.Request(runs_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req_runs) as resp:
        runs_data = json.loads(resp.read().decode('utf-8'))
    runs = runs_data.get('workflow_runs', [])
    for idx, r in enumerate(runs):
        run_id = r['id']
        commit_sha = r['head_sha'][:7]
        commit_msg = r.get('display_title', '')[:60]
        status = r.get('status')
        conclusion = r.get('conclusion')
        print(f"[{idx}] Run {run_id} ({commit_sha}: {commit_msg}) -> {status}/{conclusion}")
        if idx == 0 or conclusion == 'failure':
            url = f'https://api.github.com/repos/KazinMintori/StudyHub/actions/runs/{run_id}/jobs'
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as jresp:
                jdata = json.loads(jresp.read().decode('utf-8'))
            for j in jdata.get('jobs', []):
                print(f"    Job: {j.get('name')} -> {j.get('status')} / {j.get('conclusion')}")
                for s in j.get('steps', []):
                    print(f"      Step {s.get('number')}: {s.get('name')} -> {s.get('conclusion')}")
except Exception as e:
    print('Error:', e)
