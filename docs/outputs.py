## 변수 선언 후 정의 시 고려점 (넣는 값이 문자 or 숫자)
# 문자 출력
helloworld = "Hello, World! Juehyeon Noh." # 문자형 변수
print(helloworld)

print("Hello, World! Juehyeon Noh.") #상수
# 숫자 합산 출력
numbers = 3 + 5 # 숫자형 변수
print(numbers)

#데이터 타입 : 문자형 or 숫자형 등 변수에 대한 정의 


# 가정문
if 5 > 2: # 묶음 기호인 :과 tab은 하나의 쌍
    pass #디버깅할 때 유용
    print("Five is greater than two!")
print("end")

# 한줄에 출력
first = "First"
second = "Second"
print("first : {}! ".format(first), end=", 다음 줄 ")
print("second : {}! ".format(second))
print("End program!")