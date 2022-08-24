import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]
ACTION_URL = os.environ["ACTION_URL"]
NUMBER = os.environ["NUMBER"]
USER = os.environ["USER"]

BASE_API_URL = 'https://api.github.com'
owner = '1299172402'
repo = 'issue-bot-tongli'
issue_number = NUMBER
username = USER

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def main():
    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{issue_number}'
    res = requests.get(url, headers=headers).json()
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
            "username": username,
            "issue_number": str(issue_number)
        }
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    if res.status_code == 204:
        print(f'[info] workflow: {res}')
    else:
        url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{str(issue_number)}/comments'
        data = {"body": f"[bot] 你输入的参数有误，请重新发起 issue"}
        requests.post(url, headers=headers, data=json.dumps(data))
        print(f'[error] start workflow failed.')
        return 0

if __name__ == '__main__':
    main()
