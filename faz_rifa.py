"""
Faz rifa pro Tapira!

Modo de uso:
    $ python3 faz_rifa.py {caminho_ate_foto_da_rifa}

"""

import cv2 as cv
import sys
import tkinter
import tkinter.filedialog
import tkinter.simpledialog
import os

# TKINTER STUFF:

root = tkinter.Tk()
root.eval('tk::PlaceWindow . center')
root.withdraw() #use to hide tkinter window

# HIDING HIDDEN DIRECTORIES:
try:
    try:
        root.tk.call('tk_getOpenFile', '-foobarbaz')
    except tkinter.TclError:
        pass
    # now set the magic variables accordingly
    root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
    root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
except:
    pass


class MyDialog(tkinter.simpledialog.Dialog):
    values = None

    def body(self, master):

        tkinter.simpledialog.Label(master, text="Nome:").grid(row=0)
        tkinter.simpledialog.Label(master, text="Telefone:").grid(row=1)
        tkinter.simpledialog.Label(master, text="E-mail:").grid(row=2)
        tkinter.simpledialog.Label(master, text="Numero:").grid(row=3)

        self.e1 = tkinter.simpledialog.Entry(master)
        self.e2 = tkinter.simpledialog.Entry(master)
        self.e3 = tkinter.simpledialog.Entry(master)
        self.e4 = tkinter.simpledialog.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        return self.e1 # initial focus

    def apply(self):
        name = self.e1.get()
        phone = self.e2.get()
        email = self.e3.get()
        number = self.e4.get()
        self.values = (name, phone, email, number)


currdir = os.getcwd()
try:
    path = ' '.join(sys.argv).split(maxsplit=1)[1]
except IndexError:
    path = tkinter.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Selecione foto da rifa original')

if not path:
    exit() 

original = cv.imread(path)

popup = MyDialog(root)
name, phone, email, number = popup.values

while True:


    pic = original.copy()
    height, width, _ = pic.shape

    if height < 500:
        # low resolution

        cv.putText(pic, name, (50, 110), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, phone, (50, 210), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, email, (50, 310), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, number, (100, 365), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, number, (620, 365), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)

    else:
        # high resolution

        cv.putText(pic, name, (63, 121 + 25), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, phone, (63, 261 + 25), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, email, (63, 397 + 25), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, number, (104, 483 + 23), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv.putText(pic, number, (822, 484 + 23), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)

    cv.imshow('window', pic)
    cv.waitKey(800)
    path = tkinter.filedialog.asksaveasfilename(parent=root, initialdir=currdir, title='Salvo a nova rifa onde?', initialfile=f"{name}-{number}.png")
    if not path:
        exit()
    cv.imwrite(path, pic)

    number = tkinter.simpledialog.askstring(title="Rifa", prompt="Mais um numero?: ")
    if not number:
        break
