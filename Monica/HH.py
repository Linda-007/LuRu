# coding=utf-8
import json
import time
import requests

# url = "http://123.60.74.77:8080/demo/api/common-activiti/work/time/config"  #电子票算法停留时间和工作时间段配置
url = "http://123.60.74.77:8080/demo/api/common-activiti/work/time/config/query"   # 电子票算法停留时间和工作时间段配置查询


header = {"Content-Type": "application/json",}


data = { "eTicketAlgorithmStayTm": "10",
  "workStartTm": "10:30",
  "workEndTm": "22:00"
         }

# re = requests.post(url=url, data=json.dumps(data), headers=header)  ##电子票算法停留时间和工作时间段配置
re = requests.get(url=url, data=json.dumps(data), headers=header)   #电子票算法停留时间和工作时间段配置查询
print(re.json())
print(data)
