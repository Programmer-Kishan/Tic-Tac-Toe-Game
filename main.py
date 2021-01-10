from tkinter import *

FONT_NAME = "Courier"
MARK = "X"
player = 0

# -------------------------- MARK Management ----------------------


def change_button(button):
    button.config(text=MARK, state="disable")
    change_mark()
    if check_win("X") or check_win("O"):
        for button in button_list:
            if button['state'] != "disable":
                button.config(state="disable")
    elif draw():
        turn_label.config(text="It's Draw")
    else:
        change_player()


def change_mark():
    global MARK
    if MARK == "X":
        MARK = "O"
    else:
        MARK = "X"


def draw():
    for button in button_list:
        if button['text'] == "":
            return False
    return True


def change_player():
    global player
    if player == 0:
        turn_label.config(text="Player 1 Turn")
        player = 1
    else:
        turn_label.config(text="Player 2 Turn")
        player = 0


def win_writer(mark):
    if mark == "X":
        turn_label.config(text="Player 1 Wins")
    elif mark == "O":
        turn_label.config(text="Player 2 Wins")


# -------------------------- Check System -------------------------------


def check_win(m):
    for i in range(0, 7, 3):
        if button_list[i]["text"] == button_list[i+1]["text"] == button_list[i+2]["text"] == m:
            win_writer(m)
            return True
    for i in range(0, 3):
        if button_list[i]["text"] == button_list[i+3]["text"] == button_list[i+6]["text"] == m:
            win_writer(m)
            return True
    if button_list[0]["text"] == button_list[4]["text"] == button_list[8]["text"] == m:
        win_writer(m)
        return True
    elif button_list[2]["text"] == button_list[4]["text"] == button_list[6]["text"] == m:
        win_writer(m)
        return True
    else:
        return False


# ---------------------------- UI SETUP ---------------------------------


window = Tk()
window.title("Tic Tac Toe")
window.config(padx=30, pady=30)

button_1 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_1))
button_1.grid(row=2, column=0)

button_2 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_2))
button_2.grid(row=2, column=1)

button_3 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_3))
button_3.grid(row=2, column=2)

button_4 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_4))
button_4.grid(row=3, column=0)

button_5 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_5))
button_5.grid(row=3, column=1)

button_6 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_6))
button_6.grid(row=3, column=2)

button_7 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_7))
button_7.grid(row=4, column=0)

button_8 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_8))
button_8.grid(row=4, column=1)

button_9 = Button(padx=35, pady=35, width=5, command=lambda: change_button(button_9))
button_9.grid(row=4, column=2)

button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

player_1_label = Label(text="Player 1: X", font=(FONT_NAME, 12))
player_1_label.grid(row=0, column=0)

player_2_label = Label(text="Player 2: 0", font=(FONT_NAME, 12))
player_2_label.grid(row=0, column=2)

turn_label = Label(text="", font=(FONT_NAME, 10))
turn_label.grid(row=1, column=1)

change_player()

window.mainloop()
