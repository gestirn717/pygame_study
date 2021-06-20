import pygame
import random
######################################################
#기본 초기화 부분 (반드시 필요)
pygame.init()

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height)) #화면 크기 설정

#화면 타이틀 설정
pygame.display.set_caption("ddong")

#fps
clock = pygame.time.Clock()

######################################################

#1. 사용자 게임 초기화 ( 배경화면 , 게임이미지, 좌표, 폰트, 속도 등)
background = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/bg.png")


#캐릭터 만들기
character = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/char1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동 위치
to_x = 0
character_speed = 10

#똥만들기
ddong = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10




running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) 


#2. 이벤트 처리 (키보드 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


#3.  게임 캐릭터 위치 정의    
   
    character_x_pos += to_x
    
    



    #경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    #똥 리스폰 
    if ddong_y_pos > screen_height: #똥이 바닥에 떨어짐
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)



#4. 충돌 처리
   
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos 

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False


#5 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    

    pygame.display.update()  


#pygame 종료
pygame.quit()

