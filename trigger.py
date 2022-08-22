import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]

def main():
    url = 'https://api.github.com/repos/1299172402/tongli-new/issues'
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {GHP_TONGLI}"
    }
    res = requests.get(url, headers=headers).json()
    if res[0]['labels'][0]['name'] == 'Runner':
        params = res[0]['body']
        number = res[0]['number']

    params = json.loads(params)

    url = WORKFLOW_URL
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {GHP_TONGLI}"
    }
    data = {
        "ref":"main",
        "inputs": {
            "type": params['type'],
            "bookid": params['bookid'],
            "isSerial": params['isSerial'],
            "RefreshToken": params['RefreshToken'],
            "issue_number": number,
        }
    }
    requests.post(url, headers=headers, data=data)

if __name__ == '__main__':
    main()