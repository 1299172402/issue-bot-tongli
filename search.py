import os
import json
import requests

GHP_TONGLI = os.environ["GHP_TONGLI"]
NUMBER = os.environ["NUMBER"]

BASE_API_URL = 'https://api.github.com'
owner = '1299172402'
repo = 'issue-bot-tongli'
issue_number = NUMBER

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GHP_TONGLI}"
}

def comment(message):
    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{str(issue_number)}/comments'
    data = {"body": f"{message}"}
    requests.post(url, headers=headers, data=json.dumps(data))
    print(f'[info] comment: {message}')

def func(BookGroupID, Title, CoverURL, Author, IsSerial):
    url = f'https://api.tongli.tw/Book/BookVol/{BookGroupID}?isSerial={IsSerial}'
    res = requests.get(url).json()
    BookID = res[-1]['BookID']

    url = f'https://api.tongli.tw/Book?bookID={BookID}'
    res = requests.get(url).json()
    Introduction = res['Introduction']
    OnShelfDate = res['OnShelfDate']
    RankStar = res['Rank']['RankStar']
    Vol = res['Vol']

    text = f'''

<img src="{CoverURL}" height="50%" width="50%" >

# [bot] {Title} © {Author} 著

## 评分： {''.join('⭐' for _ in range(RankStar))}

## 简介

　　{Introduction}

## 最新话：{Vol}

## 上架日期：{OnShelfDate}
    
## 其他信息

- BookGroupID {BookGroupID}
- BookID {BookID}
- IsSerial {IsSerial}

    '''
    comment(text)

def main():
    url = f'{BASE_API_URL}/repos/{owner}/{repo}/issues/{issue_number}'
    res = requests.get(url, headers=headers).json()
    SearchStr = res['body']

    url = 'https://api.tongli.tw/Search'
    data = {
        "SearchStr": SearchStr
    }
    res = requests.post(url, data).json()
    if res:
        for item in res:
            BookGroupID = item['BookGroupID']
            Title = item['Title']
            CoverURL = item['CoverURL']
            Author = item['Author']
            IsSerial = item['IsSerial']
            func(BookGroupID, Title, CoverURL, Author, IsSerial)
    else:
        comment("无任何搜索结果")

if __name__ == '__main__':
    main()