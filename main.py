field_size = 3
game_state = [["-" for _ in range(field_size)] for _ in range(field_size)]
step_help = "to make a move, input coordinates in format x y :'2 1'"

def query_input(player):
    while True:
        try:
            query = input(f"{player}, Your turn: ").split(" ")
            coord = (int(query[0]), int(query[1]))
            for x in coord:
                if x > field_size - 1:
                    print(step_help)
                    break
            else:
                return coord
        except (ValueError, IndexError):
            print(step_help)


def check_win(coords: (int, int)):
    row = list(set(game_state[coords[0]]).symmetric_difference({"O", "X"}))
    if len(row) == 1 and row[0] != "-":
        return True

    column = list(set([game_state[x][coords[1]] for x in range(field_size)]).symmetric_difference({"O", "X"}))
    if len(column) == 1 and column[0] != "-":
        return True

    if coords[0] == coords[1]:
        diag = list(set([game_state[x][x] for x in range(field_size)]).symmetric_difference({"O", "X"}))
        if len(diag) == 1 and diag[0] != "-":
            return True

    if coords[0] == (field_size - 1) - coords[1]:
        back_diag = list(set([game_state[x][(field_size - 1) - x] for x in range(field_size)]).symmetric_difference({"O", "X"}))
        if len(back_diag) == 1 and back_diag[0] != "-":
            return True

    return False

def game_loop():
    current_player = ("X", "O")
    print(step_help)

    while True:
        for y in game_state:
            print(*y)
        while True:
            next_step = last_step = query_input(current_player[0])
            if game_state[next_step[0]][next_step[1]] == "-":
                game_state[next_step[0]][next_step[1]] = current_player[0]
                break
            else:
                print(f"field at {next_step[0]}, {next_step[1]} is taken")
        if check_win(last_step):
            print(f"{current_player[0]} has won! ")
            for y in game_state:
                print(*y)
            break

        current_player = (current_player[1], current_player[0])


game_loop()
