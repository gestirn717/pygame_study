from random import *

#일반유닛

class Unit:
      
    def __init__ ( self, name, hp, speed ):    

        self.name = name
        self.hp = hp
        self.speed = speed
        print( "{0} 유닛이 생성되었습니다." .format(name))
            
    def move ( self, location ) : 
        print( "{0} : {1} 방향으로 이동합니다. [ 속도 {2}]".format( self.name, location, self.speed ))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ". format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 채력은 {1} 입니다" . format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다."  . format(self.name))


#공격 유닛
#상속받고 싶은 클래스 ( ) 안에 넣어줌 / 위에서 정의해준거 재정의 
#일반 유닛 상속받아 공격유닛 생성

class AttackUnit( Unit ):
      
    def __init__ ( self, name, hp, speed, damage ):    

        Unit.__init__(self, name, hp, speed ) #부모 클래스 다시 초기화
        self.damage = damage



    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format( self.name, location, self.damage))

#마린

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40 ,1,5)

    #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 못합니다.".format(self.name))

#탱크

class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜 , 더 높은 파워로 공격 가능. 이동 불가
    #모든 탱크에 적용 할거니까 클래스 바로밑에서 정의

    seize_developed = False #시즈모드 개발여부
      
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1,35)
        self.seize_mode = False


    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        #현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *=2
            self.seize_mode = True
        
        #현재 시즈모드 일때 -> 시즈모드 해제 
        else:
            print("{0} : 시즈모드 헤제합니다".format(self.name))
            self.damage /=2
            self.seize_mode = False

#드랍쉽 : 공중유닛, 수송기 . 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X
#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__ ( self, flying_speed ) :
        self.flying_speed = flying_speed

    def fly (self, name, location ) :
        print ( "{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format( name, location, self.flying_speed ))
              


 #공중 공격 유닛 클래스
 #공격유닛, 공중유닛 상속받기
class FlyableAttackUnit ( AttackUnit, Flyable ):
    def __init__ ( self, name, hp, damage, fly_speed ):

    # 지상 speed는 0으로 처리
        AttackUnit. __init__ ( self, name, hp, 0, damage )
        Flyable. __init__ ( self, fly_speed )
                
    #무브 재정의
    def move ( self, location ) :
        self.fly ( self.name, location )



class Wraith(FlyableAttackUnit):
    def __init__ (self):
        FlyableAttackUnit. __init__ (self, "레이스", 80, 20, 5)
        self.clocked = False    #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드 -> 모드 해제
           print("{0} : 클로킹 모드를 해제합니다" .format(self.name))
           self.clocked = False
        else:
            print("{0} : 클로킹 모드를 설정합니다" .format(self.name))
            self.clocked = True


#건물 
# 건물은 이동 못한다 치고 스피드를 0으로
#super를 쓰면 ( ) 해주고 self 없애줌

class BuildingUnit( Unit ) :
    def __init__ ( self, name, hp, location ) : 

    #Unit. __init__ ( self, name, hp, 0 )
        super( ). __init__ ( name, hp, 0 )

        self.location = location

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


#실제 게임 시작
game_start()

#마린 3기
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기
t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")



#공격 모드 준비 ( 탱크 시즈 모드, 레이스 클로킹, 마린 스팀팩)
#isinstance 지금 만들어진 개체가 어떤 클래스의 인스턴스 인지 확인하는 것
#attack_units에는 서로 다른 클래스의 객체가 있으므로 각 객체가 특정 클래스의 개체인 지 확인 후 처리
# 마린의 경우 unit이 Marine이면 스팀팩 사용하도록

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
         unit.clocking()
        
#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해 (데미지 랜덤으로)
for unit in attack_units:
    unit.damaged(randint(5,21))

#게임 종료
game_over()