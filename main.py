from Car import Car
from Config import Config
queue = []
predecessors = {}

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


def generate_steps(path):
    counter = 1
    for step in path:
        print(f"Step {counter}")
        draw_board(step)
        print()


def get_path(predcessors, start_config, end_config):
    path = []
    if predcessors.get(end_config) is not None:
        current = end_config
        while current != start_config:
            path.insert(0, current)
            current = predcessors.get(current)
        path.insert(0, start_config)

    return path


cars = []
cars.append(Car(3, "vertical", (0, 0), 'A'))
cars.append(Car(2, "horizontal", (1, 0), 'B'))
cars.append(Car(2, "horizontal", (1, 2), "@"))
cars.append(Car(3, "vertical", (3, 1), 'C'))
cars.append(Car(2, "vertical", (0, 3), 'D'))
cars.append(Car(2, "horizontal", (1, 4), 'E'))
cars.append(Car(3, "horizontal", (2, 5), 'F'))
cars.append(Car(3, "vertical", (5, 3), 'G'))

initial_config = Config(cars)
end_config = None

queue.append(initial_config)

while len(queue) != 0:
    print(f"LENGTH OF QUEUE: {len(predecessors.keys())}")
    current_config = queue.pop(0)
    if current_config.is_solution():
        end_config = current_config
        break
    for config in current_config.get_neighbors():
        if predecessors.get(config) is None:
            predecessors[config] = current_config
            queue.append(config)


path = get_path(predecessors, initial_config, end_config)
generate_steps(path)