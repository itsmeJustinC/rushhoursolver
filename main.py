from Car import Car
from Config import Board
queue = []
predecessors = {}
move_id = 0


def draw_board(move):
    if type(move[0]) == str:
        print(f"CAR MOVED: {move[0]}")
        move = move[1:]
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

def get_valid_moves(board, cur_path):
    dirs = ("right", "left", "up", "down")
    valid_moves = []
    for car in cars:
        for dir in dirs:
            # draw_board(cars)
            for dist in range(1, 6):
                if car.can_move(dir, dist, cars):
                    car.move(dir)
                    if car.is_in_win_pos():
                        new_car = Car(car.length, car.direction, car.pos, car.number)
                        new_cars = cars[:cars.index(car)] + [new_car] + cars[cars.index(car)+1:]
                        valid_moves.append([move_id] + new_cars)
                        move_id += 1
                        car.undo_last_move()
                    else:# draw_board(cars)
                        print("CAR AFTER MOVE")
                        print(car)
                        print(car.pos)
                        new_car = Car(car.length, car.direction, car.pos, car.number)
                        new_cars = cars[:cars.index(car)] + [new_car] + cars[cars.index(car)+1:]
                        print("NEW CARS")
                        print(new_cars)
                        if new_cars not in previous_moves:
                            valid_moves.append([move_id] + new_cars)
                            move_id += 1
                        car.undo_last_move()
                        # draw_board(cars)
                else:
                    break

    return valid_moves


cars = []
cars.append(Car(3, "vertical", (0, 0), 1))
cars.append(Car(2, "horizontal", (1, 0), 2))
cars.append(Car(2, "horizontal", (1, 2), "@"))
cars.append(Car(3, "vertical", (3, 1), 4))
cars.append(Car(2, "vertical", (0, 3), 5))
cars.append(Car(2, "horizontal", (1, 4), 6))
cars.append(Car(3, "horizontal", (2, 5), 7))
cars.append(Car(3, "vertical", (5, 3), 8))

initial_config = Board(move_id, cars)

queue.append(initial_config)

while len(queue) != 0:
    current_config = queue.pop(0)
    neighbors = []
    for config in current_config.get_neighbors():
        if predecessors.get(config) is None:
            predecessors[config] = current_config
            queue.append(config)

    

print(f"NUMBER OF MOVES: {len(moves)}")
while len(moves) > 0:
    for move in get_valid_moves(moves[0][1:]):
        moves.append(move)
    moves = moves[1:]


draw_board(cars)

for move in moves:
    draw_board(move)