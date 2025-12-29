import hashlib


def crack_md5(md5_file_path, rainbow_table_content):
    # 构建彩虹表映射（MD5值 -> 明文）
    rainbow_map = {}
    for line in rainbow_table_content.strip().split('\n'):
        if line:  # 跳过空行
            md5_val, plaintext = line.split(' ', 1)  # 分割MD5和明文
            rainbow_map[md5_val.lower()] = plaintext  # 统一转为小写匹配

    # 读取MD5文件并破解，收集明文结果
    plaintext_list = []
    print("开始破解MD5，结果如下：")
    print("-" * 50)
    with open(md5_file_path, 'r', encoding='utf-8') as f:
        for idx, md5_line in enumerate(f, 1):
            md5 = md5_line.strip().lower()
            if not md5:
                continue
            # 查找明文
            plain = rainbow_map.get(md5, "未找到匹配明文")
            plaintext_list.append(plain)
            print(f"第{idx}行 | MD5: {md5} | 明文: {plain}")

    # 额外输出：所有明文按顺序拼接成一行
    print("\n" + "-" * 50)
    print("所有MD5对应的明文（一行拼接）：")
    print(''.join(plaintext_list))


# -------------------------- 配置参数 --------------------------
MD5_FILE = "md5_list.txt"  # MD5文件路径（确保与代码同目录）
# 完整彩虹表（按你确认的映射）
RAINBOW_TABLE = """7fc56270e7a70fa81a5935b72eacbe29 A
9d5ed678fe57bcca610140957afab571 B
0d61f8370cad1d412f80b84d143e1257 C
f623e75af30e62bbd73d6df5b50bb7b5 D
3a3ea00cfc35332cedf6e5e9a32e94da E
800618943025315f869e4e1f09471012 F
dfcf28d0734569a6a693bc8194de62bf G
c1d9f50f86825a1a2302ec2449c17196 H
dd7536794b63bf90eccfd37f9b147d7f I
ff44570aca8241914870afbc310cdb85 J
a5f3c6a11b03839d46af9fb43c97c188 K
d20caec3b48a1eef164cb4ca81ba2587 L
69691c7bdcc3ce6d5d8a1361f22d04ac M
8d9c307cb7f3c4a32822a51922d1ceaa N
f186217753c37b9b9f958d906208506e O
44c29edb103a2872f519ad0c9a0fdaaa P
f09564c9ca56850d4cd6b3319e541aee Q
e1e1d3d40573127e9ee0480caf1283d6 R
5dbc98dcc983a70728bd082d1a47546e S
b9ece18c950afbfa6b0fdbfa4ff731d3 T
4c614360da93c0a041b22e537de151eb U
5206560a306a2e085a437fd258eb57ce V
61e9c06ea9a85a5088a499df6458d276 W
02129bb861061d1a052c592e2dc6b383 X
57cec4137b614c87cb4e24a3d003a3e0 Y
21c2e59531c8710156d34a3c30ac81d5 Z
0cc175b9c0f1b6a831c399e269772661 a
92eb5ffee6ae2fec3ad71c777531578f b
4a8a08f09d37b73795649038408b5f33 c
8277e0910d750195b448797616e091ad d
e1671797c52e15f763380b45e841ec32 e
8fa14cdd754f91cc6554c9e71929cce7 f
b2f5ff47436671b6e533d8dc3614845d g
2510c39011c5be704182423e3a695e91 h
865c0c0b4ab0e063e5caa3387c1a8741 i
363b122c528f54df4a0446b6bab05515 j
8ce4b16b22b58894aa86c421e8759df3 k
2db95e8e1a9267b7a1188556b2013b33 l
6f8f57715090da2632453988d9a1501b m
7b8b965ad4bca0e41ab51de7b31363a1 n
d95679752134a2d9eb61dbd7b91c4bcc o
83878c91171338902e0fe0fb97a8c47a p
7694f4a66316e53c8cdd9d9954bd611d q
4b43b0aee35624cd95b910189b3dc231 r
03c7c0ace395d80182db07ae2c30f034 s
e358efa489f58062f10dd7316b65649e t
7b774effe4a349c6dd82ad4f4f21d34c u
9e3669d19b675bd57058fd4664205d2a v
f1290186a5d0b1ceab27f4e77c0c5d68 w
9dd4e461268c8034f5c8564e155c67a6 x
415290769594460e2e485922904f345d y
fbade9e36a3f36d3d676c1b808451dd7 z
b14a7b8059d9c055954c92674ce60032 _
c4ca4238a0b923820dcc509a6f75849b 1
c81e728d9d4c2f636f067f89cc14862c 2
eccbc87e4b5ce2fe28308fd9f2a7baf3 3
a87ff679a2f3e71d9181a67b7542122c 4
e4da3b7fbbce2345d7772b0674a318d5 5
1679091c5a880faf6fb5e6087eb1b2dc 6
8f14e45fceea167a5a36dedd4bea2543 7
c9f0f895fb98ab9159f51fd0297e236d 8
45c48cce2e2d7fbdea1afc51c7c6ad26 9
cfcd208495d565ef66e7dff9f98764da 0
f95b70fdc3088560732a5ac135644506 {
cbb184dd8e05c9709e5dcaedaa0495cf }"""

# -------------------------- 执行破解 --------------------------
if __name__ == "__main__":
    crack_md5("output", RAINBOW_TABLE)
