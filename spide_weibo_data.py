from pyquery import PyQuery as pq
import json
from urllib.parse import urlencode  
from pathlib import Path
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
        'Host': 'm.weibo.cn',  
    'Referer': 'https://m.weibo.cn/u/2830678474',  
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/58.0.3029.110 Safari/537.36',  
    'X-Requested-With': 'XMLHttpRequest',  
}
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        reponse = requests.get(url, headers)
        if reponse.status_code == 200:
            return reponse.json()
    except requests.ConnectionError as error:
        print('Error', error.args)
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo
if __name__ == '__main__':
    path = Path('spide_weibo_data.txt')
    for page in range(1,11):
        json1 = get_page(page)
        results = parse_page(json1)
        for result in results:
            with path.open(mode='a',encoding='utf-8') as f:
                f.write(json.dumps(result,ensure_ascii=False,indent=2))