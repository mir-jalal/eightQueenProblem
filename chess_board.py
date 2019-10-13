from PIL import Image, ImageTk
import tkinter
import math
import eight_queen_solution
import _thread



class chess_board:
    def __init__(self, board_size):
        self.chess_board_arr = []

        self.root = tkinter.Tk()
        self.default_size = board_size * 60

        img = Image.open("queen.png")
        img = img.resize((60, 60))
        self.queen_image = ImageTk.PhotoImage(img)

        error_img = Image.open("queen_error.png")
        error_img = error_img.resize((60,60))
        self.queen_unsafe_image = ImageTk.PhotoImage(error_img)

        self.root.title(str(board_size) + " queen Problem")
        self.root.minsize(width=self.default_size +
                          150, height=self.default_size)
        self.root.maxsize(width=self.default_size +
                          150, height=self.default_size)

        self.canvas = tkinter.Canvas(
            self.root, width=self.default_size, height=self.default_size)
        self.canvas.place(x=0, y=0)
        self.create_canvas(board_size)
        self.canvas.bind("<Button-1>", self.mouse_click)

        self.brute_force_button = tkinter.Button(self.root, text="Find Solution", command=self.branch_bound)
        self.brute_force_button.place(x=self.default_size+20, y=10)
        self.brute_force_button.config(width=10)

        self.clear_button = tkinter.Button(self.root, text="Clear", command=self.clear)
        self.clear_button.place(x=self.default_size+20, y=50)
        self.clear_button.config(width=10)

        self.string_message = tkinter.StringVar()
        self.string_message.set("")

        self.message_label = tkinter.Label(self.root, textvariable=self.string_message)
        self.message_label.place(x=self.default_size+20, y=90)
        self.message_label.config(fg="#ff0000", font=(20))

        self.root.mainloop()

    def find_solution(self):

        history = []
        if(eight_queen_solution.all_safe_queens(self.chess_board_arr)):
            self.brute_force([], self.chess_board_arr, eight_queen_solution.queen_counter(self.chess_board_arr))
            self.refresh_board()


    def brute_force(self,history, arr, count):
        if(count==len(arr)):
            return True
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (not eight_queen_solution.is_unsafe(arr, i, j)) and arr[i][j]==0:
                    arr[i][j]=1
                    if self.brute_force(history, arr, count+1):
                        return True
                    arr[i][j] = 0

        return False

    def branch_bound(self):
        if not eight_queen_solution.all_safe_queens(self.chess_board_arr):
            return
        right_dioganal_arr = []
        left_dioganal_arr = []
        row_arr = []
        col_arr = []
        n = len(self.chess_board_arr)

        for i in range(n):
            temp_right_dioganal_arr = []
            temp_left_dioganal_arr = []
            for j in range(n):
                temp_right_dioganal_arr.append(i + j)
                temp_left_dioganal_arr.append(i-j+n-1)
            right_dioganal_arr.append(temp_right_dioganal_arr)
            left_dioganal_arr.append(temp_left_dioganal_arr)

        row_arr = [False] * n
        col_arr = [False] * n
        x=2*n-1
        right_dioganal_arr_look = [False] * x
        left_dioganal_arr_look = [False] * x

        for i in range(n):
            for j in range(n):
                if self.chess_board_arr[i][j]==1:
                    right_dioganal_arr_look[right_dioganal_arr[i][j]]=True
                    left_dioganal_arr_look[left_dioganal_arr[i][j]]=True
                    row_arr[i]=True
                    col_arr[j]=True

        if self.solve_algorithm(0, right_dioganal_arr, left_dioganal_arr, right_dioganal_arr_look, left_dioganal_arr_look, row_arr,col_arr):
            self.string_message.set("")
            self.refresh_board()
        else:
            self.string_message.set("No solution")

    def solve_algorithm(self, j, right_dioganal_arr, left_dioganal_arr,right_dioganal_arr_look, left_dioganal_arr_look, row_arr, col_arr):
        if(j>=len(self.chess_board_arr)):
            return True
        if col_arr[j] == True:
            return self.solve_algorithm(j+1, right_dioganal_arr, left_dioganal_arr, right_dioganal_arr_look, left_dioganal_arr_look, row_arr, col_arr)

        for i in range(len(self.chess_board_arr)):
            if eight_queen_solution.is_safe(i, j, right_dioganal_arr, left_dioganal_arr, right_dioganal_arr_look, left_dioganal_arr_look, row_arr):
                self.chess_board_arr[i][j] = 1
                row_arr[i] = True
                right_dioganal_arr_look[right_dioganal_arr[i][j]] = True
                left_dioganal_arr_look[left_dioganal_arr[i][j]] = True
                #self.put_figure(j, i, False)
                #self.root.update()

                if self.solve_algorithm(j+1, right_dioganal_arr,left_dioganal_arr,right_dioganal_arr_look,left_dioganal_arr_look, row_arr, col_arr):
                    return True

                #self.delete_figure(j,i)
                #self.root.update()
                self.chess_board_arr[i][j] = 0
                row_arr[i] = False
                right_dioganal_arr_look[right_dioganal_arr[i][j]] = False
                left_dioganal_arr_look[left_dioganal_arr[i][j]] = False

        return False


    def clear(self):
        self.create_canvas(int(self.default_size/60))

    def mouse_click(self, event):
        x = math.ceil(event.x/60-1)
        y = math.ceil(event.y/60-1)

        if(self.chess_board_arr[y][x] == 0):
            self.chess_board_arr[y][x] = 1
        else:
            self.delete_figure(x, y)
            self.chess_board_arr[y][x] = 0

        self.refresh_board()

    def refresh_board(self):

        unsafe_queens_arr = eight_queen_solution.unsafe_queens(self.chess_board_arr)

        for element in unsafe_queens_arr:
            self.put_figure(element[1], element[0], element[2])

    def create_canvas(self, n):
        new_chess_board_arr = []
        for i in range(n):
            temp_arr = []
            for j in range(n):
                self.delete_figure(i, j)
                temp_arr.append(0)
            new_chess_board_arr.append(temp_arr)
        self.chess_board_arr = new_chess_board_arr

    def put_figure(self, x, y, error):
        self.canvas.create_image(
            x * 60 + 30, y * 60 + 30, image=(self.queen_unsafe_image if error else self.queen_image))


    def delete_figure(self, x, y):
        self.canvas.create_rectangle(x * 60, y * 60, x * 60 + 60, y * 60 + 60, fill=(
            "#769656" if (x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0) else "#eeeed2"))
