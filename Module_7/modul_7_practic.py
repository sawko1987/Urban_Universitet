import tkinter as tk
import os
from fileinput import filename
from tkinter import filedialog
def file_select():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Выберите файл",
                                              filetypes = (("Текстовый файл",'.txt'),
                                                           ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)

window = tk.Tk()
window.title ("Проводник")
window.iconbitmap(default = "icon50.png")
window.geometry("450x350-100+100")
window.configure(bg="black")
window.resizable(False, False)  #запрещаем менять размер
text = tk.Label(window, text = "файл", height = 5, width = 65, background = "silver", )
text.grid(row = 1, column = 1)
button_select = tk.Button(window, height=3,width=20, text= "выбрать файл",command = file_select)
button_select.grid(row = 2, column = 1)

window.mainloop()


