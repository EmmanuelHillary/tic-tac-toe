from tkinter import *
import sqlite3
from tkinter.messagebox import *

root = Tk()
root.geometry('360x180')
root.title('X\'s and O\'s')
root.iconbitmap('bugs.ico')
root.configure(bg='light blue')

player = 'X'
player1 = ''
player2 = ''
def save1():
    global player_name1
    global first_player_ent
    global player1
    player1 = ''
    player1 += first_player_ent.get()
    first_player_ent.delete(0, END)


def save2():
    global second_player_ent
    global player2
    player2 = ''
    player2 = second_player_ent.get()
    second_player_ent.delete(0, END)


def handle_turn(num):
    global chk
    global game_board
    global player
    chk = False
    global player1
    global player2
    global player_name
    if player == 'X' and game_board[num] == 0:
        board[num].configure(text=player)
        game_board[num] = 'X'
        player_name = player1
        chk = True
    elif player == 'O' and game_board[num] == 0:
        board[num].configure(text=player)
        player_name = player2
        game_board[num] = 'O'
        chk = True
    check_win()
    check_tie()
    flip_player()


def start_games():
    global game_board
    global board
    global game
    global player_name
    game = Tk()
    game.title('X\'s and O\'s')
    game.iconbitmap('bugs.ico')

    board = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
    game_board = [0, 0, 0,
                  0, 0, 0,
                  0, 0, 0]

    display_board()

    game.mainloop()


def display_board():
    global game_board
    global board
    global game
    global player
    global player_name
    global player1
    player_name = player1
    board[0] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(0))
    board[0].grid(row=0, column=0)
    board[1] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(1))
    board[1].grid(row=0, column=1)
    board[2] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(2))
    board[2].grid(row=0, column=2)
    board[3] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(3))
    board[3].grid(row=1, column=0)
    board[4] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(4))
    board[4].grid(row=1, column=1)
    board[5] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(5))
    board[5].grid(row=1, column=2)
    board[6] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(6))
    board[6].grid(row=2, column=0)
    board[7] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(7))
    board[7].grid(row=2, column=1)
    board[8] = Button(game, width=3, font=('Veranda', 28), bg='yellow', command=lambda: handle_turn(8))
    board[8].grid(row=2, column=2)
    label = Label(game, text=f'It is {player_name}\'s turn', relief=SUNKEN)
    label.grid(row=3, column=0, columnspan=3, sticky=W + E)

def check_win():
    rows()
    columns()
    diagonals()

def check_tie():
    global game_board
    global player
    global player_name
    if 0 not in game_board:
        message = askyesno(title='TIE', message='Its a tie, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
            if player_name == player1:
                player = 'O'
                player_name = player2
            elif player_name == player2:
                player = 'X'
                player_name = player1
        else:
            game.destroy()


def rows():
    global board
    global game_board
    global player_name
    if game_board[0] == game_board[1] == game_board[2] != 0:
        board[0].configure(bg='grey')
        board[1].configure(bg='grey')
        board[2].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()
    elif game_board[3] == game_board[4] == game_board[5] != 0:
        board[3].configure(bg='grey')
        board[4].configure(bg='grey')
        board[5].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()
    elif game_board[6] == game_board[7] == game_board[8] != 0:
        board[6].configure(bg='grey')
        board[7].configure(bg='grey')
        board[8].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()


def columns():
    global board
    global game_board
    global player_name
    if game_board[0] == game_board[3] == game_board[6] != 0:
        board[0].configure(bg='grey')
        board[3].configure(bg='grey')
        board[6].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()
    elif game_board[1] == game_board[4] == game_board[7] != 0:
        board[1].configure(bg='grey')
        board[4].configure(bg='grey')
        board[7].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()
    elif game_board[2] == game_board[5] == game_board[8] != 0:
        board[2].configure(bg='grey')
        board[5].configure(bg='grey')
        board[8].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()


def diagonals():
    global board
    global game_board
    global player_name
    if game_board[0] == game_board[4] == game_board[8] != 0:
        board[0].configure(bg='grey')
        board[4].configure(bg='grey')
        board[8].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()
    elif game_board[2] == game_board[4] == game_board[6] != 0:
        board[2].configure(bg='grey')
        board[4].configure(bg='grey')
        board[6].configure(bg='grey')
        message = askyesno(title='WIN', message=f'{player_name} won, would you like to play again?')
        if message == 1:
            display_board()
            game_board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        elif message == 0:
            game.destroy()


def flip_player():
    global player
    global chk
    global player1
    global player2
    global player_name
    if player == 'X' and chk == True and player_name == player1:
        player = 'O'
        player_name = player2
    elif player == 'O' and chk == True and player_name == player2:
        player = 'X'
        player_name = player1
    try:
        label = Label(game, text=f'It is {player_name}\'s turn', relief=SUNKEN)
        label.grid(row=3, column=0, columnspan=3, sticky=W + E)
    except Exception:
        pass


def page():
    label()
    entry()
    button()
    grid()


def label():
    global page_name
    global first_player_lbl
    global second_player_lbl
    global player_name
    global scores
    page_name = Label(root, text='Tic-Tac-Toe', font=('Veranda', 20, 'bold'), bg='light blue')
    first_player_lbl = Label(root, text='First player')
    second_player_lbl = Label(root, text='second player')


def entry():
    global first_player_ent
    global second_player_ent
    global player_name_ent
    first_player_ent = Entry(root)
    second_player_ent = Entry(root)


def button():
    global first_button
    global second_button
    global start_game
    global delete
    global show_records
    first_button = Button(root, text='save', command=save1)
    second_button = Button(root, text='save', command=save2)
    start_game = Button(root, text='Start game', command=start_games)

def grid():
    global page_name
    global first_player_lbl
    global second_player_lbl
    global first_player_ent
    global second_player_ent
    global first_button
    global second_button
    global start_game
    global scores_lbl
    global player_name
    global player_name_ent
    global delete
    global show_records
    page_name.grid(row=0, column=0, columnspan=5, padx=100)
    first_player_lbl.grid(row=1, column=0, pady=10)
    first_player_ent.grid(row=1, column=1, pady=10)
    second_player_lbl.grid(row=2, column=0, pady=10)
    second_player_ent.grid(row=2, column=1, pady=10)
    first_button.grid(row=1, column=2, ipady=1)
    second_button.grid(row=2, column=2, ipady=1)
    start_game.grid(row=3, column=0, columnspan=5, pady=10, ipadx=120)


page()

root.mainloop()
