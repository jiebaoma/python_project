from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#将BAIDUID,BDUSS写入到cookie中
driver.add_cookie({"name":"BAIDUID","value":"E08FB862FC7776BBD38B9C4F9366F668:FG=1"})
driver.add_cookie({"name":"BDUSS","value":"G5maXE5ZTJ1VH53MUVnTTEwdUlWfnR1SVd6WHg5U2dWZDRuOUZUa2RjdTAxZ2RjQVFBQUFBJCQAAAAAAAAAAAEAAADdmtIpvd2xqsLtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALRJ4Fu0SeBbZ"})
#刷新界面
driver.refresh()
sleep(2)
