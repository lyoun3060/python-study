from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *

# def func_open():
#     messagebox.showinfo("메뉴선택", "열기 메뉴 선택함")

# def func_sxit():
#     window.quit()
#     window.destroy()

window = Tk()
window.geometry("400x500")

# mainMenu = Menu(window) #상위메뉴
# window.config(menu = mainMenu)

# fileMenu = Menu(mainMenu) #하위메뉴
# mainMenu.add_cascade(label = "파일", menu = fileMenu)
# fileMenu.add_command(label="열기", command=func_open)
# fileMenu.add_separator()
# fileMenu.add_command(label="종료", command=func_sxit)

label1 = Label(window, text="입력된 값")
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)

label1.configure(text=str(value))

window.mainloop()