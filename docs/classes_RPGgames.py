# function만 사용해 적 캐릭터 만들기

#function만 사용할 때의 제한을 극복하기 위해 class를 사용함

class Enemy : 
    def __init__ (self, name, health): #self에는 enemy에 있는 모든 리스트들이 다 들어가게 된다. 즉, Enemy와 self는 모두 공통된 것이라 할 수 있음. #넣고 싶은 변하고 싶은 변수를 뒤에 넣기.name과 health
        self.name = name #외부 변수 name 값이 내부 변수 self.name에 할당되는 것.
        self.health =0
        self.damage =0
        pass

    def attack(self, damage):
        self.health = self.health - damage # 여기서 만약 self.damage로 한다면 내부에 있는 값인 0으로 고정됨.
        return self.health
    
    def function_name(self):
        pass        
        return 0
    
    
first_enemy = Enemy('first', 150) #__init__를 호출한 것. 자신의 자원(function과 variable) 확인
second_enemy =  Enemy('second', 300)
pass