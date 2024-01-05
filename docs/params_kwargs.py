from typing import Optional
class kwargs:
    def __init__(self,
        email: str = None,
        pswd: str = None,
        manager: str = None,
        name: str = None,
        sellist1 : str = None,
        text : str = None) -> None:
        self.name = name
        self.pswd = pswd
        self.email = email
        pass

if __name__ == "__main__":
    user = {
        "pswd": "Password123!"
        ,"email": "chulsoo.kim@example.com"
        ,"name": "김철수"
    }
    # kwargs(email=user["email"], name=user['name']) 기존의 방식. 하지만 만약 항목이 늘어난다면?

    # kwargs(**user) # 딕셔너리를 통째로 function을 통해 넘겨줄 때 사용함-**- 
    kwargs(user) # 이렇게 할 경우에는 통째로 email에 세팅됨.
    pass