import tkinter as tk



def create_chessboard():
    chessboard = []
    for row in range(8):
        chessboard_row = []
        for col in range(8):
            if (row + col) % 2 == 0:
                chessboard_row.append('W')  # Case blanche
            else:
                chessboard_row.append('B')  # Case noire
        chessboard.append(chessboard_row)
    return chessboard


def print_chessboard(chessboard):
    for row in chessboard:
        print(' '.join(row))

chessboard = create_chessboard()

racine = tk.Tk()
label = tk.Label(racine, text=chessboard)
bouton = tk.Button(racine, text="Quitter", fg="red", command=racine.destroy)
label.pack()
bouton.pack()

if __name__ == "__main__":
  racine.mainloop()
    # chessboard = create_chessboard()
    # print_chessboard(chessboard)