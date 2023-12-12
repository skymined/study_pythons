# list 안에 dic 구성

#key(str) : value(여러 변수 종류 가능)
dict_carinfor_mustang = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price" : 30000
}

dict_carinfor_sonata =    {
    "brand": "Hyundai",
    "model": "Sonata",
    "year": 2020,
    "color": "Black",
    "price": 30000
}

# 한 번에 이 정보들을 전부 전달하고 싶을 때

list_carinfor = [dict_carinfor_mustang, dict_carinfor_sonata]

# "nodel" : "Mustang" 접근 방법
list_carinfor[0]  # 그럼 dictionary 통째로 나옴
dict_cafinfor_index_first = list_carinfor[0]  # 후자는 리스트를 말하고, 첫번째는 dictionary
dict_cafinfor_index_first["model"]   # 해당 dictionary 안에 있는 model이라는 key에 맞는 value

pass


#for로 각 dic 값 출력

for dict_carinfor in list_carinfor:
    brand = dict_carinfor['brand']
    model = dict_carinfor['model']
    print("브랜드 : {}, 모델 : {}".format(brand, model))
    pass