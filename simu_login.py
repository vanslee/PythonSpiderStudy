from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener  
from urllib.error import URLError  
from pathlib import Path
username = 'admin'  
password = '123456'  
url = 'http://127.0.0.1:5500/login_page.html'  
path = Path('result.html')
p = HTTPPasswordMgrWithDefaultRealm()  
p.add_password(None, url, username, password)  
auth_handler = HTTPBasicAuthHandler(p)  
opener = build_opener(auth_handler)  

try:  
    result = opener.open(url)  
    html = result.read().decode('utf-8')  
    path.write_text(html,'utf-8')
except URLError as e:  
    print(e.reason)