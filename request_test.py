import requests
import re
from pathlib import Path
import json
path = Path('zhihu.txt')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile(r'"title":"(.*?)"', re.S)
titles = re.findall(pattern, r.text)
json_titles = json.dumps(titles,type='utf-8')
path.write_text(json_titles, 'utf-8')

#抓取图片资源
# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
    
#文件上传
# files = {'file': open('favicon.ico','rb')}
# r = requests.post('http://httpbin.org/post',files=files)
# print(r.text)

# cookie和session的区别
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

#ssl证书验证相关
# response = requests.get('https://www.12306.cn', verify=True)
# print(response.status_code)