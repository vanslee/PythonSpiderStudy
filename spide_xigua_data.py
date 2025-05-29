import requests  
from urllib.parse import urlencode  

def get_page(offset):  
    params = {  
        'offset': offset,  
        'format': 'json',  
        'keyword': ' 街拍 ',  
        'autoload': 'true',  
        'count': '20',  
        'cur_tab': '3',  
    }  
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params) 
    print(url)
    try:  
        response = requests.get(url)  
        if response.status_code == 200:
            print(response.json())
            return response.json()  
    except requests.ConnectionError:  
        return None
if __name__ == '__main__':
    get_page(1)