import re , os, codecs

os.chdir(r"/Users/gestirn7/Desktop/Jocording/python")
f = codecs.open("friends.txt", "r", encoding = "utf-8")
script101 = f.read()

# #print(script101[:100])

# #모니카 대사만 모으기
Line = re.findall(r"Monica:.+", script101)

# for item in Line:
#     print(item)

f = codecs.open("monica.txt", "w", encoding = "utf-8")

monica = ""



for i in Line:
    monica += i +"\n"
f.write(monica)
f.close()