import gmpy2, libnum


def crt(remainders, mods):
    """
    CRT中国剩余定理求解核心函数
    :param remainders: 余数列表 [r1, r2, ..., rn]
    :param mods: 模数列表 [m1, m2, ..., mn] (两两互质)
    :return: 方程组唯一解x
    """
    x = 0
    # 步骤1：计算模数总乘积
    M_total = 1
    for m in mods:
        M_total *= m
    # 步骤2+3：遍历计算+累加
    for r, m in zip(remainders, mods):
        M_k = M_total // m  # 计算Mk
        invM_k = gmpy2.invert(M_k, m)  # 计算逆元（核心）
        x = (x + r * M_k * invM_k) % M_total
    return x


# ==================== 本题调用示例（直接复用）====================
# a_list: 从s解析的p%i余数列表 | I_list: 解析的素数i列表

E = 0x10000


# 获取64个大于等于65537的因子,组合模数列表
def get_e_list():
    current_value = E
    temp = []
    for i in range(1, 0x41):
        current_value = gmpy2.next_prime(current_value)
        # print(current_value,end=',')
        temp.append(current_value)
    return temp


elist = get_e_list()

s = [
    '0001f5b25e99',
    '0003738b830b',
    '000712196449',
    '000f41395298',
    '0015f3167995',
    '001b3ee75d91',
    '002b1c7c598d',
    '002d684e5258',
    '0033dee483b2',
    '003f082e9964',
    '00491997a7ce',
    '0051a6c8b451',
    '005d07469658',
    '006129429925',
    '006f537549d5',
    '007386107291',
    '0079f9a518cc',
    '008df28cdd83',
    '0097f4c7e17b',
    '00a32f3f34bd',
    '00a5fb482f1a',
    '00ab8db3d8ae',
    '00b1ac522030',
    '00b5aded5bfe',
    '00b714303666',
    '00c18e305ba1',
    '00c38b99f954',
    '00e13a6bfc41',
    '00f1e0a577c4',
    '00fdd19c0791',
    '01119d2317f8',
    '01235a9e9365',
    '0127f964d580',
    '012d04e5e82a',
    '012f9e2c6424',
    '013330203ac0',
    '013b6ef06b65',
    '014b3d4d9843',
    '0159b1b8a48c',
    '016b1ec5aad7',
    '01819e6c0d78',
    '018791fe0684',
    '01896ea1b69a',
    '019f411527da',
    '01a5bed182d6',
    '01abf6cd2ff3',
    '01bde0d0e78c',
    '01bf4d27174a',
    '01c972210493',
    '01edd9d1ad04',
    '01f51b02ebaf',
    '01f9de167aef',
    '01ff4afd61ba',
    '0213d864bc0d',
    '0217884171c4',
    '0223f2eac3be',
    '02294c6b56ec',
    '0237095602f7',
    '023bccb9f2c7',
    '023dd4b8cba8',
    '0259d76e16ae',
    '02712383d3ee',
    '0279d31bd536',
    '027dd1132b71',
]

p_list = []
q_list = []

for i in s:
    temp_p = int(i[4:8], 16)
    # print(temp_p)
    p_list.append(temp_p)
    temp_q = int(i[8:12], 16)
    q_list.append(temp_q)


p = crt(p_list, elist)  # CRT求解p
q = crt(q_list, elist)  # CRT求解q
print(f"✅ CRT求解得到p = {p}")
print(f"✅ CRT求解得到q = {q}")

phi_n = (p - 1) * (q - 1)

d = gmpy2.invert(65537, phi_n)

n = p * q

c = 15475360999368650197289005472185581152069060634283693323946052965960589519581617455506352219490629566918460375380785814866402494147927750945480098521812138945136749723819137845883299889021416260332340178283510823030873351611619417221376364771970896181883046193073239204691348178934840121119255047703623363776102840901094913360936893794831526158811141875475591783419643997840334620232088220736832676198976140933444280092621888577300822365100141866394749645653768275658897113185158636749417282906289720331156043400848893751904936196506453076968720653786855369121200180627428793758749583878625051356019271855777009538880

m = pow(c, d, n)

flag = libnum.n2s(int(m))
flag = flag.decode("utf-8")
print(flag)
