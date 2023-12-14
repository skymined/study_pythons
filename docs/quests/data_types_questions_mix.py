# 문제작성(input으로 직접 입력)과 내용 출력
# print(list_question_mix)


def make_list_question_mix (x):
    dict_input = {}
    dict_input["question"] = input("Question을 입력하시오.")
    list_answer_input=[]
    for a in range(4):
        list_answer_input.append(input("{}번 째 답을 입력하시오.".format(a+1)))
    dict_input["answer"]=list_answer_input
    dict_input["correct_index"] = input("인덱스를 입력하시오.") 
    dict_input["score"] = input("점수를 입력하시오.")

    return dict_input

list_question_mix=[]
list_question_mix.append(make_list_question_mix(1))
list_question_mix.append(make_list_question_mix(2))
list_question_mix.append(make_list_question_mix(3))
 
pass

for total_list in list_question_mix :
    question = total_list["question"]
    answer = total_list["answer"]
    correct_index = total_list["correct_index"]
    score = total_list["score"]
    print("Question: {}".format(question))
    for x in range(4) :
        print("Answer{} : {}".format(x+1,answer[x]))
    print("Correct_index : {}".format(correct_index))
    print("score : {}".format(score))
    
pass

# 리스트 한에 dictionary가 3개 들어가 있음.
# list_question_mix = [
#     {
#         "question": "Python이라는 언어는 어떤 특징을 가지고 있나요?",
#         "answer": ["고급 프로그래밍 언어로 간결하고 읽기 쉬운 문법을 가짐", "HTML과 같은 마크업 언어", "하드웨어를 직접 제어할 수 있는 저급 언어", "한 줄씩 소스 코드를 해석해서 실행하지 않는 언어"],
#         "correct_index": 0,
#         "score": 10
#     },
#     {
#         "question": "Python에서 함수를 어떻게 정의하나요?",
#         "answer": ["'def' 키워드를 사용하여 정의", "'function' 키워드를 사용하여 정의", "'fun' 키워드를 사용하여 정의", "'define' 키워드를 사용하여 정의"],
#         "correct_index": 0,
#         "score": 10
#     },
#     {
#         "question": "Python에서 클래스를 어떻게 정의하고 사용하나요?",
#         "answer": ["'class' 키워드를 사용하여 정의", "'object' 키워드를 사용하여 정의", "'cls' 키워드를 사용하여 정의", "'new' 키워드를 사용하여 정의"],
#         "correct_index": 0,
#         "score": 10
#     }
# ]