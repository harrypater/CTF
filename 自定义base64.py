def custom_base64_decode(cipher_str, custom_charset):
    """
    自定义Base64解码函数
    :param cipher_str: 待解码的base64密文字符串
    :param custom_charset: 自定义的base64映射字符表（长度必须64）
    :return: 解码后的原始bytes数据
    """
    # 1. 校验字符表合法性（必须64个字符）
    if len(custom_charset) != 64:
        raise ValueError("自定义Base64字符表必须是64个字符！")
    
    # 2. 构建「字符→6位数值」的映射字典（核心）
    char2num = {char: idx for idx, char in enumerate(custom_charset)}
    
    # 3. 预处理密文：剔除填充符=、统一过滤非字符表内的无效字符
    cipher_str = cipher_str.replace('=', '')
    # 校验密文字符是否都在自定义表中
    for c in cipher_str:
        if c not in char2num:
            raise ValueError(f"密文包含非法字符：{c}，不在自定义字符表中")
    
    # 4. 核心解码：字符→6位数值→拼接二进制字符串
    bin_str = ''
    for c in cipher_str:
        # 字符转6位数值，再补零转6位二进制字符串（关键：保证固定6位）
        bin_str += bin(char2num[c])[2:].zfill(6)
    
    # 5. 二进制字符串→bytes字节数据（按8位分割）
    raw_bytes = b''
    for i in range(0, len(bin_str), 8):
        # 截取8位二进制，不足8位则丢弃（Base64填充规则）
        eight_bit = bin_str[i:i+8]
        if len(eight_bit) == 8:
            raw_bytes += int(eight_bit, 2).to_bytes(1, byteorder='big')
    
    return raw_bytes

# ==================== 你的需求专属配置 & 解码执行 ====================
if __name__ == "__main__":
    # ✅ 1. 你的自定义Base64映射字符表（严格按你指定）
    CUSTOM_BASE64_TABLE = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0987654321/+"
    # ✅ 2. 待解码的密文
    CIPHER_TEXT = "mTyqm7wjODkrNLcWl0eqO8K8gc1BPk1GNLgUpI=="
    
    # 执行解码
    result = custom_base64_decode(CIPHER_TEXT, CUSTOM_BASE64_TABLE)
    # 输出结果（bytes原生格式 + 字符串格式，按需选择）
    print("✅ 自定义Base64解码后的bytes结果：")
    print(result)
    print("\n✅ 解码后的字符串结果（UTF-8）：")
    print(result.decode('utf-8'))
