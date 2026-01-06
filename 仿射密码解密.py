# 这段代码的目的是解密使用仿射密码加密的文本。仿射密码是一种经典的替换密码，它通过一个线性方程对字母进行映射。具体来说，仿射密码的加密公式是：
#           E(x) = (ax + b) mod n
# 其中：
#       x 是明文中的字母对应的数字位置。
#       a 和 b 是密钥
#       n 是字母表的大小
#       E(x) 是密文中对应位置的字母
 
# 要解密仿射密码，需要使用解密公式：
#       D(y) = a 的 -1 次方 * (y−b) mod n
# 其中：
#       y 是密文中的字母对应的数字位置
#       a 的 -1 次方 是模 n 意义下 a 的逆元
 
import gmpy2
from itertools import *
 
# 解密思路：
#       仿射密码的解密基于找到加密过程中使用的线性变换的逆变换。这需要计算加密参数 a 的模逆 ai
#       对于每个加密字符，通过逆变换找到其在原始字符集中对应的索引，然后取出对应的原始字符
#       如果字符不在字符集中，可能是由于它在加密文本中没有被转换，或者是由于它在加密过程中保持不变
 
# affine_decode 函数：
#       c: 密文字符串
#       a: 加密的第一个参数，用于加密的乘法部分
#       b: 加密的第二个参数，用于加密的平移部分
#       origin: 字母表，表示加密和解密时使用的字符集
def affine_decode(c, a, b, origin="abcdefghijklmnopqrstuvwxyz0123456789"):
    r = ""
 
    # n = len(origin): 计算字母表的大小
    n = len(origin)
 
    #  ai 是 a 在模 n 意义下的逆元素
    ai = gmpy2.invert(a,n)
 
    for i in c:
        # origin.find(i) 检查字符 i 是否在字符集 origin 中。如果字符存在，find 函数返回非 -1 的索引值
        if origin.find(i) != -1:
            # 首先，找到字符 i 在字符集 origin 中的索引
            # 然后，使用仿射密码的解密公式计算原始索引：(ai * (index - b)) % len(origin)
            # 将计算得到的索引对字符集长度 len(origin) 取模，以确保索引在有效范围内
            # 最后，使用这个索引从字符集 origin 中取出解密后的字符，并将其添加到解密字符串 r
            r += origin[(ai*(origin.index(i)-b)) % len(origin)]
        else:
            # 如果字符 i 不在字符集中（例如，可能是标点符号或特殊字符），它将不会被解密，而是直接添加到解密字符串 r
            r += i
 
    return r
 
 
# permutations 函数用于生成给定字符串的所有可能排列
# 生成 “agvr” 的所有长度为 4 的排列（例如：agvr、gvar…………）
for i in permutations("agvr", 4):
    # 结合题目的双 11 来传递密钥
    print(i)
    print(affine_decode("en,i5d8{unw_ad1_f2_pg_8gea}", 11, 11, origin="slbn7q6u0w2pf3m9tzjx8o51yke"+i[0]+i[1]+i[2]+i[3]+"dhc4i"))
