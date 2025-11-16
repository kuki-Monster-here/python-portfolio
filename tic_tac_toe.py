board = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", "X"]
]

for row in board:
    print("|" + "|".join(row) + "|")
