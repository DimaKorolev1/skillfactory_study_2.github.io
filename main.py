import random


player_symbols = "-OX"
row_symbols = "123"
column_symbols = "123"


def print_game_map(gm):
    for row in gm:
        for cell in row:
            print(player_symbols[cell], end=" ")
        print()


def is_tie(gm):
    for row in gm:
        for cell in row:
            if cell == 0:
                return False
    return True

def is_completed(gm):
    assert len(gm) > 0
    assert len(gm[0]) > 0
    for row in gm:
        first = row[0]
        if first != 0:
            for cell in row[1:]:
                if cell != first:
                    break
            else:
                return True, first

    for j in range(len(gm[0])):
        first = gm[0][j]
        if first != 0:
            for i in range(1, len(gm)):
                if gm[i][j] != first:
                    break
            else:
                return True, first

    assert len(gm) == len(gm[0])
    diag = gm[0][0]
    if diag != 0:
        for i in range(len(gm)):
            if gm[i][i] != diag:
                break
        else:
            return True, diag

    inv_diag = gm[0][len(gm) - 1]
    if inv_diag != 0:
        for i in range(len(gm)):
            if gm[i][len(gm) - i - 1] != inv_diag:
                break
        else:
            return True, inv_diag

    return is_tie(gm), 0


def computer(gm, player):
    row_index = list(range(len(gm)))
    random.shuffle(row_index)
    for i in row_index:
        row = gm[i]
        empty_cells = []
        for j, cell in enumerate(row):
            if cell == 0:
                empty_cells.append(j)

        if len(empty_cells) > 0:
            player_row = i
            player_column = random.choice(empty_cells)
            return player_row, player_column


def input_player(gm, player):
    while True:
        print_game_map(gm)

        player_input = input(f"Игрок {player}, введите позицию: ")
        if len(player_input) != 2:
            print("Введено неверное количество символов. Формат: 11.")
            continue
        player_row, player_column = player_input

        player_row = row_symbols.find(player_row)
        if player_row == -1:
            print("Введен неверный номер ряда. Укажите цифру: ")
            continue

        player_column = column_symbols.find(player_column)
        if player_column == -1:
            print("Введен неверный номер колонки. Укажите цифру: ")
            continue

        if gm[player_row][player_column] > 0:
            print("Эта ячейка уже занята, выберите другую.")
            continue

        return player_row, player_column


game_map = []
for _ in range(3):
    temp = []
    for _ in range(3):
        temp.append(0)
    game_map.append(temp)


current_player = 1
completed, who_won = False, 0

game_players = [None, input_player, computer]

while not completed:
    player_function = game_players[current_player]
    row_index, column_index = player_function(game_map, current_player)
    game_map[row_index][column_index] = current_player

    completed, who_won = is_completed(game_map)

    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1
    else:
        print("Неверный номер игрока")
        exit(1)


print_game_map(game_map)
if who_won != 0:
    print(f"Игрок №{who_won} победил!")
else:
    print("Ничья.")