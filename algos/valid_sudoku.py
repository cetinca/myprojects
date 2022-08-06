from typing import List

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lst = board
        rows, columns = [], []
        for i in range(82):
            a, b = i // 9, i % 9

            if i % 9 == 0:
                if len(set(rows)) != len(rows): return False
                if len(set(columns)) != len(columns): return False
                rows, columns = [], []

            if i < 81:
                if lst[a][b] != ".": rows.append(lst[a][b])
                if lst[b][a] != ".": columns.append((lst[b][a]))

        x, y, z = [], [], []
        for i in range(82):
            a, b = i // 9, i % 9

            if i % 27 == 0:
                if len(set(x)) != len(x): return False
                if len(set(y)) != len(y): return False
                if len(set(z)) != len(z): return False
                x, y, z = [], [], []

            if i < 81:
                if b // 3 == 0:
                    if lst[a][b] != ".": x.append(lst[a][b])
                if b // 3 == 1:
                    if lst[a][b] != ".": y.append(lst[a][b])
                if b // 3 == 2:
                    if lst[a][b] != ".": z.append((lst[a][b]))

        return True


# alternative approach
x = zip(*board)
for z in x:
    print(z)
