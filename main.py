from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.title('Tic Tac Toe')
window.geometry('12000x7100')

clicked = True
count = 0

#exit
def exit():
    time.sleep(1)
    
    #New game or exit
    answer = messagebox.askyesno("New game", "Do you want to start a new game?")
    
    if answer:
        #new game starts
        print("New game starting...")
        reset_game()
    else:
        window.destroy()

# Reset the game
def reset_game():
    global clicked, count

    # Reset all buttons to their initial state
    for btn in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
        btn["text"] = " "
        btn["bg"] = "#ebdccb"

    clicked = True
    count = 0

#if someone wins
def win():
    global winner
    winner = False

    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="#ff0000")
        button2.config(bg="#ff0000")
        button3.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button6.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="#ff0000")
        button8.config(bg="#ff0000")
        button9.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="#ff0000")
        button4.config(bg="#ff0000")
        button7.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button8.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="#ff0000")
        button6.config(bg="#ff0000")
        button9.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button9.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button7.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        exit()
    else:
        winner = False

def win1():
    global winner
    winner = False

    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        print("X 1 wins!")
        button1.config(bg="#ff0000")
        button2.config(bg="#ff0000")
        button3.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        print("O wins!")
        exit()
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button6.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="#ff0000")
        button8.config(bg="#ff0000")
        button9.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="#ff0000")
        button4.config(bg="#ff0000")
        button7.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button8.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg="#ff0000")
        button6.config(bg="#ff0000")
        button9.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button9.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="#ff0000")
        button5.config(bg="#ff0000")
        button7.config(bg="#ff0000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        exit()
    else:
        winner = False


#click function
def btnClick(buttons):
    global clicked, count
    
    if buttons["text"] == " " and clicked == True:
        buttons["text"] = "X"
        clicked = False
        count += 1
        
    elif buttons["text"] == " " and clicked == False:
        buttons["text"] = "O"
        clicked = True
        count += 1
        
    else:
        messagebox.showerror("Tic Tac Toe", "Button already clicked!")

    win()
    win1()

    '''
    if buttons["text"] == " " and clicked == True:
        buttons["text"] = "X"
        clicked = False
        count += 1

    elif buttons["text"] == " " and clicked == False:
        buttons["text"] = "O"
        clicked = True
        count += 1

    else:
        messagebox.showerror("Tic Tac Toe", "Button already clicked!")
    if b["text"] == " " and clicked == True:
        buttons["text"] = "X"
        clicked = False
        count += 1
        '''


#buttons
button1 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button1))
button2 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button2))
button3 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button3))

button4 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button4))
button5 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button5))
button6 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button6))

button7 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button7))
button8 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button8))
button9 = Button(window, text=' ', font=("Roboto", 20), height=4, width=8, bg="#ebdccb", command=lambda: btnClick(button9))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

#exit button
exit_button = Button(window, text="Exit", command=exit)
exit_button.grid()

window.mainloop()