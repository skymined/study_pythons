# class Arithmetic : 곱셈, 나눗셈 추가
# 뺄셈, 곱셈, 나눗셈 실행과 출력


class Arithmetics() : 
    def __init__(self): # 생성사(class가 가지고 있는 자원)
        pass

    def add(self, first, second):
        result=first+second
        return result
    
    def minus(self, first, second):
        result = first-second
        return result
    
    def multi(self,first, second):
        result =first*second
        return result
    
    def divi(self, first, second):
        result = first/second
        return result
    



num_1 = int(input("첫 번째 숫자"))
num_2 = int(input("두 번째 숫자"))

ari = Arithmetics()


print("더할 경우 : {}, 뺄 경우 :{}, 나눌 경우 : {}, 곱할 경우:{}".format(ari.add(num_1, num_2), ari.minus(num_1, num_2), ari.divi(num_1, num_2), ari.multi(num_1, num_2), end=""))