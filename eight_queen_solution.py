def unsafe_queens(arr):
    unsafe_queens_arr = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] == 1 and is_unsafe(arr, i, j)):
                unsafe_queens_arr.append([i, j, True])
            elif(arr[i][j] == 1):
                unsafe_queens_arr.append([i, j, False])
    return unsafe_queens_arr


def is_unsafe(arr, x, y):

    for i in range(len(arr)):
        if(i != y and arr[x][i] == 1):
            return True
        if(i != x and arr[i][y] == 1):
            return True

    for i in range(1, len(arr)):
        if(x + i < len(arr) and y + i < len(arr) and arr[x + i][y + i] == 1):
            return True
        if(x - i > -1 and y - i > -1 and arr[x - i][y - i] == 1):
            return True
        if(x + i < len(arr) and y - i > -1 and arr[x + i][y - i] == 1):
            return True
        if(x - i > -1 and y + i < len(arr) and arr[x - i][y + i] == 1):
            return True


def all_safe_queens(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] == 1 and is_unsafe(arr, i, j)):
                return False
    return True


def is_safe(i, j, right_diagonal_arr, left_diagonal_arr, right_diagonal_arr_look, left_diagonal_arr_look, row_arr):
    if right_diagonal_arr_look[right_diagonal_arr[i][j]] or left_diagonal_arr_look[left_diagonal_arr[i][j]] or row_arr[i]:
        return False
    return True


def column_occupied(arr, j):
    for i in range(j):
        if arr[i][j] == 1:
            return True
    return False


def queen_counter(arr):
    counter = 0
    for i in arr:
        for j in i:
            counter = counter + j
    return counter
