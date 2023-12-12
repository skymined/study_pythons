# 같은 폴더에 있는 클래스 호출
# import를 사용함
# special variables는 내부에 가지고 있는 것이고 나머지는 우리가 선언한 것

import classes_format

# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance (클래스 호출)
person = classes_format.Person()
arithmetics = classes_format.Arithmetics()   # 매번 앞에 classes_format을 넣어줘야 하는가? - > 대부분은 그냥 클래스 이름을 사용할 수 있도록 해둠
class_name = classes_format.Class_name()
# 3. call function
person.add_age()


# 2차적인 방법!
from classes_format import Person, Arithmetics, Class_name
Person() # 을 바로 호출할 수 있음