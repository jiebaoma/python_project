#!/usr/bin/env python
#__*__ coding:utf-8 __*__
import paramiko
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from paramiko import Transport

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//input[@name='wd']").send_keys("python")
driver.implicitly_wait(100)
# sleep(5)
driver.find_element_by_xpath("//input[@name='wd']").send_keys(Keys.CONTROL,'a')


def ssh_edit_file(adress, user, passw, remotefile, regex, replace):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    trans = paramiko.Transport((adress, 22))
    trans.connect(username=user, password=passw)
    sftp = paramiko.SFTPClient.from_transport(trans)
    # f_in = sftp.file(remotefile, "r")
    # c_in = f_in.read()
    # pattern = re.compile(regex, re.MULTILINE | re.DOTALL)
    # c_out = pattern.sub(replace, c_in)
    # f_out = sftp.file(remotefile, "w")
    # f_out.write(c_out)
    # f_in.close()
    # f_out.close()
    # sftp.close()
    # trans.close()