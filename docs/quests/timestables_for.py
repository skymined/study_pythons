#quest
#구구단 5단 단계별 표시
# ex. 5*1=5, 5*2=10 ... 5*9=45
# 단수 입력받아 연산

a=int(input())

for x in range(1,10):
    print("{}*{}={}".format(a,x,a*x))
    pass

