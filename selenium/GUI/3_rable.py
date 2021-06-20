from tkinter import *

root = Tk()
root.title("Mergi GUI") #제목
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="/Users/gestirn7/Desktop/Jocording/python/selenium/GUI/img.png") #이미지로 라벨 
label2 = Label(root, image=photo)
label2.pack()


#눌렀을때 라벨 바뀜 
def change():
    label1.config(text="또 만나요")
      
      #함수 내에서 레이블의 이미지 값 등을 바꾸기 위해서는 photo값을 전역변수 (global)로 설정해야함
    global photo2 
    photo2 = PhotoImage(file="/Users/gestirn7/Desktop/Jocording/python/selenium/GUI/img2.png")
    label2.config(image = photo2)

btn = Button(root, text="클릭", command=change) 
btn.pack()

root.mainloop()