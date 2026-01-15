import random


step=1
huakuai_wdith=5
huakuai_height=5

# 原矩阵尺寸
mat_h = len(erwei)    # 矩阵行数
mat_w = len(erwei[0]) # 矩阵列数

str_list=[]

# 核心：双重循环实现滑块滑动
print("\n===== 5x5滑块在10x10矩阵上完整滑动 =====")
# 控制滑块的【起始行】，范围：0 ~ mat_h-huakuai_height
for start_row in range(mat_h - huakuai_height + 1):
    # 控制滑块的【起始列】，范围：0 ~ mat_w-slide_w
    for start_col in range(mat_w - huakuai_wdith + 1):
        # 提取当前滑块的5x5数据：切片取值
        slide_window = [
            hang[start_col : start_col+huakuai_wdith] 
            for hang in erwei[start_row : start_row+huakuai_height]
        ]
        
        # 打印当前滑块信息 + 滑块内的数据
        # print(f"\n滑块起始位置：行={start_row}, 列={start_col} → 5x5滑块数据：")
        slid=''
        for line in slide_window:
            slid+=''.join(str(x) for x in line)
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
str_list2=[]
for line in str_list:
    if(len(line.split('00'))>=3):
        if(line.split('00')[0]!=''and line.split('00')[1]!=''and line.split('00')[2]!=''):
            temp=line.split('00')
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
        if piece == '1':        # 只有1个连续的1 → 替换成 .
            res.append('.')
        elif piece =='11':      # 有2个连续的1 → 替换成 -
            res.append('-')
    return res

# 核心：遍历二维列表，逐个处理所有字符串
final_result = []

# 遍历每一个子list
for sub_list in str_list2:
    processed_sub = []
    # 遍历子list中的每一个字符串
    for single_str in sub_list:
        processed_str = process_str(single_str)
        processed_sub.append(''.join(str(x)for x in processed_str))
    final_result.append(processed_sub)

# 打印格式化的结果，方便查看
print("处理完成后的结果：")
print("-" * 60)
for idx, item in enumerate(final_result):
    flag=True
    for x in item:
        if(x in MORSE_MAP):
            continue
        else:
            flag=False
            break
    if(flag):
         ans=''.join([MORSE_MAP[y] for y in item])
         print(f"第{idx+1}行：{ans}")   
        
   
                
    
