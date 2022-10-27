from tkinter import *


root = Tk()
root.geometry('190x230')

frame = Frame(root)
frame.pack()

operacion = ''
resultado = 0
reset_screen = False
#---------------------------- PANTALLA -------------------------------------
numscreen = StringVar()


screen = Entry(frame, bg='black', fg='lightgreen', justify='right', textvariable=numscreen)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

def pressed_button(num):
    global operacion
    global reset_screen

    if reset_screen != False:
        numscreen.set(num)
        reset_screen = False
    else:
        numscreen.set(numscreen.get() + num) 

#----------------------------- BORRAR -----------------------------------------------
def clear():
    global operacion
    global resultado
    numscreen.set('')
    operacion = 'clear'
    resultado = 0
    
#----------------------------- SUMA ---------------------------------------

def suma(num):
    global resultado
    global operacion
    global reset_screen
    operacion = 'suma'
    resultado += int(num)
    reset_screen = True
    numscreen.set(resultado)



#----------------------------- RESTA ---------------------------------------
num1 = 0
restcontador = 0

def resta(num):
    global resultado
    global operacion
    global num1
    global restcontador
    global reset_screen
    
    if restcontador == 0:
        num1 = int(num)
        resultado = num1
    else:
        if restcontador == 1:
            resultado = num1 = int(num)
        else:
            resultado = int(resultado) - int(num)

        numscreen.set(resultado)
        resultado = numscreen.get()

    restcontador = restcontador + 1
    operacion = 'resta'
    reset_screen = True
        

#---------------------------- MULTIPLICACION ----------------------------
multcontador = 0

def mult(num):
    global operacion
    global resultado
    global num1
    global multcontador
    global reset_screen

    if multcontador == 0:
        num1 = int(num)
        resultado = num1

    else:
        if multcontador == 1:
            resultado = num1*int(num)
        else:
            resultado = int(resultado) * int(num)
        
        numscreen.set(resultado)
        resultado = numscreen.get()

    multcontador = multcontador + 1
    operacion = 'multiplicacion'
    reset_screen = True


#--------------------------- DIVISION-------------------------------------
divcontador = 0

def div(num):
	global operacion
	global resultado
	global num1
	global divcontador
	global reset_screen
	
	if divcontador==0:
		num1=float(num)
		resultado=num1
        
	else:
		if divcontador==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)	

		numscreen.set(resultado)
		resultado=numscreen.get()

	divcontador=divcontador+1

	operacion="division"
	reset_screen=True
#----------------------------IGUAL----------------------------------------

def igual():
    global resultado
    global operacion
    global restcontador
    global multcontador
    global divcontador

    if operacion == 'suma':
        numscreen.set(int(resultado) + int(numscreen.get()))
        resultado = 0

    elif operacion == 'resta':
        numscreen.set(int(resultado) - int(numscreen.get()))
        resultado = 0
        restcontador = 0

    elif operacion == 'multiplicacion':
        numscreen.set(int(resultado) * int(numscreen.get()))
        resultado = 0
        multcontador = 0

    elif operacion == 'division':
        numscreen.set(int(resultado / int(numscreen.get())))
        resultado = 0
        divcontador = 0
        
    
 
#---------------------------- fila 1 -------------------------------------

cbutton = Button(frame, text='C', padx=6, width=3, bg='#B0E0E6', command=clear)
cbutton.grid(row=2, column=1)

Label(frame, text='𝓒𝓪𝓵𝓬𝓾𝓵𝓪𝓽𝓸𝓻', padx=3).grid(row=2, column=3, columnspan=2)
#---------------------------- fila 2 -------------------------------------

but7 = Button(frame, text='7', width=4, command=lambda:pressed_button('7'), bg='#F5FFFA')
but7.grid(row=3, column=1, padx=1, pady=3)
but8 = Button(frame, text='8', width=4, command=lambda:pressed_button('8'), bg='#F5FFFA')
but8.grid(row=3, column=2, padx=1, pady=3)
but9 = Button(frame, text='9', width=4, command=lambda:pressed_button('9'), bg='#F5FFFA')
but9.grid(row=3, column=3, padx=1, pady=3)
butdiv = Button(frame, text='/', width=3, command=lambda:div(numscreen.get()), bg='#E6E6FA')
butdiv.grid(row=3, column=4, padx=5, pady=3)



#---------------------------- fila 3 -------------------------------------

but4 = Button(frame, text='4', width=4, command=lambda:pressed_button('4'), bg='#F5FFFA')
but4.grid(row=4, column=1, padx=1, pady=3)
but5 = Button(frame, text='5', width=4, command=lambda:pressed_button('5'), bg='#F5FFFA')
but5.grid(row=4, column=2, padx=1, pady=3)
but6 = Button(frame, text='6', width=4, command=lambda:pressed_button('6'), bg='#F5FFFA')
but6.grid(row=4, column=3, padx=1, pady=3)
butmult = Button(frame, text='X', width=3, command=lambda:mult(numscreen.get()), bg='#E6E6FA')
butmult.grid(row=4, column=4, padx=5, pady=3)



#---------------------------- fila 4 -------------------------------------

but1 = Button(frame, text='1', width=4, command=lambda:pressed_button('1'), bg='#F5FFFA')
but1.grid(row=5, column=1, padx=1, pady=3)
but2 = Button(frame, text='2', width=4, command=lambda:pressed_button('2'), bg='#F5FFFA')
but2.grid(row=5, column=2, padx=1, pady=3)
but3 = Button(frame, text='3', width=4, command=lambda:pressed_button('3'), bg='#F5FFFA')
but3.grid(row=5, column=3, padx=1, pady=3)
butrest = Button(frame, text='-', width=3, command=lambda:resta(numscreen.get()), bg='#E6E6FA')
butrest.grid(row=5, column=4, padx=5, pady=3)


#---------------------------- fila 4 -------------------------------------

butcoma = Button(frame, text='.', width=4, command=lambda:pressed_button('.'), bg='#FFF5EE')
butcoma.grid(row=6, column=1, padx=1, pady=3)
but0 = Button(frame, text='0', width=4, command=lambda:pressed_button('0'), bg='#F5FFFA')
but0.grid(row=6, column=2, padx=1, pady=3)
butigual = Button(frame, text='=', width=4, command=lambda:igual(), bg='#FFF5EE')
butigual.grid(row=6, column=3, padx=1, pady=3)
butsuma = Button(frame, text='+', width=3, command=lambda: suma(numscreen.get()), bg='#E6E6FA')
butsuma.grid(row=6, column=4, padx=5, pady=3)



Label(frame, text='------------------------', fg='#FFE4B5').grid(row=7, column=0, columnspan=4, pady=5)
exit = Button(frame, text='Exit', command=root.quit, bg='#FFB6C1', width=5)
exit.grid(row=7, column=3, columnspan=2, pady=5, sticky='e')







root.mainloop()