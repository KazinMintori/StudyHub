import urllib.request
import json
import sys

run_id = '38728742875'
url = f'https://api.github.com/repos/KazinMintori/StudyHub/actions/runs/{run_id}/jobs'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    for j in data.get('jobs', []):
        print(f"Job: {j.get('name')}, Status: {j.get('status')}, Conclusion: {j.get('conclusion')}")
        for s in j.get('steps', []):
            print(f"  Step {s.get('number')}: {s.get('name')} -> {s.get('conclusion')} ({s.get('status')})")
except Exception as e:
    print('Error:', e)
