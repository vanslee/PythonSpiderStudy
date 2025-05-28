import urllib.error
import socket
import urllib.request
import urllib.parse  
from pathlib import Path
# response = urllib.request.urlopen('https://www.python.org')  
# path = Path("result.txt")
# path.write_text(response.read().decode('utf-8'),'utf-8')
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf-8')
try:
    response = urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT!')
print(response.read())