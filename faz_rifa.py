"""
Faz rifa pro Tapira!

Modo de uso:
    $ python3 faz_rifa.py {caminho_ate_foto_da_rifa}

"""

import cv2 as cv
import sys

try:
    path = ' '.join(sys.argv).split(maxsplit=1)[1]
except IndexError:
    print("Faltou especificar a foto de origem")
    exit()

original = cv.imread(path)
name = input("Nome: ")
phone = input("Phone: ")
email = input("E-mail: ")

while True:

    number = input("Numero: ")

    pic = original.copy()
    cv.putText(pic, name, (63, 121 + 25), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
    cv.putText(pic, phone, (63, 261 + 25), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
    cv.putText(pic, email, (63, 397 + 25), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
    cv.putText(pic, number, (104, 483 + 23), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
    cv.putText(pic, number, (822, 484 + 23), cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)

    cv.imshow('window', pic)
    cv.waitKey(800)
    cv.imwrite(f'./{name}_{number}.jpeg', pic)

    answer = input("Mais rifa para a mesma pessoa? ")
    if (answer != "s") and (answer != "y"):
        break
