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

for index,k in enumerate(key_index):
    str_second_encry.append(str_first_encry[int(k)-1])
   
  
for i in  str_second_encry:
    print(i)
    
print("-------------------------------------")
  
for i,ch in enumerate(cipher_text):
    line = str_second_encry[i]
    find_index=line.index(ch)
    temp1=[]
    temp2=[]
    temp1[:find_index]=line[find_index:]
    temp2[find_index+1:]=line[:find_index]
    new_line=''.join(temp1)+''.join(temp2)
    # print(new_line)
    str_second_encry[i]=new_line
     
 
print("-------------------------------------")
for plain in str_second_encry:
    print(plain)
    
print("-------------------------------------")    
for i in range(len(str_second_encry[0])):
    for j in str_second_encry:
        print(j[i].lower(),end='')
    print('\n')
