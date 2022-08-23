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
    else:
        print('[error] `Runner` not in labels')
        return 0

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
    if res.status_code == 204:
        print(f'[info] workflow: {res}')
    else:
        url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{str(issue_number)}/comments'
        data = {"body": f"[bot] 你输入的参数有误，请重新发起 issue"}
        requests.post(url, headers=headers, data=json.dumps(data))
        print(f'[error] start workflow failed.')
        return 0

    url = f'{ACTION_URL}/runs'
    res = requests.get(url, headers=headers).json()
    run_id = res['workflow_runs'][0]['id']
    print(f'[info] run_id: {run_id}')

    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{str(issue_number)}/comments'
    data = {"body": f"[bot] 你的 run_id 是 {run_id}。 当工作流完成时会通知你。"}
    requests.post(url, headers=headers, data=json.dumps(data))
    print(f'[info] comment: start download')

if __name__ == '__main__':
    main()
