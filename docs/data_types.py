# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타

# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?
# A. Python B. Java C. JavaScript D. C++ E. 기타

# 3. 어떤 개발 환경(IDE)을 주로 사용하시나요?
# A. Visual Studio Code B. IntelliJ C. PyCharm D. Eclipse E. 기타

#단순 출력
print( "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?")
print(" A. Windows B. macOS C. Linux D. Chrome OS E. 기타")

print( "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?")
print( "A. Python B. Java C. JavaScript D. C++ E. 기타")

#단순 출력  with 변수
str_first = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
print(str_first)
str_second = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
print(str_second)
str_third = "2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
print(str_third)
str_fourth = "A. Python B. Java C. JavaScript D. C++ E. 기타"
print(str_fourth)

print("------------")

# 다른 출력 방식 "{}" 하나는 변수 하나와 매칭

"{} -> {}"
print("{}->{}".format(str_third, str_fourth))