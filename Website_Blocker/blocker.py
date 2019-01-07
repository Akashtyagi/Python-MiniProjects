# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 00:09:39 2018

@author: Akash
"""

import time
from datetime import datetime as dt

Host_file_path ="C:\Windows\System32\drivers\etc\hosts"
website_list = ["www.facebook.com","www.instagram.com"]
redirect = "127:0:0:1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,20) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23,59):
        print("Working Hours...")
        with open(Host_file_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"\t"+website+"\n")
    else:
        with open(Host_file_path,'r+') as file:
            content = file.readlines()
            print("Fun hours")
            file.seek(0)
            for line in content:
                if not any(website in content for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(10)
