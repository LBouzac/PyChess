import chess
import tkinter as tk

class ChessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.geometry("800x800")
        self.board = chess.Board()
        self.canvas = tk.Canvas(self, width=800, height=800)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill=color)
        self.draw_pieces()

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board.piece_at(chess.square(i, j))
                if piece is not None:
                    filename = f"pieces/{piece.symbol().lower()}.png"
                    try:
                        img = tk.PhotoImage(file=filename)
                        self.canvas.create_image(i * 100, j * 100, image=img, anchor="nw")
                        self.canvas.image = img  # Keep a reference to avoid garbage collection
                    except tk.TclError:
                        print(f"Error: File {filename} not found")

if __name__ == '__main__':
    app = ChessApp()
    app.mainloop()