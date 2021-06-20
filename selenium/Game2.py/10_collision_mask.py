#충돌처리(mask)

import os
import pygame
import math

#집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__ (self, image, position):
        super().__init__()
        self.image = image 
        self.original_image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw,0)
        self.position = position

        self.direction = LEFT #집게의 이동방향
        self.angle_speed = 2.5 #집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 #최초 각도 정의 (오른쪽 끝)
        


    def update(self, to_x):
        if self.direction == LEFT: #왼쪽방향으로 이동하고 있다면
            self.angle += self.angle_speed #이동 속도만큼 각도 증가
        elif self.direction == RIGHT: #오른쪽 방향으로 이동하고 있다면
            self.angle -= self.angle_speed

        #만약에 허용 각도 범위를 벗어나면?
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)


        self.offset.x += to_x

        self.rotate() #회전처리

        
    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
         #회전대상이미지, 회전각도, 이미지크기(스케일)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.position + offset_rotated)

    def set_direction(self, direction):   
        self.direction = direction
          

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT



#보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self,image, position, price, speed):
        super().__init__()

        #sprite를 쓰려면 아래 두가지를 반드시 초기화 해줘야함
        self.image = image
        self.rect = image.get_rect(center=position) 
        self.price = price
        self.speed = speed
 
    def set_position(self, position, angle):
        r = self.rect.size[0] // 2 #동그라미 이미지 기준으로 반지름
        rad_angle = math.radians(angle) #각도
        to_x = r * math.cos(rad_angle) #삼각형의 밑변
        to_y = r * math.sin(rad_angle) #삼각형의 높이

        self.rect.center = (position[0] + to_x, position[1] + to_y)
        

def setup_gemstone():
    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2
    diamond_price, diamond_speed = 600, 7


    #작은 금 (좌표는 튜플로 감싼형태로)
    small_gold = Gemstone(gemstone_images[0],(200,380),small_gold_price,small_gold_speed ) #0번째 이미지를 (200, 380) 위치에
    gemstone_group.add(small_gold) #그룹에 추가
    # 큰 금 
    gemstone_group.add(Gemstone(gemstone_images[1], (300,500),big_gold_price, big_gold_speed))  
    #돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300,380),stone_price,stone_speed))
    #다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900,420),diamond_price, diamond_speed))


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) #튜플 형태로 
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()


#게임 관련 변수
default_offset_x_claw = 40
to_x = 0 # 좌표 기준으로 깁게 이미지를 이동시킬 값 저장 변수
caught_gemstone = None # 집게를 뻗어서 잡은 보석 정보



#속도 변수
move_speed = 12    #발사할때 이동 스피드 (x좌표 기준으로 증가되는 값)
return_speed = 20  #아무것도 없이 돌아올때



#방향변수
LEFT = -1 #왼쪽방향
STOP = 0 #이동 방향이 좌우가 아닌 고정인 상태 (집게를 뻗음)
RIGHT = 1 #오른쪽방향

#색깔변수
RED = (255,0,0)
BLACK = (0,0,0)

#배경이미지 불러오기
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환 (Game.py)
background = pygame.image.load(os.path.join(current_path,"background.png"))
  

#4개의 보석이미지 불러오기(작은 금,큰 금, 돌, 다이아몬드)
gemstone_images = [
   pygame.image.load(os.path.join(current_path,"small_gold.png")).convert_alpha(),
   pygame.image.load(os.path.join(current_path,"large_gold.png")).convert_alpha(),
   pygame.image.load(os.path.join(current_path,"stone.png")).convert_alpha(),
   pygame.image.load(os.path.join(current_path,"diamond.png")).convert_alpha()]

#보석 그룹 
gemstone_group =pygame.sprite.Group()
setup_gemstone() #게임에 원하는 만큼의 보석을 정의

#집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha()
claw = Claw(claw_image, (screen_width // 2, 110)) #가로위치는 화면 가로크기 기준 절반, 로는 위에서 110px 정도




running = True  
while running:
    clock.tick(30) #FPS값이 30 으로 고정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #마우스를 버튼 누를 때 집게를 뻗음
            claw.set_direction(STOP)             #좌우 멈춤 상태
            to_x = move_speed                    #move_speed만큼 빠르게 쭉 뻗음

    if claw.rect.left < 0 or claw.rect.right >  screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
    if claw.offset.x < default_offset_x_claw: #원위치에 오면
        to_x = 0
        claw.set_init_state() #처음 상태로 되돌림

        if caught_gemstone: #잡힌 보석이 있다면  
            # update_score(caught_gemstone.price) #점수 업데이트 처리
            gemstone_group.remove(caught_gemstone) # 그룹에서 잡힌 보석 제외
            caught_gemstone = None

    if not caught_gemstone: #잡힌 보석이 없다면 충돌 체크
        for gemstone in gemstone_group:
            #if claw.rect.colliderect(gemstone.rect): #직사각형 기준으로 충돌 처리
            if pygame.sprite.collide_mask(claw,gemstone): #투명 영역 제외하고 실제 이미지 존재하는 영역에 대해 충돌 처리
                caught_gemstone = gemstone #잡힌 보석
                to_x = -gemstone.speed #잡힌 보석의 속도에 - 한 값을 이동 속도로 설정
                break
    
    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center, claw.angle)

    screen.blit(background, (0,0))
    
    gemstone_group.draw(screen) #그룹 내 모든 스트라이프를 screen에 그림
    claw.update(to_x)
    claw.draw(screen)


    pygame.display.update()

    
pygame.quit()

