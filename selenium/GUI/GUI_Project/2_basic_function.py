import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Mergi GUI") 

#파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
        filetypes=(("PNG파일", "*.png"),("모든파일","*.*")), \
            initialdir=r"Documents/") #최초에 사용자가 지정한 경로를 보여줌

    #사용자가 선택한 파일 목록 리스트에 추가       
    for file in files:
        list_file.insert(END, file)


#파일 삭제
def del_file():
    #파일을 삭제 처리할때는 맨 뒤에서부터 삭제하는것이 좋음
    #인덱스를 뒤에서부터 받아야함, reversed 사용 
    #revers 는 값을 바꿈
    #reversed는 값을 바꾸지 않고 새로운 값을 넘겨줌
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#저장 경로 (파일)
def browse_dest_path():
    #폴더 선택하는 창이 뜸 
    folder_selected = filedialog.askdirectory()
    if folder_selected == None:  #사용자가 취소를 누를때
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)
   
#시작
def start():
    #각 옵션들 깂을 확인   
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    #파일 목록 확인 / 선택된 파일 없으면 경고창 뜸 
    if list_file.size() == 0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return #아래쪽으로 빠져나가지 않게 하기 위함 
    
    #저장 경로 확인 / 저장경로 지정 안하면 경고창 뜸 
    #get으로 값을 가져와서 문자열의 길이가 0이면 경고창 
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고","저장 경로를 확인 하세요")
        return


#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) #간격 띄우기

btn_add_file = Button(file_frame,padx=5,pady=5,width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5,pady=5,width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extanded", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #ipad : 안쪽 패딩, 높이변경

btn_dest_path = Button(path_frame, text="찾아보기", padx=5, pady=5, width=10, command=browse_dest_path)
btn_dest_path.pack(side="right")

#옵션 프레임 
frame_option = LabelFrame(root, text="옵션")
frame_option.pack( padx=5, pady=5, ipady=5)


#1. 가로 넓이 옵션

#가로 넓이 선택 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

#가로 넓이 선택 콤보박스
opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)



#2. 간격옵션
#간격 옵션 선택 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)


#간격 옵션 선택 콤보박스
opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)


#3. 파일 포맷 옵션
#파일 포맷옵션 레이블
lbl_format = Label(frame_option, text="포멧", width=8)
lbl_format.pack(side="left", padx=5, pady=5)


#파일 포맷 옵션 콤보
opt_format = ["PNG","JPG","BMP",]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


#진행 상황 Progress Bar
#레이블 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

#진행상황
p_var = DoubleVar
progress_bar =ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)




root.resizable(False,False) 
root.mainloop()