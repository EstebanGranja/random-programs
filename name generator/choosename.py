
from tkinter import *
import random


# ROOT
root = Tk()
root.title('Elegir nombre')
root.resizable(True, True)
root.iconbitmap('garen.ico')
root.config(bg="lightblue")
root.config(bd=30) 
root.config(relief="sunken")



def random1():
    pronouns = ['El', 'La', 'Un', 'Una', 'Dr.', 'Dra.', 'Presidente', 'Jefe', 'Mister', 'Pequeño', 'Pequeña']
    choice1 = random.choice(pronouns)
    text1.set(choice1)


def random2():
    nouns = ['Gato', 'Hombre', 'Spiderman', 'Batman', 'Mujer', 'Chico', 'Niña', 'Niño', 'Gigante', 'Demoledor', 'Rockstar', 'León', 'Tractor', 'Asesino', 'Carnicero',
            'Abogado', 'Comegordas', 'Pedófilo', "Comepanes", 'Chupachichi', "Chino", 'Leñador', 'Niño', 'Superhéroe', 'Niña', 'Gordita', 'Diputada', 'Músculo',
            'Ratón', 'Gata', 'Lubricante', 'Dildo', 'Soldado', 'Militar'] 
    choice2 = random.choice(nouns)
    text2.set(choice2)

def random3():
    adjectives = ['Supremo', 'Suprema', 'Tímido', 'Glorioso', 'Nashe', 'Devora viejas', 'Obeso', 'Apuesto', 'Horrible', 'Gracioso', 'Enano', 'Enana', 'Putarraco', 'Volador',
                'Afortunado', 'Extremo', 'Soñador', 'Honesto', 'Cariñoso >.<', 'Otaku', 'Mugroso', 'Tetrapléjica', 'Marginado', 'Boliviano', 'Inglés', 'Británico',
                'Poderoso', 'Poderosa', 'Linda', 'Lindo']
    choice3 = random.choice(adjectives)
    text3.set(choice3)


def borrar1():
    text1.set('')

def borrar2():
    text2.set('')

def borrar3():
    text3.set('')

text1 = StringVar()
text1.set('----')

text2 = StringVar()
text2.set('----')

text3 = StringVar()
text3.set('----')


# FRAME
frame = Frame(root, width=100, height=100)
frame.grid(padx=70, pady=50)



# IMAGE
imagen = PhotoImage(file="quepro.gif")
Label(root, image=imagen).grid()


title = Label(frame, text='Elige tu nombre de guerrero', fg="brown", font=("Times New Roman", 16, "bold italic"))
title.grid(column=1, row=0)



# PRONOMBRES
l1 = Label(frame, textvariable=text1)
l1.grid(column=0, row=2)
Label(frame).grid(column=1, row=2)

l1button = Button(frame, text='Cambiar', command=random1, bg='lightgreen', padx=20)
l1button.grid(column=2, row=2)

Button(frame, text='X', command=borrar1, bg='red').grid(column=3, row=2)



# SUSTANTIVOS
l2 = Label(frame, textvariable=text2)
l2.grid(column=0, row=3)
Label(frame).grid(column=1, row=3)


l2button = Button(frame, text='Cambiar', command=random2, bg='orange', padx=20)
l2button.grid(column=2, row=3)

Button(frame, text='X', command=borrar2, bg='red').grid(column=3, row=3)


# ADJETIVOS
l3 = Label(frame, textvariable=text3)
l3.grid(column=0, row=4)
Label(frame).grid(column=1, row=4)

l3button = Button(frame, text='Cambiar', command=random3, bg='yellow', padx=20)
l3button.grid(column=2, row=4)

Button(frame, text='X', command=borrar3, bg='red').grid(column=3, row=4)

f = StringVar()
f.set("")

def final():
    msj = ['Buen nombre!', 'Que creativo!', ':)']
    option = random.choice(msj)
    f.set(option)


Button(frame, text='Confirmar', fg='white', command=final, bg='black').grid()

Label(frame, textvariable=f, font=('Courier', 10, 'bold')).grid()




root.mainloop()