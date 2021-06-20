from tkinter import *

root = Tk()
root.title("Mergi GUI") #제목

btn1 = Button(root, text="버튼1")
btn1.pack() #버튼 활성화, 프로그램에 포함시키기

btn2 = Button(root, padx=5, pady=10, text="버튼2") #여백 
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button (root, width=10, height=3, text="버튼4")   #고정크기
btn4.pack()

btn5 = Button(root, fg="red", bg="blue", text="버튼5")
btn5.pack()

#이미지를 버튼으로 만들기
photo = PhotoImage(file="/Users/gestirn7/Desktop/Jocording/python/selenium/GUI/img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()