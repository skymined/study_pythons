#quest
#구구단 5단 단계별 표시
# ex. 5*1=5, 5*2=10 ... 5*9=45
# 단수 입력받아 연산

## Using break

num=0
while True : 
    num = num +1
    result = 5*num
    print("5*{}={}".format(num, result))
    if result==45 :
        pass
        break
    pass
pass


## Not Using break

num=0
while num<9 :
    num=num+1
    result = 5*num
    print("5*{}={}".format(num, result))
pass

