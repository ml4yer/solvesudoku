sudoku = [
    [8, 0, 0, 9, 3, 0, 0, 0, 2],
    [0, 0, 9, 0, 0, 0, 0, 4, 0],
    [7, 0, 2, 1, 0, 0, 9, 6, 0],
    [2, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 7, 0, 0, 0, 6, 0, 0, 5],
    [0, 2, 7, 0, 0, 8, 4, 0, 6],
    [0, 3, 0, 0, 0, 0, 5, 0, 0],
    [5, 0, 0, 0, 6, 2, 0, 0, 8]
]


def table(s):
    for i in range(len(s)):
        if i % 3 == 0:
            print()
        for j in range(len(s[0])):
            if j % 3 == 0:
                print("  ", end="")
            if j == 8:
                print(s[i][j])
            else:
                print(s[i][j], end=" ")
    print("      ---- End ----")


table(sudoku)


def possible(row, column, n):
    global sudoku
    if n in sudoku[row]:
        return False
    for i in range(len(sudoku[0])):
        if sudoku[i][column] == n:
            return False
    r = (row // 3) * 3
    c = (column // 3) * 3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if sudoku[i][j] == n:
                return False
    return True


def solve():
    global sudoku
    for row in range(len(sudoku[0])):
        for column in range(len(sudoku)):
            if sudoku[row][column] == 0:
                for n in range(1, 10):
                    if possible(row, column, n):
                        sudoku[row][column] = n
                        solve()
                        sudoku[row][column] = 0
                return
    table(sudoku)


solve()
