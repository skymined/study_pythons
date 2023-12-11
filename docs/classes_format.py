
# 
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
person = Person()
# 3. call function

# class basic format
# class Class_name :
#     def function_name(self): #self 키워드 필요(class 소속 확인용)
#         pass
#         return 0

# class Person : 
#     def add_age(self):
#         pass
#     print("45세")
#     return 0 


# 사칙연산 되는 class 작성
# 덧셈과 뺼셈
class Arithmetics : 
    def __init__(self) :
        pass
    
def add(first, second) : 
    sum=first+second
    return sum

def minus(first, second):
    result = first-second
    return result

arithmetics = Arithmetics()