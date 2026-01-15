from PIL import Image

data = []

with Image.open("file.jpg") as myimg:
    frame = myimg.convert("L")
    wdith, height = frame.size
    print(wdith, height)
    for i in range(0, height, 20):
        for j in range(0, wdith, 20):
            temp = frame.getpixel((j, i))
            if temp < 100:
                data.append(1)
            elif temp > 200:
                data.append(0)


for i in range(0, len(data), 25):
    print(data[i : i + 25])  # 从索引i开始，切片取25个元素，打印一行


# 1. 源数据：一维列表(625个元素)
one_list = data

# 2. 目标容器：初始化25×25的二维列表（全0）
erwei = [[0 for x in range(25)] for _ in range(25)]

# 3. 核心：一维列表 → 二维列表 填充数据
index = 0  # 一维列表的索引，从0开始
for y in range(25):  # 遍历二维列表的每一行（y是行号 0-24）
    for x in range(25):  # 遍历该行的每一列（x是列号 0-24）
        erwei[y][x] = one_list[index]  # 赋值填充
        index += 1  # 索引+1，取下一个元素

print("=====================================================")

step = 1
huakuai_wdith = 5
huakuai_height = 5

# 原矩阵尺寸
mat_h = len(erwei)  # 矩阵行数
mat_w = len(erwei[0])  # 矩阵列数

str_list = []

# 核心：双重循环实现滑块滑动
print("\n===== 5x5滑块在25x25矩阵上完整滑动 =====")
# 控制滑块的【起始行】，范围：0 ~ mat_h-huakuai_height
for start_row in range(mat_h - huakuai_height + 1):
    # 控制滑块的【起始列】，范围：0 ~ mat_w-slide_w
    for start_col in range(mat_w - huakuai_wdith + 1):
        # 提取当前滑块的5x5数据：切片取值
        slide_window = [
            hang[start_col : start_col + huakuai_wdith]
            for hang in erwei[start_row : start_row + huakuai_height]
        ]

        # 打印当前滑块信息 + 滑块内的数据
        # print(f"\n滑块起始位置：行={start_row}, 列={start_col} → 5x5滑块数据：")
        slid = ''
        for line in slide_window:
            slid += ''.join(str(x) for x in line)
            # print(temp,end='')
        str_list.append(slid)

MORSE_MAP = {
    # 字母
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
}
str_list2 = []
for line in str_list:
    if len(line.split('00')) >= 3:
        if (
            line.split('00')[0] != ''
            and line.split('00')[1] != ''
            and line.split('00')[2] != ''
        ):
            temp = line.split('00')
            # print(temp)
            print(temp[:3])
            str_list2.append(temp[:3])


# 定义处理单个字符串的核心函数
def process_str(s):
    """
    处理单个01字符串：按0拆分 → 1替换为. → 连续≥2个1替换为-
    :param s: 原始01字符串，如 '0101111101'
    :return: 处理后的字符串片段列表
    """
    # 步骤1：用0拆分当前字符串
    split_list = s.split('0')
    # 步骤2：遍历拆分后的每个片段，执行替换规则
    res = []
    for piece in split_list:
        if piece == '1':  # 只有1个连续的1 → 替换成 .
            res.append('.')
        elif piece == '11':  # 有2个连续的1 → 替换成 -
            res.append('-')
        else:
            break
    return res


# 核心：遍历二维列表，逐个处理所有字符串
final_result = []

# 遍历每一个子list
for sub_list in str_list2:
    processed_sub = []
    # 遍历子list中的每一个字符串
    for single_str in sub_list:
        processed_str = process_str(single_str)
        processed_sub.append(''.join(str(x) for x in processed_str))
    final_result.append(processed_sub)

# 打印格式化的结果，方便查看
print("处理完成后的结果：")
print("-" * 60)
ans_list = []
for item in final_result:
    flag = True
    for x in item:
        if x in MORSE_MAP:
            continue
        else:
            flag = False
            break
    if flag:
        ans = ''.join([MORSE_MAP[y] for y in item])
        if ans not in ans_list:
            ans_list.append(ans)

for i in ans_list:
    print(i, end=',')
