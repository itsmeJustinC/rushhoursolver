class Config:
    def __init__(self, id, cars):
        self.cars = cars

    def __eq__(self, value):
        return sorted(self.cars) == sorted(value)

    def get_neighbors(self):
        return []
    # TODO

    def is_solution(self):
        for car in self.cars:
            if car.number == "@" and car.pos == (5, 2):
                return True
