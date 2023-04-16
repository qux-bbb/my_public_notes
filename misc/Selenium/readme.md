# Selenium

官网: https://www.selenium.dev/  

Selenium 主要用于Web应用程序的自动化测试，用来写爬虫也很方便。  
Selenium IDE 是一个浏览器插件，可以记录对浏览器的操作，生成测试脚本，在这个脚本的基础上修改逻辑比较方便。  

这里记一下python版本的安装和简单用法。  


## 安装
1. 安装python包: `pip install selenium`  
2. 提前安装浏览器，然后安装相应浏览器driver程序，需要将driver程序文件夹路径添加到PATH，现阶段这样装driver是最简单的
   ```r
   Chromium/Chrome https://chromedriver.chromium.org/downloads
   Firefox https://github.com/mozilla/geckodriver/releases
   Edge https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   Internet Explorer https://www.selenium.dev/downloads
   ```


## 脚本简单示例
```python
# coding:utf-8
# 2018/10/6

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {
    "User-Agent": "Baiduspider+(+http://www.baidu.com/search/spider.htm)",
    "Referer": "http://www.baidu.com",
}

option = webdriver.FirefoxOptions()
option.add_argument("-headless")
browser = webdriver.Firefox(firefox_options=option)

browser.get("http://www.helloworld.com/")
child = browser.find_element_by_class_name("thumbnail")
child_url = child.get_attribute("href")
mp4_name = child_url.split("/")[-2]

browser.get(child_url)
mp4_url = browser.find_element_by_id("player_html5_api").get_attribute("src")

res = requests.get(mp4_url, headers=headers)
open(mp4_name, "wb").write(res.content)
print("Got it")
```

示例2：  
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```


## 参考链接
1. https://www.selenium.dev/documentation/webdriver/getting_started/
2. https://selenium-python.readthedocs.io/


---
2023/4/16  
