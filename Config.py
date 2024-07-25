from Car import Car

class Config:
    def __init__(self, cars):
        self.cars = cars

    def __eq__(self, value):
        return sorted(self.cars) == sorted(value)

    def __hash__(self):
        return hash(tuple(sorted(self.cars)))

    def get_neighbors(self):
        valid_moves = []
        dirs = ("right", "left", "up", "down")
        for car in self.cars:
            for dir in dirs:
                # draw_board(cars)
                for dist in range(1, 6):
                    if car.can_move(dir, dist, self.cars):
                        car.move(dir)
                        new_car = Car(car.length, car.direction, car.pos, car.number)
                        new_cars = self.cars[:self.cars.index(car)] + [new_car] + self.cars[self.cars.index(car)+1:]
                        new_config = Config(new_cars)
                        valid_moves.append(new_config)
                        car.undo_last_move()
                        # draw_board(cars)
                    else:
                        break

        return valid_moves

    def is_solution(self):
        for car in self.cars:
            if car.number == "@" and car.pos == (5, 2):
                return True
