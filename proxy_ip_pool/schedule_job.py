TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
import time
from multiprocessing import Process
from avaliable_ip import app
from getter_ip import Getter
from update_ip_status import Tester
from settings import APP_PROD_METHOD_GEVENT, APP_PROD_METHOD_MEINHELD, APP_PROD_METHOD_TORNADO, CYCLE_GETTER, CYCLE_TESTER, API_HOST, \
    API_THREADED, API_PORT, ENABLE_SERVER, IS_PROD, APP_PROD_METHOD, \
    ENABLE_GETTER, ENABLE_TESTER, IS_WINDOWS
class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """定时测试代理"""
        tester = Tester()
        while True:
            print(' 测试器开始运行 ')
            tester.run()
            time.sleep(cycle)
    
    def schedule_getter(self, cycle=GETTER_CYCLE):
        """定时获取代理"""
        getter = Getter()
        while True:
            print(' 开始抓取代理 ')
            getter.run()
            time.sleep(cycle)
    
    def schedule_api(self):
        """开启 API"""
        app.run(API_HOST, API_PORT)
    
    def run(self):
        print(' 代理池开始运行 ')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()