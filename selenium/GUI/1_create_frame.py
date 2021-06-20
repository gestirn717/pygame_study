from tkinter import *

root = Tk()
root.title("Mergi GUI") #제목
# root.geometry("640x480") #크기 지정
root.geometry("640x480+100+300") #가로*세로 + x좌표 + y좌표, 창이뜨는 위치 조정

root.resizable(False,False) #  x너비 y높이 값 변경 불가 ( 창 크기 변경 불가)

root.mainloop()