import pygame
from pygame.constants import K_RIGHT 

pygame.init() #초기화 / 반드시 필요

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height)) #화면 크기 설정

#화면 타이틀 설정
pygame.display.set_caption("Mergi Game") #게임 이름

#fps
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/bg.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/char.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = screen_width / 2 - character_width / 2 #화면 가로크기의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치


#이동할 좌표
to_x = 0 
to_y = 0

#이동속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = screen_width / 2 - enemy_width / 2 #화면 가로크기의 절반에 해당하는 곳에 위치
enemy_y_pos = screen_height / 2 - enemy_height / 2 #화면 세로 크기 가장 아래에 해당하는 곳에 위치


#폰트정의
game_font = pygame.font.Font(None,40) #폰트객체 생성 ( 폰트, 크기)

#총시간
total_time = 10

#시작시간
start_ticks = pygame.time.get_ticks() #현재 tick을 받아옴

#이벤트 루프가 실해되어있어야 창이 꺼지지 않음
#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정




    for event in pygame.event.get(): #pygame에서 무조건 필요함 사용자가 동작하는지 확인
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False #게임이 진행중이 아님
    
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
               to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
               to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 뗌
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리

    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height



    #충돌 처리를 위한 rect정보 업데이트
    #캐릭터 고유 위치는 변하지 않으므로 충돌처리시에 바꿔줘야함 
    # left와 top만 바꾸면 됨
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    #충돌 체크
    if character_rect.colliderect(enemy_rect):
       print("충돌했어요")
       running = False







    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos )) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos )) #적그리기

    #타이머 집어 넣기
    #경과 시간 계산
    #경과시간(ms)을 1000으로 나누어서 초 단위로 표시
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 

    #정수로 표현 위해 int / 문자열 처리
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    #render( 출력할 글자, True, 글자색상 )
    screen.blit(timer, (10,10))

    #만약 시간이 0이하 이면 게임 종료
    if total_time - elapsed_time <=0:
        print("타임아웃")
        running = False


    pygame.display.update() #for문을 계속해서 돌면서 화면을 게속 그려줌 반드시 해줘야 배경이 나타남 

#종료 직전 잠시 대기
pygame.time.delay(2000) #2초정도 대기 (ms)

#pygame 종료
pygame.quit()

