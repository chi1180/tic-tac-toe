### tic-tac-toe game

from tkinter import *
from tkinter.messagebox import *


class Board:

    def __init__(self, size=3):
        self.size = size
        self.clear()

    def clear(self):
        self.marks = [[""] * self.size for _ in range(self.size)]

    def __iter__(self):
        return iter(self.marks)

    def is_full(self):
        return all(mark != "" for marks in self.marks for mark in marks)

    def is_putable(self, row, column):
        return self.marks[row][column] == ""

    def put(self, row, column, mark):
        self.marks[row][column] = mark

    def has_line(self, mark):
        line = [mark] * self.size
        return (line in self.marks or
                tuple(line) in zip(*self.marks) or
                line == [marks[i] for i, marks in enumerate(self.marks)] or
                line == [marks[i] for i, marks in enumerate(self.marks[::-1])])


class BoardUI:  # Input/Output User Interface for Board

    def __init__(self, board, put):
        self.board = board
        self.buttons = [[self._make_button(mark, put, row, column)
                         for column, mark in enumerate(marks)]
                        for row, marks in enumerate(board)]

    def _make_button(self, mark, put, row, column):
        button = Button(text=mark,
                        command=lambda: put(row, column),
                        width=5,
                        height=2,
                        font=", 24")
        button.grid(row=row, column=column)
        return button

    def update(self):
        for buttons, marks in zip(self.buttons, self.board):
            for button, mark in zip(buttons, marks):
                button["text"] = mark


class Player:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


class TicTacToe:

    def __init__(self, exit_):
        self.exit = exit_
        self.board = Board()
        self.ui = BoardUI(self.board, self.put)
        self.player1 = Player("first player", "O")
        self.player2 = Player("seocnd player", "X")
        self.turn = {self.player1: self.player2, self.player2: self.player1}

    def play(self):
        self.player = self.player1
        self.board.clear()
        self.ui.update()

    def put(self, row, column):
        if not self.board.is_putable(row, column):
            showinfo("against the rules",
                     "This square has selected!\n" +
                     "You must select to square that wasn't selected.")
            return
        self.board.put(row, column, self.player.mark)
        self.ui.update()
        if self.board.has_line(self.player.mark):
            self.win(self.player)
        elif self.board.is_full():
            self.draw()
        else:
            self.player = self.turn[self.player]

    def win(self, player):
        showinfo("game end",
                 f"This game's winer is {player.name}({player.mark})!")
        self.ask_play_again()

    def draw(self):
        showinfo("game end", "This game is draw!")
        self.ask_play_again()

    def ask_play_again(self):
        if askyesno("replay or exit", "Are you want to play again?"):
            self.play()
        else:
            self.exit()


def main():
    root = Tk()
    root.title("tic tac toe game")
    game = TicTacToe(root.quit)
    game.play()
    root.mainloop()

if __name__ == "__main__":
    main()
