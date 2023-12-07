# 사용자 입력 반복 곱셈 계산기
# 'q' 입력 시 종료
# function 2개 사용하기
# 하나는 return으로 하고 하나는 필요하다고 생각되는 function 만들기


def multiply_repeat(num_1, num_2) :
    result = num_1 * num_2
    return result
    
def end_program() :
    result = "프로그램을 종료합니다."
    return result

while True :
    input_data = input()
    if "q" in input_data:
        print(end_program())
        break
    else :
        input_data_1, input_data_2 = map(int, input_data.split())
        print(multiply_repeat(input_data_1, input_data_2))
        pass

