from PIL import Image, ImageSequence


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
    # 数字
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    # 特殊符号（修正为标准摩尔斯码）
    '/': ' ',  # 单词分隔符→空格
    '-....-': '-',  # 连字符→-
    '----.--': '{',  # 左大括号（无标准摩尔斯码，直接映射）
    '-----.-': '}',  # 右大括号（无标准摩尔斯码，直接映射）
}


def morse_to_string(morse_code):
    """
    :param morse_code: 从GIF提取的摩尔斯码字符串
    :return: 解码后的明文（含特殊符号）
    """
    # 步骤3：逐单词、逐字符解码
    result = ''
    for morse_chars in morse_code.strip().split():
        # 查找映射，无匹配则保留原码（避免丢失{}/-等符号）
        result += MORSE_MAP[morse_chars]
        # 单词间加空格

    # 去除首尾多余空格，转小写（可选，根据需求注释）
    return result.strip().lower()


# 像素值→摩尔斯符号映射（和之前一致）
PIXEL_TO_MORSE = {0: '.', 251: '-', 243: ' '}  # 点  # 杠 # 空格

pixel_list = []  # 存储提取的所有RGB像素点 (R,G,B)

mose_code = ''
with Image.open('flag.gif') as gif_image:
    for frame in ImageSequence.Iterator(gif_image):
        RGB_frame = frame.convert('RGB')
        single_pixel = RGB_frame.getpixel((0, 0))
        pixel_list.append(single_pixel)
        # 转RGB+取左上角像素B值
        b_value = single_pixel[2]
        if b_value in PIXEL_TO_MORSE:
            mose_code += PIXEL_TO_MORSE[b_value]

# print(mose_code)

print(morse_to_string(mose_code))

# with Image.open('hack1.png') as hackpng:
#     for index, pixel in enumerate(pixel_list):
#         write_y = 0
#         wirte_x = index
#         hackpng.putpixel((wirte_x, write_y), pixel)

#     hackpng.save('hack2.png')


# with Image.open('hack2.png') as hackpng:
#     RGB_frame = hackpng.convert('RGB')
#     img_width, img_height = hackpng.size
#     for i in range(img_width):
#         pixel = RGB_frame.getpixel((i, 0))
#         b_value = pixel[2]
#         # print(b_value)
#         if b_value in PIXEL_TO_MORSE:
#             mose_code += PIXEL_TO_MORSE[b_value]

# print(morse_to_string(mose_code))
