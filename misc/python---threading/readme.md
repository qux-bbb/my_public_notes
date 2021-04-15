# python---threading
python 多线程 threading模块简单使用  

如果有冲突就加锁，如果没有就不需要加锁  

由于python全局锁的存在，一般的多线程并没有什么用处  

```python
# coding:utf8
# python3

from time import sleep
from threading import Thread, Lock


class Test:

    def __init__(self):
        self.lock = Lock()

    def submit(self, file_path):
        self.lock.acquire()
        print('submit start')
        sleep(2)
        print('{} submitted'.format(file_path))
        print('submit end')
        self.lock.release()

    def get_report(self, md5_value):
        self.lock.acquire()
        print('get_report start')
        sleep(2)
        print('{}\' report saved'.format(md5_value))
        print('get_report end')
        self.lock.release()

    def submit_get(self):
        submit_thread = Thread(target=self.submit('/tmp/hello.exe'))
        get_report_thread = Thread(target=self.get_report(
            '0123456789abcdeffedcba9876543210'))

        submit_thread.start()
        get_report_thread.start()

        submit_thread.join()
        get_report_thread.join()


test = Test()
test.submit_get()
print('end')
```
