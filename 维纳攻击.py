import math

def continued_fraction_expansion(a, b):
    """
    计算a/b的连分数展开
    返回：连分数系数列表 [q0, q1, q2, ..., qn]
    """
    cf = []
    while b != 0:
        q = a // b
        cf.append(q)
        a, b = b, a % b
    return cf

def convergents(cf):
    """
    从连分数系数计算所有渐进分数
    返回：渐进分数列表 [(h0, k0), (h1, k1), ...]，其中h/k为渐进分数
    """
    conv = []
    h_prev, h_curr = 0, 1
    k_prev, k_curr = 1, 0
    for q in cf:
        # 递推公式：h_n = q_n * h_{n-1} + h_{n-2}, k_n = q_n * k_{n-1} + k_{n-2}
        h_next = q * h_curr + h_prev
        k_next = q * k_curr + k_prev
        conv.append((h_next, k_next))
        h_prev, h_curr = h_curr, h_next
        k_prev, k_curr = k_curr, k_next
    return conv

def wiener_attack(N, e):
    """
    维纳攻击核心逻辑：从e/N的渐进分数中找到私钥d
    返回：私钥d（若找到），否则返回None
    """
    print("开始维纳攻击，求解私钥d...")
    # 步骤1：计算e/N的连分数展开
    cf = continued_fraction_expansion(e, N)
    # 步骤2：计算所有渐进分数
    conv = convergents(cf)
    
    # 步骤3：遍历渐进分数，验证是否为私钥d
    for (k, d) in conv:
        if d == 0:
            continue
        if k == 0:
            continue
        
        # 维纳攻击核心验证：ed - 1 需能被φ(N)整除，且满足 φ(N) ≈ N - 2√N + 1
        if (e * d - 1) % k != 0:
            continue
        
        # 计算φ(N)的候选值：phi = (ed - 1)/k
        phi_candidate = (e * d - 1) // k
        
        # 验证phi_candidate是否合理（构造二次方程 x² - (N - phi_candidate + 1)x + N = 0）
        # 判别式 D = (N - phi_candidate + 1)² - 4*N 需为完全平方数
        b = N - phi_candidate + 1
        D = b * b - 4 * N
        if D < 0:
            continue
        
        # 计算平方根，验证是否为整数
        sqrt_D = int(math.isqrt(D))
        if sqrt_D * sqrt_D != D:
            continue
        
        # 验证p和q是否为整数（p = (b + sqrt_D)/2, q = (b - sqrt_D)/2）
        if (b + sqrt_D) % 2 != 0 or (b - sqrt_D) % 2 != 0:
            continue
        
        p = (b + sqrt_D) // 2
        q = (b - sqrt_D) // 2
        
        # 最终验证：p*q == N 且 e*d ≡ 1 mod phi_candidate
        if p * q == N and (e * d) % phi_candidate == 1:
            print(f"✅ 维纳攻击成功！找到私钥d = {d}")
            print(f"   对应的p = {p}, q = {q}")
            print(f"   对应的φ(N) = {phi_candidate}")
            return d, p, q
    
    # 未找到d（可能d不是小指数，或不满足维纳攻击条件）
    print("❌ 维纳攻击失败：d不是小指数，或不满足维纳攻击条件")
    return None, None, None

# ========== 你的RSA参数 ==========
N = 460657813884289609896372056585544172485318117026246263899744329237492701820627219556007788200590119136173895989001382151536006853823326382892363143604314518686388786002989248800814861248595075326277099645338694977097459168530898776007293695728101976069423971696524237755227187061418202849911479124793990722597
e = 354611102441307572056572181827925899198345350228753730931089393275463916544456626894245415096107834465778409532373187125318554614722599301791528916212839368121066035541008808261534500586023652767712271625785204280964688004680328300124849680477105302519377370092578107827116821391826210972320377614967547827619
enc = 38230991316229399651823567590692301060044620412191737764632384680546256228451518238842965221394711848337832459443844446889468362154188214840736744657885858943810177675871991111466653158257191139605699916347308294995664530280816850482740530602254559123759121106338359220242637775919026933563326069449424391192

# ========== 执行维纳攻击 + 解密 ==========
if __name__ == "__main__":
    # 步骤1：维纳攻击求d
    d, p, q = wiener_attack(N, e)
    
    if d is not None:
        # 步骤2：解密密文
        plain = pow(enc, d, N)
        print("\n🔓 解密结果：")
        print(f"明文（整数）：{plain}")
        
        # 步骤3：转换为字符串
        try:
            plain_hex = hex(plain)[2:]
            if len(plain_hex) % 2 != 0:
                plain_hex = '0' + plain_hex
            plain_str = bytes.fromhex(plain_hex).decode('utf-8')
            print(f"明文（UTF-8字符串）：{plain_str}")
        except UnicodeDecodeError:
            try:
                plain_str = bytes.fromhex(plain_hex).decode('gbk')
                print(f"明文（GBK字符串）：{plain_str}")
            except:
                print("提示：明文为数值型，无需转换为字符串")
        except Exception as e:
            print(f"字符串转换失败：{e}")
    else:
        # 维纳攻击失败时，自动降级为Pollard's Rho分解（备用方案）
        print("\n📌 自动降级为Pollard's Rho分解（极速）...")
        # 导入之前的分解函数（纯Python实现）
        import random
        
        def is_prime(n, k=5):
            if n < 2:
                return False
            for p in [2, 3, 5, 7, 11]:
                if n % p == 0:
                    return n == p
            d = n - 1
            s = 0
            while d % 2 == 0:
                d //= 2
                s += 1
            for _ in range(k):
                a = random.randint(2, n-2)
                x = pow(a, d, n)
                if x == 1 or x == n-1:
                    continue
                for _ in range(s-1):
                    x = pow(x, 2, n)
                    if x == n-1:
                        break
                else:
                    return False
            return True
        
        def pollards_rho(n):
            if n % 2 == 0:
                return 2
            while True:
                c = random.randint(1, n-1)
                f = lambda x: (pow(x, 2, n) + c) % n
                x, y, d = 2, 2, 1
                while d == 1:
                    x = f(x)
                    y = f(f(y))
                    d = math.gcd(abs(x-y), n)
                if d != n:
                    return d
        
        def factor(n):
            if n == 1:
                return []
            if is_prime(n):
                return [n]
            d = pollards_rho(n)
            return factor(d) + factor(n//d)
        
        # 执行分解
        factors = factor(N)
        p, q = factors[0], factors[1]
        print(f"✅ 分解完成：p = {p}, q = {q}")
        
        # 计算d并解密
        phi = (p-1)*(q-1)
        def modinv(a, m):
            g, x, y = math.gcd(a, m), 1, 0
            while m:
                t = a // m
                a, m = m, a % m
                x, y = y, x - t*y
            return x % phi
        
        d = modinv(e, phi)
        print(f"私钥d = {d}")
        plain = pow(enc, d, N)
        print(f"\n明文（整数）：{plain}")
