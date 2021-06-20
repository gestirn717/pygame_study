from tkinter import *

root = Tk()
root.title("Mergi GUI") 
root.geometry("640x480")

#pack 한번에 쓰기, 레이블을 바꿔주려면 변수 따로 지정해줘야뎀 
Label(root, text="메뉴를 선택하세요").pack() 

#radiobutton은 여러개 항목중 하나만 선택할때 / 항목이 그룹으로 묶여있어야됨 / 하나의 var를 공유
burger_var = IntVar() #여기에 int형으로 값을 저장한다 
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() #미리 선택되도록 
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라",value="콜라", variable=drink_var)
btn_drink1.select() #미리 선택되도록 
btn_drink2= Radiobutton(root, text="콜라",value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) #햄버거 중 선택된 라디오 항목의 값(value)
    print(drink_var.get()) #음료 중 선택된 값 출력 
   

btn = Button(root, text="주문", command = btncmd)
btn.pack()


root.mainloop()