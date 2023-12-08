#quest1
#구구단 5단 단계별 표시
# ex. 5*1=5, 5*2=10 ... 5*9=45
# 단수 입력받아 연산

# num_get=int(input())

# for num_count in range(1,10):
#     print("{}*{}={}".format(num_get,num_count,num_get*num_count))
#     pass



#quest2
# [30, 35, 20] 단 대한 출력
# timestables_fors.py -> function 화
# option) [30, 35, 20] 부분 사용자 입력, 'q'이면 종료

### def 하나에 몽땅 넣고 나와서는 함수 하나만 쓸 수 있게 해보기! -----> def 안에 while을 넣으면 뒤에 반복이 안되고 while을 빼면 break도 빼야하고... 무슨 방법 없을까... 고민 후 다시 오기

# def cal(num_get):
#     while True : 
#         if "q" != num_get :
#             for num_count in range(1,10):
#                 num_get = int(num_get)
#                 result = print("{}*{}={}".format(num_get,num_count, num_get*num_count ))
#         elif "q" == num_get : 
#             result = print("End program!")
#             break
#         return result

# num_get = input("숫자를 입력하시오(종료를 원하면 q 입력) : ")
# print(cal(num_get))


### 일단 과제부터 제출하고 보자

def cal(num) :
    for count in range(1,10):
        result = print("{}*{}={}".format(num, count, num*count))
    return result

def ex():
    result = print("프로그램을 종료합니다.")
    return result

while True :
    input_data = input("숫자를 입력하시오(종료를 원하면 q 입력) : ")
    if "q" in input_data : 
        ex()
        break
    elif (input_data=="30" or input_data=="35" or input_data=="20"):
        num =int(input_data)
        cal(num)
    else :
        print("잘못 입력하셨습니다. 30,35,20 중 하나의 숫자를 입력해주세요.")
        print("")

        


