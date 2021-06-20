import re , os

os.chdir(r"/Users/gestirn7/Desktop/Jocording/python")
f = open("friends.txt", "r")
sentence = f.readlines()



line = [ i for i in sentence if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
for i in line:
    print(i)