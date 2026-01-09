import base64
import hashlib

encrypted_str = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='
key = hashlib.md5('ISCC'.encode()).hexdigest()  # 结果：729623334f0aa2784a1599fd374c120d
key_str=str(key)
print(key)

base64_jiema=base64.b64decode(encrypted_str)
print(base64_jiema)

jiami=''


for index,i in enumerate(base64_jiema):
    if(index>=len(key_str)):
        index-=len(key_str)
    jiami+=key_str[index]
    
for  index,i  in  enumerate(jiami.encode()):
    print(chr((base64_jiema[index]-i+128)%128),end='')


