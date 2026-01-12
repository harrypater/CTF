# author: lzq2000   2025.6.12 6:30

# lz77的压缩思想为：向前寻找与本字符串相同的字符串的位置，然后用相对距离和长度(相同的字符数)来简化存储！
# 为了提高效率，用到滑动窗口的方法，就是说向前搜索的范围是一个有限范围，大小固定，但是会不断向后滑动！

# 滑动窗口字节宽度，一般为4KB
swlen=32768 
# 前向搜索缓冲字节宽度，一般不超过100B，可以为32B
abuf=32

# 在滑动窗口(mystr)中搜索是否有匹配substr的字符串
# 如果匹配，返回位置和匹配长度
def searchposlen(mystr, substr): 
    findpos, findlen=-1, -1 
    searchlen=len(substr)
    if len(mystr)<searchlen:                            # 因为本程序的滑动窗口一开始宽度为“0”
        searchlen=len(mystr)                            # 所以，如果子字符串比滑动窗口大，最长字符串就从滑动窗口长度开始搜索即可！
    for i in range(searchlen,0,-1):                     # 从最长字符串的顺序进行查找，例如abcd的查找顺序为：abcd abc ab a 
        findpos = mystr.find(substr[0:i])               # find从左边开始查找！rfind为从右边开始查找
        if(findpos != -1):
            findlen = i
            break
    return(findpos, findlen)

# lz77压缩算法
def lz77(mystr,method="lz77"):                          # method是编码方法，目前有“lz”和“lz77”，默认为lz77
    result  = []                                        # 编码结果列表
    winside = 0                                         # 滑动窗口右边界
    slidewin = ""                                       # 滑动窗口，注意我这里的滑动窗口一开始的宽度为“0”！！！
    mystr="".join(chr(x) for x in mystr.encode('utf-8'))  
    aheadbuf = mystr[0:abuf]                            # 前向搜索缓冲
    while(winside < len(mystr)):
        resultpos, resultlen = searchposlen(slidewin,aheadbuf)
        if(resultpos == -1):                            # 滑动窗口中没有匹配前向搜索缓冲中的字符串
            result.append(ord(aheadbuf[0:1]))
            winside  += 1
            if winside>=swlen:
                slidewin = mystr[winside-swlen:winside] # 滑动窗口向右滑动一个字符
            else:
                slidewin = mystr[0:winside]             # 增加滑动窗口
            aheadbuf = mystr[winside:winside+abuf]      # 前向搜索缓冲向右滑动一个字符
        else:                                           # 有匹配的字符串
            rpos=resultpos
            if len(slidewin)<swlen:                     # 滑动窗口不足swlen宽度，要补齐位置数值
                rpos+=swlen-len(slidewin)
            rpos=swlen-rpos
            if method=="lz":
                result.append((rpos,resultlen))         # 添加一个元组
                winside += resultlen                    # 滑动窗口右边界增加的距离
            else:
                if winside+resultlen < len(mystr):      
                    result.append((rpos,resultlen,ord(mystr[winside+resultlen:winside+resultlen+1])))
                else: 
                    result.append((rpos,resultlen))     # 添加一个元组
                winside += resultlen + 1                # 滑动窗口右边界增加的距离
            if winside>len(mystr):                      # 最后剩余的字符数不够滑动的距离了
                winside=len(mystr)                      # 那么滑动窗口滑到头！
            if winside>=swlen:
                slidewin = mystr[winside-swlen:winside] # 滑动窗口向右滑动
            else:
                slidewin = mystr[0:winside]             # 一开始滑动窗口不足swlen宽度，直接增加滑动窗口宽度
            aheadbuf = mystr[winside:winside+abuf]
    return result

if __name__=="__main__":
    m="测试lz77算法！flag{test}" 
    c=lz77(m)      
    print("lz77压缩结果为：\n"+str(c))

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
解密

#-*- coding: utf-8
import base64
def decompress_lz77(data):
    output = []
    for entry in data:
        if isinstance(entry, int):
            output.append(chr(entry))
        elif isinstance(entry, tuple):
            offset, length, next_char = entry
            start = len(output) - offset
            for i in range(length):
                output.append(output[start + i])
            output.append(chr(next_char))
    return ''.join(output)
f = open('lz77的压缩结果.txt','r')
data = eval(f.read())
result = decompress_lz77(data)
print(base64.b64decode(result).decode())


    


