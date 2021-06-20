from random import *


lst = list(range(1,21))
shuffle(lst)

print("-- 당첨자 발표 --")
print("치킨당첨자 : ",sample(lst,1))
print("커피당첨자 : ",sample(lst,3))
print("--축하합니다--") 


# suffle 쓰려면 list형으로 




users = list(range(1,21))
shuffle(users)

winners = sample(users,4)

print("-- 당첨자 발표 -- ")
print("치킨당첨자 : {0}".format(winners[0]))  
print("커피당첨자 : {0}".format(winners[1:]))
print(" --축하합니다-- ") 