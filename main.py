import tkinter as tk
from tkinter import messagebox

class TicTacToe:
	def __init__(self, master):
		self.master = master
		self.current_player = "X"
		self.board = [[" " for _ in range(3)] for _ in range(3)]

		self.create_widgets()

	def create_widgets(self):
		self.frame = tk.Frame(self.master)
		self.frame.pack()

		self.buttons = []
		
		for i in range(3):
			row = []
			for j in range(3):
				btn = tk.Button(
					self.frame, text=" ", width=4, height=2,
					command=lambda x=i, y=j: self.on_button_click(x, y)
				)
				btn.grid(row=i, column=j)
				row.append(btn)
			self.buttons.append(row)

	def on_button_click(self, row, col):
		if self.board[row][col] == " ":
			self.board[row][col] = self.current_player
			self.buttons[row][col].config(text=self.current_player)

			if self.check_winner(self.current_player):
				messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
				self.reset_game()
			elif self.check_draw():
				messagebox.showinfo("Tic Tac Toe", "It's a draw!")
				self.reset_game()
			else:
				self.current_player = "X" if self.current_player == "O" else "O"


	def check_winner(self, player):
		for i in range(3):
			if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
				return True

		for j in range(3):
			if self.board[0][j] == self.board[1][j] == self.board[2][j] == player:
				return True

		if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
			return True
		if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
			return True

		return False

	def check_draw(self):
		for i in range(3):
			if " " in self.board[i]:
				return False
		return True

	def reset_game(self):
		self.current_player = "X"

		for i in range(3):
			for j in range(3):
				self.board[i][j] = " "
				self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
	root = tk.Tk()
	root.title('Minesweeper')
	root.resizable(False, False)
	
	app = TicTacToe(root)
	
	root.mainloop()

