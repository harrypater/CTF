# 从C代码中提取的64位整数（小端序）
v6 = 2536141372637721907
v7 = 3042234510439362354
v8 = 2750641857828633918
v8_fix = -2710481527095417300


# 将64位整数转换为字节序列（小端序）
def int_to_bytes(n, length=8):
    return n.to_bytes(length, byteorder='little', signed=True)


# 提取完整的目标字节序列
target_bytes = []
# v6 (8字节)
target_bytes.extend(int_to_bytes(v6))
print(int_to_bytes(v6))
# v7 (8字节)
target_bytes.extend(int_to_bytes(v7))
# v8 前6字节 + 修正后的字节（覆盖）
v8_bytes = int_to_bytes(v8)
v8_fix_bytes = int_to_bytes(v8_fix)
# 前6字节保留，后8字节用修正值（注意：小端序）
target_bytes.extend(v8_bytes[:6])
target_bytes.extend(v8_fix_bytes)

# 正确的逆向计算：(字节值 ^ 0x5A) - 3
flag = []
for b in target_bytes:
    # 逆向运算：先异或0x5A，再减3
    char_code = (b ^ 0x5A) - 3
    char = chr(char_code)
    flag.append(char)

# 输出正确的flag
flag_str = ''.join(flag)
print("Correct Flag:", flag_str)
print("Flag Length:", len(flag_str))
