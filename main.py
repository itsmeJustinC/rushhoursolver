from Car import Car

def draw_board(move):
    board = [[0, 0, 0, 0, 0, 0] for i in range(6)]
    for car in move:
        for point in car.points:
            board[point[1]][point[0]] = car.number
    print("+------------+")
    for line in board:
        print("|", end="")
        for spot in line:
            print(str(spot) + " ", end="")
        print("|")
    print("+------------+")

def get_valid_moves(cars):
    print("bye")
    dirs = ("right", "left", "up", "down")
    valid_moves = []
    for car in cars:
        for dir in dirs:
            # draw_board(cars)
            if car.can_move(dir):
                car.move(dir)
                # draw_board(cars)
                valid_moves.append(cars)
                car.undo_last_move()
                # draw_board(cars)

    return valid_moves



moves = []

cars = []
cars.append(Car(3, "vertical", (0, 0), 1))
cars.append(Car(2, "horizontal", (1, 0), 2))
cars.append(Car(2, "horizontal", (1, 2), 3))
cars.append(Car(3, "vertical", (3, 1), 4))
cars.append(Car(2, "vertical", (0, 3), 5))
cars.append(Car(2, "horizontal", (1, 4), 6))
cars.append(Car(3, "horizontal", (2, 5), 7))
cars.append(Car(3, "vertical", (5, 3), 8))

for move in get_valid_moves(cars):
    moves.append(move)

print(moves)
# while len(moves) > 0:
#     pass

for move in moves:
    draw_board(move)