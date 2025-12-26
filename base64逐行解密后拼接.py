import base64
import re

# -------------------------- 核心配置 --------------------------
INPUT_FILE = "passwd.txt"   # 你的输入TXT文件路径（每行是独立Base64编码）
OUTPUT_FILE = "decoded.txt"  # 最终拼接结果的保存路径
# -------------------------------------------------------------

def fix_base64(s):
    """修复单行Base64字符串：过滤非法字符 + 补全填充符"""
    # 1. 去除行首尾空格/换行，过滤非Base64合法字符（A-Za-z0-9+/=）
    s = re.sub(r"[^A-Za-z0-9+/=]", "", s.strip())
    # 2. 补全缺失的填充符（Base64长度需为4的倍数）
    missing_padding = len(s) % 4
    if missing_padding != 0 and len(s) > 0:
        s += "=" * (4 - missing_padding)
    return s

def decode_single_line(line_str, line_num):
    """解码单行Base64字符串，返回解码后的字符串（失败则返回错误提示）"""
    if not line_str:  # 空行直接返回空
        return ""
    
    # 预处理Base64字符串
    fixed_str = fix_base64(line_str)
    if not fixed_str:
        return f"【第{line_num}行】空内容，跳过解码"
    
    try:
        # Base64解码为字节
        decoded_bytes = base64.b64decode(fixed_str)
        # 兼容中文编码（优先utf-8，失败则用gbk）
        try:
            decoded_str = decoded_bytes.decode("utf-8")
        except UnicodeDecodeError:
            decoded_str = decoded_bytes.decode("gbk")
        return decoded_str
    except base64.binascii.Error as e:
        return f"【第{line_num}行】解码失败：{str(e)}"
    except Exception as e:
        return f"【第{line_num}行】未知错误：{str(e)}"

def main():
    # 存储每行解码后的结果
    line_results = []
    # 存储最终拼接的有效内容（过滤错误提示和空行）
    final_combined = ""

    try:
        # 1. 逐行读取并解码
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print("开始逐行解码...\n")
            for idx, line in enumerate(lines, 1):
                decoded_line = decode_single_line(line, idx)
                line_results.append(decoded_line)
                # 打印单行解码结果（便于调试）
                print(f"第{idx}行解码结果：{decoded_line}")
                
                # 收集有效解码内容（跳过错误提示和空行）
                if not decoded_line.startswith("【") and decoded_line != "":
                    final_combined += decoded_line

        # 2. 输出最终拼接结果
        print("\n" + "-"*50)
        print("✅ 所有行解码后拼接的最终结果：")
        print(final_combined)

        # 3. 保存拼接结果到文件
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(final_combined)
        print(f"\n拼接结果已保存到：{OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"错误：未找到文件 {INPUT_FILE}，请检查路径是否正确")
    except Exception as e:
        print(f"程序异常：{str(e)}")

if __name__ == "__main__":
    main()
