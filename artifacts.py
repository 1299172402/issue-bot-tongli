import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
WORKFLOW_URL = os.environ["WORKFLOW_URL"]
ACTION_URL = os.environ["ACTION_URL"]
COMMENT = os.environ["COMMENT"]

BASE_API_URL = 'https://api.github.com'
owner = '1299172402'
repo = 'tongli-new'
issue_number = NUMBER

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def main():
    print(type(COMMENT))
    comments = json.loads(COMMENT)
    print(COMMENT)
    print(COMMENT['id'])
    print(COMMENT['body'])
    

if __name__ == '__main__':
    main()