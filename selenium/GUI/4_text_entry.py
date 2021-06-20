from tkinter import *

root = Tk()
root.title("Mergi GUI") 
root.geometry("640x480")

#여러줄의 텍스트
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")



#로그인 아이디 등등 한줄로 넣을때
e = Entry(root, width=30)
e.pack()
e.insert(0,"한 줄만 입력해요")
#비어있으면 0대신 END 넣어도 됨 



#버튼을 통해 값을 가져오는 방법
#txt에서 가져오기 
# get("1.0",END)는 처음부터 끝까지 가져올때 (1: 첫번째라인, 0 : 0번째 column위치 )


def btncmd():
    #내용출력
    print(txt.get("1.0",END)) 
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text="클릭", command = btncmd)
btn.pack()


root.mainloop()