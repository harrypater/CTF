import base64

# 待解码的 Base64 字符串
encoded_str = 'UEsDBBQAAAAIAOJRT1tclFOiJQAAADAAAAAIAAAAZmxhZy50eHR7snfBi+VNT9fPf7Kr7XnP6vd7eoDks20dT5dsBIq83zMfDQEAUEsBAhQAFAAAAAgA4lFPW1yUU6IlAAAAMAAAAAgAAAAAAAAAAAAAALaBAAAAAGZsYWcudHh0UEsFBgAAAAABAAEANgAAAEsAAAAAAA=='

# Base64 解码
decoded_data = base64.b64decode(encoded_str)

# 打印解码后的数据（二进制）+ 保存为文件
print("解码后二进制数据（前100字节）：")
print(decoded_data[:100])

# 将解码后的数据保存为文件（关键！因为是 ZIP 包）
with open('flag.zip', 'wb') as f:
    f.write(decoded_data)
print("\n已将解码后的数据保存为 flag.zip")
