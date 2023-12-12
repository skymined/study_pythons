import os #os 가 가지고 있는 내장함수들을 바로 사용할 수 있음

#현재 폴더 위치를 알려줌 CLI : pwd
os.getcwd() 
current_folder=os.getcwd() #값을 뱉어내는 아이라서 굳이 안에 변수를 넣을 필요가 없음.
print("현재 실행되는 파이썬 위치{}".format(current_folder))\

#현재 폴더 안에 있는 파일과 폴더 리스트 출력
file_folder_list = os.listdir(current_folder)
print("파일과 폴더 리스트 : {}".format(file_folder_list))