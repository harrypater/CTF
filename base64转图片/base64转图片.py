import base64
import os


def read_base64_from_file(file_path):
    """
    从文件读取 Base64 字符串（处理多行/单行、空白字符）

    参数：
        file_path (str): 存储 Base64 字符串的文件路径（如 base64_data.txt）
    返回：
        str: 清理后的纯 Base64 字符串
    """
    try:
        # 读取文件并清理空白字符（换行、空格、制表符）
        with open(file_path, "r", encoding="utf-8") as f:
            base64_str = f.read().strip()  # 移除首尾空白
            base64_str = "".join(base64_str.split())  # 移除所有中间空白（换行/空格）
        return base64_str
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}")
        return None
    except Exception as e:
        print(f"读取文件失败：{e}")
        return None


def base64_file_to_image(base64_file_path, output_image_path):
    """
    从存储 Base64 字符串的文件中读取数据，转换为图片文件

    参数：
        base64_file_path (str): 存储 Base64 字符串的文件路径
        output_image_path (str): 输出图片的路径（如 output.jpg、result.png）
    返回：
        bool: 转换成功返回 True，失败返回 False
    """
    # 1. 读取并清理 Base64 字符串
    base64_str = read_base64_from_file(base64_file_path)
    if not base64_str:
        return False

    try:
        # 2. 移除 Base64 前缀（如 data:image/png;base64,）
        if "," in base64_str:
            base64_str = base64_str.split(",")[1]

        # 3. 补全 Base64 填充符（确保长度是 4 的倍数）
        missing_padding = len(base64_str) % 4
        if missing_padding != 0:
            base64_str += "=" * (4 - missing_padding)

        # 4. 解码 Base64 为二进制字节流
        image_bytes = base64.b64decode(base64_str)

        # 5. 确保输出目录存在
        output_dir = os.path.dirname(output_image_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 6. 将二进制流写入图片文件
        with open(output_image_path, "wb") as f:
            f.write(image_bytes)

        print(f"✅ 图片已成功生成：{output_image_path}")
        print(f"📄 图片文件大小：{os.path.getsize(output_image_path)} 字节")
        return True

    except base64.binascii.Error as e:
        print(f"❌ Base64 解码失败：{e}（请检查 Base64 字符串是否完整/有效）")
        return False
    except Exception as e:
        print(f"❌ 生成图片失败：{e}")
        return False


# ------------------- 示例使用 -------------------
if __name__ == "__main__":
    # 配置文件路径（替换为你的实际路径）
     BASE64_FILE = "base64_data.txt"  # 存储 Base64 字符串的文件
     OUTPUT_IMAGE = "output_image.png"  # 输出图片路径（后缀要和图片格式匹配）

     # 执行转换
     success = base64_file_to_image(BASE64_FILE, OUTPUT_IMAGE)

