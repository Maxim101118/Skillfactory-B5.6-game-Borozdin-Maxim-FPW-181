table = [["-"] * 3 for i in range(3)]

def game_board(table):
    print("  0 1 2")
    for i in range(3):
        row_table = " ".join(table[i])
        print(f"{i} {row_table}")

def player_input():
    while True:
        x, y = map(int, input("Сделайте ход: ").split())

        if x < 0 or x > 2 and y < 0 or y > 2:
            print("Ввод вне диапазона координат!")
            continue

        if table[x][y] != "-":
            print("Клетка уже занята!")
            continue

        return x, y

def game_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(table[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

counter = 0
while True:
    counter += 1
    game_board(table)
    if counter % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = player_input()

    if counter % 2 == 1:
        table[x][y] = "X"
    else:
        table[x][y] = "0"

    if game_win():
        break

    if counter == 9:
        print(" Ничья!")
        break
