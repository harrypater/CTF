# -*- coding: utf-8 -*-
# @Author  : MARX·CBR
# @File    : 微信Dat文件转图片.py
 
import os
 
txtType = [
    {"type": "jpg", "h1": 0xff, "h2": 0xd8},
    {"type": "png", "h1": 0x89, "h2": 0x50},
    {"type": "gif", "h1": 0x47, "h2": 0x49},
]
 
def imageDecode(f,fn):
    print(f"f:{f} fn:{fn}")
    with open(f, "rb") as dat_read:
        headHex = dat_read.read(2)
        selectTypeCnf = None
        for txtTypeCnf in txtType:
            if txtTypeCnf["h1"] ^ headHex[0] == txtTypeCnf["h2"] ^ headHex[1]:
                selectTypeCnf = txtTypeCnf
                break
        if selectTypeCnf:
            selectTxtType = selectTypeCnf["type"]
            key = txtTypeCnf["h1"] ^ headHex[0]
            print(f"check and find file:{f} is {selectTxtType}. xor value is {key}")
            out=fn+"."+selectTxtType
            with open(out, "wb") as file_write:
                file_write.write(bytes([headHex[0] ^ key, headHex[1] ^ key]))
                for now in dat_read:
                    for nowByte in now:
                        newByte = nowByte ^ key
                        file_write.write(bytes([newByte]))
 
def findFile(f):
    fsinfo = os.listdir(f)
    for fn in fsinfo:
        temp_path = os.path.join(f, fn)
        if not os.path.isdir(temp_path):
            print('文件路径: {}' .format(temp_path))
            print(fn)
            imageDecode(temp_path,fn)
        else:
            ...
 
path = r'./'
findFile(path)
