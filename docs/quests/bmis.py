# input : 몸무게, 키
# BMI : 몸무게(kg) / 키(m)^2
# BMI 분류
# 18 미만 : 저체중
# 18-22 : 정상
# 23-24 : 과체중
# 25이상 :비만

put1 = "몸무게(kg)를 입력하십시오."
put2 = "키(m)를 입력하십시오."

# 몸무게 입력
print("{}".format(put1))
weight = int(input())
print("{}".format(put2))
tall = int(input())

BMI = (weight) / (tall**2)

if BMI < 18 :
    print("{}점은 18점 미만이기 때문에 저체중입니다.".format(BMI))
    pass
elif BMI<=22 :
    print("{}점은 18점 이상, 22점 이하이기 때문에 정상 체중입니다.".format(BMI))
    pass
elif BMI <=24 : 
    print("{}점은 23점 이상 24점 이하이기 때문에 과체중입니다.".format(BMI))
    pass
else : 
    print("{}점은 25점 이상이기 때문에 비만입니다.".format(BMI))
    pass