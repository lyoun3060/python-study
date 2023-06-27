from tkinter import *
from tkinter import messagebox

def  myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")
window = Tk()
window.title("윈도창 연습")
window.geometry("500x400")
window.resizable(width=True, height=True)

label1 = Label(window, text ="COOKBOOK, 데이터 분석을")
label2 = Label(window, text ="열심히", font = ("궁서체", 30), fg="blue")
label3 = Label(window, text ="공부중 입니다.", bg="magenta", width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

photo = PhotoImage(file="gif/rat.jpg")
labelImg.Label(window, image=photo)
window.mainloop()