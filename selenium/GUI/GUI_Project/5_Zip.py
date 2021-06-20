kor = ["사과", "바나나","오렌지"]
eng = ["apple", "banana", "orange"]

#합치기
print(list(zip(kor,eng)))


mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

#분리
print(list(zip(*mixed)))