import chess_board
import tkinter


def start_program():
    n = int(text_box.get())
    root.destroy()
    chess_board.chess_board(n)


root = tkinter.Tk()
root.title("N queen Problem")
root.minsize(width=500, height=250)
root.maxsize(width=500, height=250)

label = tkinter.Label(root, text="Board Size: ")
label.place(x=40, y=100)
label.config(font=("Calibri", 20))

text_box = tkinter.Entry(root, width=8)
text_box.place(x=200, y=100)
text_box.config(font=("Calibri", 20))

button = tkinter.Button(root, text="Start", command=start_program)
button.place(x=375, y=95)
button.config(font=("Calibri", 20))

root.mainloop()
