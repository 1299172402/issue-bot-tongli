import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]
ACTION_URL = os.environ["ACTION_URL"]
NUMBER = os.environ["NUMBER"]

BASE_API_URL = 'https://api.github.com'
owner = '1299172402'
repo = 'tongli-new'
issue_number = NUMBER

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def main():
    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{issue_number}'
    res = requests.get(url, headers=headers).json()
    if res['labels'][0]['name'] == 'Runner':
        params = res['body']

    params = json.loads(params)
    print(f'[info] params: {params}')

    url = WORKFLOW_URL
    data = {
        "ref": "main",
        "inputs": {
            "type": params['type'],
            "bookid": params['bookid'],
            "isSerial": params['isSerial'],
            "RefreshToken": params['RefreshToken'],
            "issue_number": str(issue_number)
        }
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    print(f'[info] workflow: {res}')

    url = ACTION_URL
    res = requests.get(url, headers=headers).json()
    run_id = res['workflow_runs'][0]['id']
    print(f'[info] run_id: {run_id}')

    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{str(issue_number)}/comments'
    data = {"body": f"Your run id is #{run_id}#. We'll let you know when it's done."}
    requests.post(url, headers=headers, data=json.dumps(data))
    print(f'[info] comment: start download')

if __name__ == '__main__':
    main()
