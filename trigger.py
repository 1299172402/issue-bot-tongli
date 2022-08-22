import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]
ACTION_URL = os.environ["ACTION_URL"]

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def main():
    url = 'https://api.github.com/repos/1299172402/tongli-new/issues'
    res = requests.get(url, headers=headers).json()
    if res[0]['labels'][0]['name'] == 'Runner':
        params = res[0]['body']
        number = res[0]['number']

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
            "issue_number": str(number)
        }
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    print(f'[info] workflow: {res}')

    url = ACTION_URL
    res = requests.get(url, headers=headers).json()
    run_id = res['workflow_runs'][0]['id']
    print(f'[info] run_id: {run_id}')

    url = f'https://api.github.com/repos/1299172402/tongli-new/issues/{str(number)}/comments'
    data = {"body": f"Your run id is ${run_id}$. We'll let you know when it's done."}
    requests.post(url, data=json.dumps(data))
    print(f'[info] comment: start download')

if __name__ == '__main__':
    main()