import csv, os
os.chdir(r"/Users/gestirn7/Desktop/Jocording/python/selenium/Lifecoding")
f = open("popSeoul.csv", "r", encoding = "utf-8")
new = csv.reader(f)

a=[]
for i in new:
    print(i)
    a.append(i)
print(a)