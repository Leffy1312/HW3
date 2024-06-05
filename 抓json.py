# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:54:27 2024

@author: KIDO
"""

import requests
import json
url ="https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=100"

data = requests.get(url).text
#print(data)
bike = json.loads(data)

while True:
    area = input("請輸入區域,q退出:")
    
    if area.lower() =='q':
        break
    found_area = False
    for item in bike:
        if area == item['sarea']:
            found_area = True
            print('地區',item['sarea'])
            print('站名:',item['sna'])
            print('可借:',item['sbi'])
            print('可停:',item['bemp'])
            print()
            continue

    if not found_area:
        print("沒找到,請再查詢一次")
