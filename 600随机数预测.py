from pyrandcracker import RandCracker

data=[]
with open("data.txt","r") as f:   
    for i in range(600):          #读取题目提供的600个随机数
        data.append(int(f.readline()))  

rc = RandCracker()                #构建RandCracker对象
for num in data:
    rc.submit(int(num))           #先提交已知的600个随机数
for i in range(624-len(data)):
    rc.submit(0)                  #因为pyrandcracker要求提交624个随机数，所以我们再提交24个0(这些数随便取)，补齐624个！
rc.check()

for i in range(2025-624):         #预测624个之后的随机数，直到预测完2025个
    rc.rnd.getrandbits(32)

res=""  
for j in range(32):               #从2026个开始预测随机数并还原flag
    res+=hex(rc.rnd.getrandbits(32)%16)[2:]
    
print("bugku{"+res+"}")
