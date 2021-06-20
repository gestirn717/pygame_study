#집개 클래스 만들기
import os
import pygame

#집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__ (self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)


    def draw(self, screen):
        screen.blit(self.image, self.rect)




#보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self,image, position):
        super().__init__()

        #sprite를 쓰려면 아래 두가지를 반드시 초기화 해줘야함
        self.image = image
        self.rect = image.get_rect(center=position) 


def setup_gemstone():
    #작은 금 (좌표는 튜플로 감싼형태로)
    small_gold = Gemstone(gemstone_images[0],(200,380)) #0번째 이미지를 (200, 380) 위치에
    gemstone_group.add(small_gold) #그룹에 추가
    # 큰 금 
    gemstone_group.add(Gemstone(gemstone_images[1], (300,500)))  
    #돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300,380)))
    #다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900,420)))


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) #튜플 형태로 
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

#배경이미지 불러오기
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환 (Game.py)
background = pygame.image.load(os.path.join(current_path,"background.png"))
  

#4개의 보석이미지 불러오기(작은 금, 큰 금 , 돌, 다이아몬드)
gemstone_images = [
   pygame.image.load(os.path.join(current_path,"small_gold.png")),
   pygame.image.load(os.path.join(current_path,"large_gold.png")),
   pygame.image.load(os.path.join(current_path,"stone.png")),
   pygame.image.load(os.path.join(current_path,"diamond.png"))]

#보석 그룹 
gemstone_group =pygame.sprite.Group()
setup_gemstone() #게임에 원하는 만큼의 보석을 정의

#집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_image, (screen_width // 2, 110)) #가로위치는 화면 가로크기 기준 절반, 로는 위에서 110px 정도




running = True 
while running:
    clock.tick(30) #FPS값이 30 으로 고정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.blit(background, (0,0))
    
    gemstone_group.draw(screen) #그룹 내 모든 스트라이프를 screen에 그림
    claw.draw(screen)


    pygame.display.update()

    
pygame.quit()


