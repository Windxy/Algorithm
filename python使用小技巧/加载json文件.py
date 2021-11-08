'''参考 https://blog.csdn.net/whjkm/article/details/81159888'''
import json

dict = '{"name": "Tom", "age": 23}'   # 将字符串还原为dict
data1 = json.loads(dict)
print(data1, type(data1))

with open("xxx.json", "r", encoding='utf-8') as f:
    data2 = json.loads(f.read())    # load的传入参数为字符串类型
    print(data2, type(data2))
    f.seek(0)                       # 将文件游标移动到文件开头位置
    data3 = json.load(f)
    print(data3, type(data3))