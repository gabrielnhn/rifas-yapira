#!/usr/bin/env python3
"""
Faz rifa pro Tapira!

Pré-requisitos: instale os modulos 'tkinter' e 'cv2':
    $ pip install tk
    $ pip install opencv-python

Modo de uso:
    $ python3 faz_rifa.py
"""

__author__ = "Gabriel Hishida and Allan Cedric"

import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])     


try:
    import cv2
except ImportError:
    pip.main(['install', "opencv-python"])
    import cv2     


import_or_install("tkinter")


import sys
import tkinter.filedialog
import tkinter.simpledialog
import os

class MyDialog(tkinter.simpledialog.Dialog):
    """ Multiple entries dialog, for name, phone, e-mail and more"""

    values = None

    def body(self, master):

        tkinter.simpledialog.Label(master, text="Nome:").grid(row=0)
        tkinter.simpledialog.Label(master, text="E-mail:").grid(row=1)
        tkinter.simpledialog.Label(master, text="Telefone:").grid(row=2)
        tkinter.simpledialog.Label(master, text="Numero(s):").grid(row=3)

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
        email = self.e2.get()
        phone = self.e3.get()
        number = self.e4.get()
        self.values = (name, email, phone, number)

if __name__ == "__main__":

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

    
    program_dir = os.path.dirname(os.path.realpath(__file__))
    currdir = os.getcwd()

    path = program_dir+"/rifa.png"
    if not os.path.isfile(path):
        path = tkinter.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Selecione o template da rifa')

    if not path:
        exit() 

    original = cv2.imread(path)

    while True:
        # Get info:
        popup = MyDialog(root)
        name, email, phone, number = popup.values

        if not name:
            # no data was given
            break

        # Print info to image

        pic = original.copy()
        height, width, _ = pic.shape

        # high resolution

        cv2.putText(pic, name, (63, 110), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv2.putText(pic, email, (63, 230), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv2.putText(pic, phone, (63, 335), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
        cv2.putText(pic, number, (130, 490), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(0,0,0), thickness=2)
        cv2.putText(pic, number, (900, 490), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(0,0,0), thickness=2)

        cv2.imshow('Rifa', pic)
        cv2.waitKey(800)

        # Save image

        path = tkinter.filedialog.asksaveasfilename(parent=root, initialdir=currdir, title='Salvo a nova rifa aonde?', initialfile=f"{name}-{number}.png")
        if not path:
            exit()
        cv2.imwrite(path, pic)

        # Ask whether there are more numbers
        # number = tkinter.simpledialog.askstring(title="Rifa", prompt="Mais um numero?: ")
        # if not number:
        #     break
