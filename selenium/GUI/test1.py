from tkinter import *
import tkinter.ttk as ttk
import os

root = Tk()
root.title("제목없음 - apple 메모장")
root.geometry("640x480")

filename = "mynote.txt"

#파일이 있는지 없는지 확인 
def open_file():
    if os.path.isfile(filename): #파일 있으면 True, 없으면 false
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0", END) #텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) #파일 내용을 본문에 입력


def save_file():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0", END)) #모든 내용 가져와서 저장 



menu = Menu(root)

#파일 메뉴
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

#편집메뉴
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집",menu=menu_edit)

#서직메뉴
menu_start = Menu(menu, tearoff=0)
menu.add_cascade(label="서식",menu=menu_edit)

#보기메뉴
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기",menu=menu_edit)

#도움말메뉴
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말",menu=menu_edit)


#스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")




#본문영역
#expand 요구되지 않은 공간을 모두 요구할때 True
#fill 현재 공간을 늘리고자할때 수직 수평 both
#스크롤바 연동해줄 곳에 넣어줘
#config 는 연동 처리 
txt = Text(root,yscrollcommand = scrollbar.set)
txt.pack(side="left",fill="both", expand=True) 

scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()
