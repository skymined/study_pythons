

# list_fruits = ["melon", "apple", "banana", "cherry"]
# index로 값 가져오기
# list_fruits[0] # 단일 변수로 여김 1차원(행)

def return_list() :
    list_fruits = ["melon", "apple", "banana", "cherry"]  #내용 넣기
    return list_fruits
print("return_list() return result : {}".format(return_list()))


#반복 print 작업 줄이기

def function_name() : 
    my_score=79
    my_grade = ''
    if my_score >=90 : # 90점 이상이면A
        my_grade = 'A'
        pass
    elif my_score >80  #80점 초과면 B
        my_grade = 'B'
        pass
    else : 
        my_grade = 'C'
        pass
    return my_grade

str_grade = return_grade()
print("당신의 학점은 {}입니다.".format(str_grade))