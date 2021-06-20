import re , os, codecs

os.chdir(r"/Users/gestirn7/Desktop/Jocording/python")
f = codecs.open("friends.txt", "r", encoding = "utf-8")
script101 = f.read()

#패턴만들기
char = re.compile(r'[A-Z][a-z]+:')

#set으로 감싸서 중복 제거
y = set(re.findall(char, script101))

#끝에 : 지우기 작업
z = list(y)
character = []
for i in z:
    character +=[i[:-1]]

#character = [i[:-1] for i in list(set(re.findall(char, script101)))]



print(character)