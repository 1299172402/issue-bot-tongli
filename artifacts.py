import re
import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]
ACTION_URL = os.environ["ACTION_URL"]
COMMENTID = os.environ["COMMENT_ID"]
NUMBER = os.environ["NUMBER"]

BASE_API_URL = 'https://api.github.com'
owner = '1299172402'
repo = 'tongli-new'
comment_id = COMMENTID
issue_number = NUMBER

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def main():
    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/comments/{comment_id}'
    res = requests.get(url, headers=headers).json()
    run_id = re.search(r'#\d+#', res['body'])
    if run_id:
        run_id = run_id.group()
        run_id = run_id[1:-1]
        print(f'[info] run_id: {run_id}')
    else:
        print('[error] not found run_id')
        return 0

    url = f'{ACTION_URL}/runs/{run_id}'
    res = requests.get(url, headers=headers).json()
    artifacts_url = res['artifacts_url']
    # print(f'[info] artifacts_url: {artifacts_url}')

    url = artifacts_url
    res = requests.get(url, headers=headers).json()
    artifact_id = res['artifacts'][0]['id']
    print(f'[info] artifact_id: {artifact_id}')

    archive_format = 'zip'
    url = f'{ACTION_URL}/artifacts/{artifact_id}/{archive_format}'
    res = requests.get(url, headers=headers, allow_redirects=False)
    print(f'[info] result: {res}')
    if res.status_code == 302:
        direct_url = res.headers['Location']
        data = {"body": f"[Bot] URL: {direct_url} "}
        print(f'[info] url: {direct_url}')
    else:
        data = {"body": f"[Bot] artifacts 已过期。请重新发起 issue "}
        print(f'[error] The artifacts url already gone.')

    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{str(issue_number)}/comments'
    requests.post(url, headers=headers, data=json.dumps(data))
    print(f'[info] comment: display direct_url')


if __name__ == '__main__':
    main()