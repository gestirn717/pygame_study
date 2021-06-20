from random import *

cnt = 0 #총 탑승 승객 수
for i in range(1,51):      #1~50 승객 수
    time = randrange(5,51) #5~50 소요시간
    if 5 <= time <= 15:    #5~15 분 사이의 손님, 탑승객 수 증가
        print("[0] {0}번째 손님 (소요시간 : {1}분) ".format(i, time))
        cnt += 1 
    else: #매칭 실패
        print( "[] {0}번째손님 (소요시간 : {1}분) ".format(i, time))

print( "총 탑승 승객수 : {0}명".format(cnt))