

from typing import MutableMapping


gender = input("당신의 성별은?")
height = int(input("당신의 키는?"))


def std_weight():
    if gender == "남자":
       weight = round((height/100)*(height/100)*22,2)
       print("키 {0} 남자의 표준 체중은 {1}kg 입니다.".format(height,weight))
    else:
       weight = round((height/100)*(height/100)*21,2)
       print("키 {0} 여자의 표준 체중은 {1}kg 입니다.".format(height,weight))


std_weight()