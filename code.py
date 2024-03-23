
###  tic-tac-toe game


from tkinter import *
from tkinter.messagebox import *

class TicTacToe(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("tic tac toe game")

        self.turn = 1
        self.turn_mark = [ "", "!", "?" ]
        self.turn_name = [ "first turn", "second turn" ]

        self.setBoardData()
        self.createBoardView()

    def setBoardData(self):
        self.board = []
        square_num = 0

        for c in range(3):
            self.board.append([])

            for r in range(3):
                square_num += 1

                square = [ square_num, 0 ]
                self.board[c].append(square)

    def createBoardView(self):
        for c in range(3):
            for r in range(3):
                # set inner text by selected turn
                inner_text = self.turn_mark[self.board[c][r][1]]

                # set clicked fundtion's arugument
                square_num = self.board[c][r][0]

                square = Button(
                    self.master,
                    text=inner_text,
                    command=lambda arug=square_num: self.squareClicked(arug),
                    width=5,
                    height=2,
                    font=", 24")

                square.grid(row = c, column = r)

    def squareClicked(self, square_num):
        for c in range(3):
            for r in range(3):
                # check selecting square's number is the argu's number
                is_arug_square = self.board[c][r][0] == square_num

                if is_arug_square:
                    # check to is this square was selected
                    selected = self.board[c][r][1]

                    if selected:
                        showinfo("against the rules", "This square has selected!\nYou must select to square that wasn't selected.")
                    else:
                        self.board[c][r][1] = self.turn

                        self.createBoardView()
                        self.turnToggleChange()
                        self.winerCheck()

    def turnToggleChange(self):
        turn = self.turn

        if turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def winerCheck(self):
        winer = 0

        # check row line and column line
        for c in range(3):
            is_row_selected_by_only_turn = self.board[c][0][1] == self.board[c][1][1] == self.board[c][2][1] and self.board[c][2][1]
            is_column_selected_by_only_turn = self.board[0][c][1] == self.board[1][c][1] == self.board[2][c][1] and self.board[2][c][1]

            if is_row_selected_by_only_turn:
                winer = self.board[c][2][1]
                break
            elif is_column_selected_by_only_turn:
                winer = self.board[2][c][1]
                break

        if winer:
            self.showWiner(winer_num=winer)
        else:
            # check x line
            is_x_right_selected_by_only_turn = self.board[0][2][1] == self.board[1][1][1] == self.board[2][0][1] and self.board[2][0][1]
            is_x_left_selected_by_only_turn = self.board[0][0][1] == self.board[1][1][1] == self.board[2][2][1] and self.board[2][2][1]

            if is_x_right_selected_by_only_turn:
                winer = self.board[2][0][1]
            elif is_x_left_selected_by_only_turn:
                winer = self.board[2][2][1]

            if winer:
                self.showWiner(winer_num=winer)
            else:
                # check is this drow
                selected_count = 0

                for c in range(3):
                    for r in range(3):
                        is_selected = self.board[c][r][1]

                        if is_selected:
                            selected_count += 1

                if selected_count == 9:
                    showinfo("game end", "This game is draw!")
                    self.askPlayAgain()


    def showWiner(self, winer_num):
        message = "This game's winer is " + self.turn_name[winer_num - 1] + "!"
        showinfo("game end", message)
        self.askPlayAgain()

    def askPlayAgain(self):
        message = "Are you want to play again?"
        ask_replay = askyesno("replay or exit", message)

        if ask_replay:
            self.__init__(root)
        else:
            self.master.quit()




# run
root = Tk()
frame = TicTacToe(root)
frame.grid()

root.mainloop()

