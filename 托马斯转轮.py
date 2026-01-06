key="2,5,1,3,6,4,9,7,8,14,10,13,11,12"
#密文
cipher_text = "HCBTSXWCRQGLES"
  
  
# f = open("zhuanlun.txt")
str_first_encry = [
    "ZWAXJGDLUBVIQHKYPNTCRMOSFE",
    "KPBELNACZDTRXMJQOYHGVSFUWI",
    "BDMAIZVRNSJUWFHTEQGYXPLOCK",
    "RPLNDVHGFCUKTEBSXQYIZMJWAO",
    "IHFRLABEUOTSGJVDKCPMNZQWXY",
    "AMKGHIWPNYCJBFZDRUSLOQXVET",
    "GWTHSPYBXIZULVKMRAFDCEONJQ",
    "NOZUTWDCVRJLXKISEFAPMYGHBQ",
    "QWATDSRFHENYVUBMCOIKZGJXPL",
    "WABMCXPLTDSRJQZGOIKFHENYVU",
    "XPLTDAOIKFZGHENYSRUBMCQWVJ",
    "TDSWAYXPLVUBOIKZGJRFHENMCQ",
    "BMCSRFHLTDENQWAOXPYVUIKZGJ",
    "XPHKZGJTDSENYVUBMLAOIRFCQW"]
  
  
# for line in f:
#     line = line.strip()
#     str_first_encry.append(line)
  
  
key_index = key.split(",")
str_second_encry=[]
for k in key_index:
    str_second_encry.append(str_first_encry[int(k)-1])
    print(str_first_encry[int(k)-1])
  
  
for i,ch in enumerate(cipher_text):
    line = str_second_encry[i]
    split_index = line.index(ch)
    temp=[]
    temp[0:len(line)-split_index+1] = line[split_index:len(line)]
    temp[len(temp):] = line[0:split_index]
    str_second_encry[i] = "".join(temp)
print("-------------------------------------")
for plain in str_second_encry:
    print(plain)
