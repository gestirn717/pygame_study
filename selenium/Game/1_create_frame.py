import pygame 

pygame.init() #초기화 / 반드시 필요

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height)) #화면 크기 설정

#화면 타이틀 설정
pygame.display.set_caption("Mergi Game") #게임 이름

#이벤트 루프가 실해되어있어야 창이 꺼지지 않음
#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #pygame에서 무조건 필요함 사용자가 동작하는지 확인
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가
            running = False #게임이 진행중이 아님

#pygame 종료
pygame.quit()

