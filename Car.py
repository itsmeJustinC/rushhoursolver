class Car:
    def __init__(self, length, direction, pos, number):
        self.length = length
        self.direction = direction
        self.pos = pos
        self.number = number
        self.points = []
        self.last_move = (0, 0)
        if self.direction == "vertical":
            self.points = [(pos[0], i) for i in range(pos[1], pos[1] + self.length)]
        if self.direction == "horizontal":
            self.points = [(i, pos[1]) for i in range(pos[0], pos[0] + self.length)]

    def move(self, dir):
        dx = 0
        dy = 0
        if dir == "right":
            dx = 1
        if dir == "left":
            dx = -1
        if dir == "up":
            dy = -1
        if dir == "down":
            dy = 1
        for i in range(len(self.points)):
            print(self.points)
            self.points[i] = (self.points[i][0]+dx, self.points[i][1] + dy)

        self.last_move = (dx, dy)
        

    def undo_last_move(self):
        print(f"last move: {self.last_move}")
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + -self.last_move[0], self.points[i][1] + -self.last_move[1])

    def can_move(self, dir):
        if self.number == 2:
            print(dir)
        if self.direction == "vertical":
            if dir not in ("up", "down"):
                return False
            else:
                if dir == "up":
                    return not any([i[1] - 1 < 0] for i in self.points)
                if dir == "down":
                    return not any([i[1] + 1 > 5] for i in self.points)
        if self.direction == "horizontal":
            if self.number == 2:
                print("direction is horizontal")
            if dir not in ("right", "left"):
                print("THinks it's not a valid direction")
                return False
            else:
                if dir == "right":
                    if self.number == 2:
                        print(f"can move: {not any(i[0] + 1 > 5 for i in self.points)}")
                        # print(any(list(i[0] + 1 > 5 for i in self.points)))
                    return not any(i[0] + 1 > 5 for i in self.points)
                if dir == "left":
                    return not any([i[0] - 1 < 0] for i in self.points)


