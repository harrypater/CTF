import base64



temp="""XQNGuAc9DEoRTAEFAygFDA6BDwz/DJSYbjpeOBBZCbg37dmLNYgNBA0JDAk/iQgC
AwEGBwaNDAoOAgQKbGJty24RbH8l73NOfIF/Q0y+wr9EkUHKq/oL4smYRouL38/0
w6Yv+yjdx6ZMuqfciszC/kD6jb3A/MCeyv3O887uychMv439SvPNvyn8hKov9Q0f
R62rUQEa0FHDT2hxHmXOdhR+q1oibuRm6khVT81ir3KUWuxgKp3fYggtCAhSBUm5
BxcOJBpHCQQcTQ4NCSMDDgqEBgbwBpCeZThQPh5YDLUz69yKM4AADQMEDg0+gAEL
AwEICwuGDQIjSAoMAg4HAAADDQwADQQLLgYNDg0JAwAODAQFAwoICm5ibsJrFmlw
KOx/TnmOckgLqQkMIQgDCAoIDQILBAMKCh4ODxuFDwc+K252vu4fwapI1wDXcgwf
px1pUVoBGtmvTN0M234FERj21DB42WyFrTjYCdB+BxpcCUeyAlIEbgQOBwkLAAsN
BxENAQMeDAZZqQoNDAAMDVzsCQsEBAcKAwMPDg=="""


temp2=base64.b64decode(temp)
hex_str = temp2.hex()
data=hex_str[::2]

print(data)



def hex_to_zip(hex_str, output_zip_path):
    """
    将十六进制字符串转换为ZIP文件
    :param hex_str: 完整的十六进制字符串（无空格、无0x前缀）
    :param output_zip_path: 输出的ZIP文件路径（如 "output.zip"）
    """
    try:
        # 1. 十六进制字符串转二进制数据
        binary_data = bytes.fromhex(hex_str)
        
        # 2. 将二进制数据写入ZIP文件
        with open(output_zip_path, 'wb') as f:
            f.write(binary_data)
        
        print(f"成功转换！ZIP文件已保存至: {output_zip_path}")
    except ValueError as e:
        print(f"转换失败：十六进制字符串格式错误 → {e}")
    except Exception as e:
        print(f"其他错误 → {e}")

# 示例使用（替换为你的十六进制字符串）

hex_to_zip(data, "out.zip")

        
        
