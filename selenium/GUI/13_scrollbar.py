from tkinter import *

root = Tk()
root.title("Mergi GUI") 
root.geometry("640x480")

frame = Frame(root)
frame.pack()

#스크롤바 넣기
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right")

#set이 없으면 스크롤을 내려도 다시 올라옴 
listbox = Listbox(frame, selectmode="extanded", height=5, yscrollcommand = scrollbar.set)
for i in range(1,32): # 1 ~ 31일 
    listbox.insert(END,str(i) + "일") #1일, 2일 ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()