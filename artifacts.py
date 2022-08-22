import re
import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]
ACTION_URL = os.environ["ACTION_URL"]
COMMENTID = os.environ["COMMENT_ID"]

BASE_API_URL = 'https://api.github.com'
owner = '1299172402'
repo = 'tongli-new'
comment_id = COMMENTID

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def main():
    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/comments/{comment_id}'
    res = requests.get(url, headers=headers).json()
    run_id = re.search(r'#.*#', res['body']) 
    run_id = run_id[1:-1]

    url = f'{BASE_API_URL}/repos/{owner}/{repo}/actions/runs/{run_id}'
    res = requests.get(url, headers=headers).json()
    print(res)



if __name__ == '__main__':
    main()