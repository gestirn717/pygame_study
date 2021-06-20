import pygame 

pygame.init() #초기화 / 반드시 필요

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height)) #화면 크기 설정

#화면 타이틀 설정
pygame.display.set_caption("Mergi Game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("/Users/gestirn7/Desktop/Jocording/python/selenium/Game/project1/images/bg.png")




#이벤트 루프가 실해되어있어야 창이 꺼지지 않음
#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #pygame에서 무조건 필요함 사용자가 동작하는지 확인
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False #게임이 진행중이 아님
    
    screen.blit(background, (0,0)) #배경 그리기

    pygame.display.update() #for문을 계속해서 돌면서 화면을 게속 그려줌 반드시 해줘야 배경이 나타남 



#pygame 종료
pygame.quit()

