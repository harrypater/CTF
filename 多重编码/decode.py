import html
import base64,re

from urllib.parse import unquote

import urllib

with open("base.txt",'r') as f:
    c=f.read()
    # print(c)
    
    c_1=base64.b64decode(c).decode('utf-8')
    # print(c_1)
    
    C2 = re.findall(r'\d+',c_1)
    # print(C2)
    
    c3=''
    
    for x in C2:
        c3+=chr(int(x,8))
        
    # print(c3)
    
    c4=c3.split('\\x')
    c4.pop(0)
    
    # print(c4)
    
    C5 = ''
    for i in c4:
        C5 += chr(int(i,16))

    # print(C5)
    
    C6 = C5.encode('utf-8').decode('unicode-escape')

    
    C6=C6.split('String.fromCharCode(')[1][:-1]
    C6=C6.split(',')
    # print(C6)
    
    
    c7=''
    for i in C6:
        c7+=chr(int(i))
    
    # print(c7)
    
    c8=html.unescape(c7)
    
    # print(c8)
    
    c8=html.unescape(c8)
    
    # print(c8)
    
    C9 =unquote(c8)
    print(C9)
