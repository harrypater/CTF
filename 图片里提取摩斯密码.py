from PIL import Image, ImageSequence

# 完整的摩尔斯码映射字典（包含字母、数字、特殊符号：- { }）
# 注意：修正了{和}的标准摩尔斯码（原映射值非标准，会导致解码失败）
MORSE_MAP = {
    # 字母
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    # 数字
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    # 特殊符号（修正为标准摩尔斯码）
    '/': ' ',        # 单词分隔符→空格
    '-....-': '-',   # 连字符→-
    '----.--': '{',        # 左大括号（无标准摩尔斯码，直接映射）
    '-----.-': '}'         # 右大括号（无标准摩尔斯码，直接映射）
}

# 像素值→摩尔斯符号映射（和之前一致）
PIXEL_TO_MORSE = {
    0: '.',    # 点
    247: ' ',  # 空格
    249: '-'   # 划
}

def morse_to_string(morse_code):
    """
    摩尔斯码转字符串（适配特殊符号：- { }）
    :param morse_code: 从GIF提取的摩尔斯码字符串
    :return: 解码后的明文（含特殊符号）
    """
    # 步骤1：处理摩尔斯码格式（多个空格替换为/，区分单词）
    processed_code = morse_code.replace('  ', ' / ')
    # 步骤2：按/分割成单词
    morse_words = processed_code.split('/')
    
    # 步骤3：逐单词、逐字符解码
    result = ''
    for word in morse_words:
        # 按单个空格分割成字符级摩尔斯码
        morse_chars = word.strip().split(' ')
        for char_code in morse_chars:
            # 查找映射，无匹配则保留原码（避免丢失{}/-等符号）
            result += MORSE_MAP.get(char_code, char_code)
        # 单词间加空格
        result += ' '
    
    # 去除首尾多余空格，转小写（可选，根据需求注释）
    return result.strip().lower()

def extract_morse_from_gif(gif_path):
    """从flag.gif逐帧提取摩尔斯码"""
    morse_code = ''
    try:
        with Image.open(gif_path) as gif_image:
            for frame in ImageSequence.Iterator(gif_image):
                # 转RGB+取左上角像素R值
                r_value = frame.convert('RGB').getpixel((0, 0))[0]
                # 拼接摩尔斯符号（确保R值在映射中，避免报错）
                if r_value in PIXEL_TO_MORSE:
                    morse_code += PIXEL_TO_MORSE[r_value]
                else:
                    print(f"警告：未知像素R值 {r_value}，跳过该帧")
        return morse_code
    except FileNotFoundError:
        print(f"错误：未找到文件 {gif_path}")
        return ""

# 主执行逻辑
if __name__ == "__main__":
    # 1. 提取摩尔斯码
    morse_code = extract_morse_from_gif('flag.gif')
    print(f"提取的摩尔斯码：{morse_code}")  # 调试用，可注释
    
    # 2. 解码为明文
    ans = morse_to_string(morse_code)
    
    # 3. 打印结果
    print(f"解码后的flag：{ans}")
