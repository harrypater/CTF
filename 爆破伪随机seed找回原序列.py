import random

# ===================== 1. 核心工具函数（单独封装，功能明确） =====================
def get_reverse_map(list_length, seed):
    """
    功能：根据种子，获取「打乱后位置 → 原始索引」的映射关系
    作用：知道这个映射，就能把打乱后的列表还原成原始列表
    """
    # 生成原始索引列表 [0,1,2,...列表长度-1]
    original_indexes = list(range(list_length))
    # 用指定种子打乱索引（模拟原始打乱过程）
    random.seed(seed)
    random.shuffle(original_indexes)
    # 构建反向映射：打乱后的位置 → 原始索引
    reverse_map = {}
    for shuffled_pos, original_idx in enumerate(original_indexes):
        reverse_map[shuffled_pos] = original_idx
    return reverse_map

def restore_original_list(shuffled_list, reverse_map):
    """
    功能：根据反向映射，还原打乱前的原始列表
    参数：
        shuffled_list：打乱后的列表
        reverse_map：get_reverse_map生成的反向映射
    """
    list_length = len(shuffled_list)
    original_list = [None] * list_length  # 初始化原始列表容器
    # 按反向映射，把打乱后的元素放回原始位置
    for shuffled_pos in range(list_length):
        original_idx = reverse_map[shuffled_pos]  # 找到原始位置
        original_list[original_idx] = shuffled_list[shuffled_pos]
    return original_list

# ===================== 2. 固定配置（所有参数集中管理，一目了然） =====================
# 目标要匹配的前缀（只要前5位不是这个，直接跳过）
TARGET_PREFIX = "flag{"
# 二进制字符串列表（你的原始数据，已补前导0，固定29位）
BIN_STR_LIST = [
    '11101111010111110100111111111',
    '10111111101011111111100111110',
    '01010101111110011011101100101',
    '11100010000111001000100110111',
    '01000010000111110111001011011',
    '01010101010101100000001101011',
    '01111001001110100000101110101'
]
# 种子范围（要枚举的区间）
SEED_START = 114514
SEED_END = 1919810
# 二进制字符串长度（固定29位，提前算好）
BIN_CHAR_LENGTH = len(BIN_STR_LIST[0])

# ===================== 3. 预处理数据（只做一次，避免重复劳动） =====================
# 把每个二进制字符串转成字符列表（比如 "101" → ['1','0','1']）
# 后续逆向操作直接用这个列表，不用重复转换
bin_char_lists = [list(bin_str) for bin_str in BIN_STR_LIST]

# ===================== 4. 核心破解逻辑（分步拆解，每步都有说明） =====================
print("开始破解，种子范围：{} ~ {}".format(SEED_START, SEED_END))
print("="*50)

# 枚举每个种子（带进度提示，知道破解到哪了）
total_seeds = SEED_END - SEED_START + 1
progress_step = 10000  # 每10000个种子打印一次进度

for seed in range(SEED_START, SEED_END + 1):
    # ---------- 进度提示（可选，方便监控） ----------
    if seed % progress_step == 0:
        progress = (seed - SEED_START) / total_seeds * 100
        print("当前进度：{:.2f}% | 正在测试种子：{}".format(progress, seed))
    
    # ---------- 步骤1：计算反向映射（每个种子只算一次） ----------
    # 因为所有二进制字符串长度都是29位，所以映射关系通用
    reverse_map = get_reverse_map(BIN_CHAR_LENGTH, seed)
    
    # ---------- 步骤2：还原所有二进制字符串的原始顺序 ----------
    restored_bin_lists = []  # 存储每个二进制字符串还原后的列表
    for char_list in bin_char_lists:
        # 还原当前二进制字符串的原始顺序
        restored_list = restore_original_list(char_list, reverse_map)
        restored_bin_lists.append(restored_list)
    
    # ---------- 步骤3：组装字符并验证（剪枝提速关键） ----------
    flag_chars = []  # 存储组装后的flag字符
    is_match = True  # 标记是否匹配目标前缀
    
    for i in range(BIN_CHAR_LENGTH):
        # 组装第i位的二进制字符串（从7个还原后的列表中各取第i位）
        bin_char = ""
        for restored_list in restored_bin_lists:
            bin_char += restored_list[i]
        
        # 二进制转十进制，再转字符（异常处理：避免无效二进制）
        try:
            char = chr(int(bin_char, 2))
        except ValueError:
            is_match = False
            break  # 无效二进制，直接跳过当前种子
        
        flag_chars.append(char)
        
        # ---------- 剪枝：前5位不匹配，直接跳过 ----------
        if i < len(TARGET_PREFIX):
            if char != TARGET_PREFIX[i]:
                is_match = False
                break  # 不用算后续字符，直接试下一个种子
    
    # ---------- 步骤4：验证并输出结果 ----------
    if is_match and "".join(flag_chars[:5]) == TARGET_PREFIX:
        final_flag = "".join(flag_chars)
        print("\n✅ 找到目标Flag：", final_flag)
        print("✅ 匹配的种子：", seed)
        break

print("\n破解完成！")
