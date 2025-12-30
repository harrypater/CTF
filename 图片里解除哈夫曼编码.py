from PIL import Image
import libnum
import base64

from matplotlib.pyplot import switch_backend

im = Image.open("mumumisc.png")

(w, h) = im.size
w = 5  # 信息只有5个块宽度
# print(w, h)
flag = ''

for x in range(w):
    for y in range(h):
        p = im.getpixel((x, y))
        if p == (0, 0, 0):
            flag += '1'
        elif p == (255, 255, 255):
            flag += '0'

# print(flag)
# 二进制转字节串
myfalg = libnum.n2s(int(flag, 2))
temp = base64.b64decode(myfalg)
temp = temp.decode("utf-8")
temp_list = temp.split(' ')

for i in temp_list:
    match i:
        case '110001':
            print('f', end='')
        case '101':
            print('m', end='')
        case '00000':
            print('l', end='')
        case '00001':
            print('h', end='')
        case '0001':
            print('i', end='')
        case '001':
            print('s', end='')
        case '010':
            print('a', end='')
        case '11101':
            print('n', end='')
        case '0110':
            print('g', end='')
        case '0111':
            print('u', end='')
        case '1101':
            print('d', end='')
        case '11001':
            print('{', end='')
        case '110000':
            print('c', end='')
        case '1111':
            print('o', end='')
        case '101':
            print('m', end='')
        case '101':
            print('m', end='')
        case '100':
            print('-', end='')
        case '111001':
            print('e', end='')
        case _:
            print('#', end='')
