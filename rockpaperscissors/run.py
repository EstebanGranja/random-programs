from tkinter import *
import random
from tkinter import messagebox


# --------------------- window ------------------------------------------------------------
root = Tk()
root.title('Rock Paper Scissors')
root.geometry('570x400')
root.config(bg='#FFFFF0')
root.iconbitmap("rock.ico")

frame = Frame(root, bg='#FFFFF0')
frame.grid()

rpsimage = PhotoImage(file='rps.png')
Label(frame, image=rpsimage).place(x=50, y=30)

rps2image = PhotoImage(file='rps2.png')
Label(frame, image=rps2image).place(x=480, y=30)


#------------------------------ points ----------------------------------------------------

pc_choice = ''
player_choice = ''
playerpts = 0
pcpts = 0
pcchoicemarker = ''

# ------------------------- pc choice --------------------------------------------------------

def rps_pc():
    global pc_choice
    global pcchoicemarker
    global pcpts
    global playerpts

    options = ['rock', 'paper', 'scissors']
    pc_choice = random.choice(options)

    if pcpts == 9:
        pcpts += 1
        pcscreen.set(pcpts)
        option = messagebox.askquestion('What a shame', "I'm sorry, you lost!\n\nWanna play again? :)")
        if option == "no":
            root.destroy()
        elif option == 'yes':
            pcpts = 0
            playerpts = 0
            playerscreen.set(playerpts)
            pcscreen.set(pcpts)
    else:
        if pc_choice == 'rock':
            pcchoicemarker = 'Rock ⪡'
            pcchoicescreen.set(pcchoicemarker)

        elif pc_choice == 'paper':
            pcchoicemarker = 'Paper ⪡'
            pcchoicescreen.set(pcchoicemarker)
        elif pc_choice == 'scissors':
            pcchoicemarker = 'Scissors ⪡'
            pcchoicescreen.set(pcchoicemarker)



#------------------------- player => rock ---------------------------------------------------

def rock():
    rps_pc()
    global pc_choice
    global result
    global playerpts
    global pcpts
    global player_choice
    global pcchoicemarker

    if playerpts == 9:
        playerpts +=1
        playerscreen.set(playerpts)        
        option = messagebox.askquestion('Congratulations', 'You are the champion!\n\n\nWanna play again?')
        if option == "no":
            root.destroy()
        elif option == 'yes':
            pcpts = 0
            playerpts = 0
            playerscreen.set(playerpts)
            pcscreen.set(pcpts)
    else:
        if pc_choice == 'rock':
            result.set('𝐈𝐭𝐬 𝐚 𝐝𝐫𝐚𝐰 :/') 
            player_choice = '➤ Rock'
            playerchoicescreen.set(player_choice)


        elif pc_choice == 'paper':
            result.set('𝐘𝐨𝐮 𝐥𝐨𝐬𝐭! :(')   
            pcpts += 1
            pcscreen.set(pcpts)
            player_choice = '➤ Rock'
            playerchoicescreen.set(player_choice)

        elif pc_choice == 'scissors':
            result.set('𝗬𝗼𝘂 𝘄𝗼𝗻! :)')   
            playerpts +=1
            playerscreen.set(playerpts)
            player_choice = '➤ Rock'
            playerchoicescreen.set(player_choice)
    


#------------------------- player => paper ---------------------------------------------------

def paper():
    rps_pc()
    global pc_choice
    global result
    global playerpts
    global pcpts
    global player_choice

    if playerpts == 9:
        playerpts +=1
        playerscreen.set(playerpts) 
        option = messagebox.askquestion('Congratulations', 'You are the champion!\n\n\nWanna play again?')
        if option == "no":
            root.destroy()
        elif option == 'yes':
            pcpts = 0
            playerpts = 0
            playerscreen.set(playerpts)
            pcscreen.set(pcpts)
    
    else:
        if pc_choice == 'rock':
            result.set('𝗬𝗼𝘂 𝘄𝗼𝗻! :)')    
            playerpts += 1 
            playerscreen.set(playerpts)
            player_choice = '➤ Paper'
            playerchoicescreen.set(player_choice)
            
        elif pc_choice == 'paper':
            result.set('𝐈𝐭𝐬 𝐚 𝐝𝐫𝐚𝐰 :/')   
            player_choice = '➤ Paper'
            playerchoicescreen.set(player_choice)

        elif pc_choice == 'scissors':
            result.set('𝐘𝐨𝐮 𝐥𝐨𝐬𝐭! :(')     
            pcpts += 1
            pcscreen.set(pcpts)
            player_choice = '➤ Paper'
            playerchoicescreen.set(player_choice)
    
#------------------------- player => scissors ---------------------------------------------------

def scissors():
    rps_pc()
    global pc_choice
    global result
    global playerpts
    global pcpts
    global player_choice

    if playerpts == 9:
        playerpts +=1
        playerscreen.set(playerpts) 
        option = messagebox.askquestion('Congratulations', 'You are the champion!\n\n\nWanna play again?')
        if option == "no":
            root.destroy()
        elif option == 'yes':
            pcpts = 0
            playerpts = 0
            playerscreen.set(playerpts)
            pcscreen.set(pcpts)

    else:
        if pc_choice == 'rock':
            result.set('𝐘𝐨𝐮 𝐥𝐨𝐬𝐭! :(')    
            pcpts += 1
            pcscreen.set(pcpts)
            player_choice = '➤ Scissors'
            playerchoicescreen.set(player_choice)

        elif pc_choice == 'paper':
            result.set('𝗬𝗼𝘂 𝘄𝗼𝗻! :)')   
            playerpts += 1 
            playerscreen.set(playerpts)
            player_choice = '➤ Scissors'
            playerchoicescreen.set(player_choice)

        elif pc_choice == 'scissors':
            result.set('𝐈𝐭𝐬 𝐚 𝐝𝐫𝐚𝐰 :/')    
            player_choice = '➤ Scissors'
            playerchoicescreen.set(player_choice)



# -------------------- title -----------------------------------------------------------------


title = Label(frame, text="𝙇𝙚𝙩'𝙨 𝙥𝙡𝙖𝙮 𝙍𝙤𝙘𝙠, 𝙋𝙖𝙥𝙚𝙧, 𝙎𝙘𝙞𝙨𝙨𝙤𝙧𝙨 !", bg='#FFFFF0', font=(26))
title.grid(padx=80, pady=8, columnspan=20)


# -------------------player name -------------------------------------------------------------------

def play(n):
    a = StringVar()
    a.set(n)
    Label(frame, textvariable=a, font=('Times New Roman', 20), bg='#FFFFF0').grid(row=4, column=1, padx=10, pady=10)
    

# name label
name = Label(frame, text='Name: ', bg='#FFFFF0')
name.grid(row=1, column=2)

# boxtext name
boxname = Entry(frame, bg="#FFEFD5")
boxname.grid(row=1, column=3)

nombre = boxname.get()
n = StringVar()
n.set(nombre)


# play button
confirm = Button(frame, text='Play', command=lambda:play(boxname.get()), width=5, bg="#FFEFD5")
confirm.grid(row=1, column=4, pady=10, padx=10)



Label(frame, text='▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', bg='#FFFFF0', fg='#BC8F8F').grid(row=3, column=0, columnspan=100)



#-------------------------- player options ---------------------------------------------------


rockimage = PhotoImage(file='rock.png')
rockbutton = Button(frame, image=rockimage, bg='#FFFFF0', command=rock)
rockbutton.grid(row=5, column=1, pady=15)

paperimage = PhotoImage(file='paper.png')
paperbutton = Button(frame, image=paperimage, bg='#FFFFF0', command=paper)
paperbutton.grid(row=7,column=1, padx=20, pady=20)

scissorsimage = PhotoImage(file='scissors.png')
scissorsbutton = Button(frame, image=scissorsimage, bg='#FFFFF0', command=scissors)
scissorsbutton.grid(row=7,column=2, padx=5, pady=5)



#-------------------------- pc options ---------------------------------------------------

pc = Label(frame, text='PC', bg='#FFFFF0', font=('Times New Roman', 20))
pc.grid(row=4, column=10, padx=10, pady=10)

rockpcimage = PhotoImage(file='rock.png')
rockpc = Button(frame, image=rockpcimage, bg='#FFFFF0', state=DISABLED)
rockpc.grid(row=5, column=10, pady=15)

paperpcimage = PhotoImage(file='paper.png')
paperpc = Button(frame, image=paperimage, bg='#FFFFF0', state=DISABLED)
paperpc.grid(row=7,column=10, padx=20, pady=20)

scissorspcimage = PhotoImage(file='scissors.png')
scissorspc = Button(frame, image=scissorsimage, state=DISABLED, bg='#FFFFF0')
scissorspc.grid(row=7,column=6, padx=5, pady=5)


# ----------------------------- marker --------------------------------------------------

# result
result = StringVar()
result.set('Good luck!')
msj = Label(frame, textvariable=result, bg='#FFFFF0', font=('bold', 14))
msj.place(x=230, y=130)

# msj
ten = Label(frame, text='| 10 points to win |', bg='#FFFFF0')
ten.place(x=225, y=170)


# player points
playerscreen = StringVar()
playerscreen.set(playerpts)
Label(frame, textvariable=playerscreen, bg='#FFFFF0', font=('Times New Roman',24)).place(x=140, y=210)


# pc points
pcscreen = StringVar()
pcscreen.set(pcpts)
Label(frame, textvariable=pcscreen, bg='#FFFFF0', font=('Times New Roman',24)).place(x=410, y=210)


# player choice
playerchoicescreen = StringVar()
playerchoicescreen.set(player_choice)
Label(frame, textvariable=playerchoicescreen, bg="#FFFFF0", font=('Times New Roman',20)).place(x=200, y=210)


# pc choice
pcchoicescreen = StringVar()
pcchoicescreen.set(pcchoicemarker)
Label(frame, textvariable=pcchoicescreen, bg="#FFFFF0", font=('Times New Roman',20)).place(x=260, y=300)


def close():
    root.quit()


# exit
exit = Button(frame, text='Exit', command=close, width=4, bg='#FFEFD5')
exit.place(x=260, y=350)


root.mainloop()

