class Unit:
      
    def __init__ ( self, name, hp, speed ):    

        self.name = name
        self.hp = hp
        self.speed = speed
            
    def move ( self, location ) : 
        print( "[지상 유닛 이동]" )
        print( "{0} : {1} 방향으로 이동합니다. [ 속도 {2}]".format( self.name, location, self.speed ))


class AttackUnit( Unit ):
          
    def __init__ ( self, name, hp, speed, damage ):    

        Unit.__init__(self, name, hp, speed ) #부모 클래스 다시 초기화
        self.damage = damage



    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.". format(self.name. damage))
        self.hp -= damage

        print("{0} : 현재 채력은 {1} 입니다" . format(self.name. self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다."  . format(self.name))


class Flyable:
    def __init__ ( self, flying_speed ) :
        self.flying_speed = flying_speed

    def fly (self, name, location ) :
        print ( "{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format( name, location, self.flying_speed ))



class FlyableAttackUnit ( AttackUnit, Flyable ):
    def __init__ ( self, name, hp, damage, fly_speed ):

                 
       AttackUnit. __init__ ( self, name, hp, 0, damage )
       Flyable. __init__ ( self, fly_speed )
                
                
    def move ( self, location ) :
        print ( "[공중 유닛 이동 ]" )
        self.fly ( self.name, location )



vulture = AttackUnit( "벌쳐", 80, 10, 20 )       
battlecruiser = FlyableAttackUnit( "배틀크루저", 500, 25, 3 )

vulture.move ( "3시" )
battlecruiser.move ( "9시" )
