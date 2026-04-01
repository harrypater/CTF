import requests
import base64
session = requests.Session() 

url="http://171.80.2.169:15492/"
response = session.get(url)                  # 发起一次 get 请求，获取首页内容
headers = response.headers                   # 获取响应标头
flagBase64Str = headers["flag"]              # 获取响应标头里的flag参数
flagStr = base64.b64decode(flagBase64Str)    # base64解码
print(flagStr) #   b'\xe8\xb7\x91\xe7\x9a\x84\xe8\xbf\x98\xe4\xb8\x8d\xe9\x94\x99\xef\xbc\x8c\xe7\xbb\x99\xe4\xbd\xa0flag\xe5\x90\xa7: ODQzNzEx' (设置下 utf-8 格式吧)
flagStr = flagStr.decode("utf-8")
print(flagStr)                        # 跑的还不错，给你flag吧: MTY5NTM0 （好啦，拿到了，但是要把字符截取出来）

flagStr = flagStr.split(": ")[1]      # 以: 为分隔符，把字符串分成两部分（拿到下标为 1 的值）
flagStr = base64.b64decode(flagStr)
flagStr = flagStr.decode("utf-8")
print("gargin:  "+flagStr) # 
# 发起 post 请求

res = session.post(url, data={"margin": flagStr})
print(res.text)
