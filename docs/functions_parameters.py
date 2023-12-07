def add(first, second):
   first=5
   second=4
   sum =first+second
   #return =0
   return =sum #상수 대신에 변수 사용

first = 5
second = 4
# num_sum()
num_sum = add(5,4)
print("add() return 결과 : {}".format(num_sum))


# 내 점수를 넣으면 학점이 나오는 function
def return_grade(my_score) :
   my_grade=""
   if my_score >=90 :
      my_grade = "A"
    elif my_score >80 :
      my_grade = "B"
    else : 
      my_grade = "F"
    return my_grade

str_grade = return_grade(99)
