# coding=utf-8
import jsonlines
import json

#jsonlines 转换成json
with jsonlines.open("yao20210928.jsonlines", "r") as rfd:
    with open("report.json", "w", encoding='utf-8') as wfd:
        for data in rfd:
            json.dump(data, wfd, indent=4, ensure_ascii=False)


