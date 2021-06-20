gun = 10

def checkpoint(gun, soldier):
    gun = gun - soldier
    print("[함수 내] 남은 총 : {0} " .format(gun))
    return gun

print("전체 총 : {0}". format(gun))
gun = checkpoint(gun, 2)                   #함수에서 계산되고 반환되는 값 저장                
print("남은 총 : {0}". format(gun))