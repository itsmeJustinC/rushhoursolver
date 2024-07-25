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

    def __repr__(self):
        string_builder = f"#{self.number}#"
        for i in self.points:
            string_builder += f"X: {i[0]} | Y: {i[1]}\n"
        return string_builder

    def __lt__(self, other):
        return self.number < other.number

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

        # print(f"dX: {dx}, dY: {dy}")
        for i in range(len(self.points)):
            # print(self.points)
            self.points[i] = (self.points[i][0]+dx, self.points[i][1] + dy)
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)

        self.last_move = (dx, dy)
        
    def will_collide(self, dx, dy, cars):
        for car in cars:
            for point in car.points: # other cars
                for self_point in self.points: # current car
                    # print("### CAR COORDINATES ###")
                    # print(f"dX: {dx} dY: {dy}")
                    # print(f"SELF  X: {self_point[0]} Y: {self_point[1]}")
                    # print(f"OTHER  X: {point[0]} Y: {point[1]}")
                    if self_point[0] + dx == point[0] and self_point[1] + dy == point[1]:
                        # print("### COLLISION ###")
                        # print(f"dX: {dx} dY: {dy}")
                        # print(f"SELF  X: {self_point[0]} Y: {self_point[1]}")
                        # print(f"OTHER  X: {point[0]} Y: {point[1]}")

                        return True
        return False

    def undo_last_move(self):
        for i in range(len(self.points)):
            self.points[i] = (self.points[i][0] + -self.last_move[0], self.points[i][1] + -self.last_move[1])
        self.pos = (self.pos[0] + -self.last_move[0], self.pos[1] + -self.last_move[1])

    def can_move(self, dir, dist, cars):
        cars = cars[:cars.index(self)] + cars[cars.index(self)+1:]
        # print(cars)
        # print(f"### CAR NUMBER {self.number} ###")
        if self.direction == "vertical":
            # print("Direction is vertical")
            if dir not in ("up", "down"):
                # print("not up or down")
                return False
            else:
                if dir == "up":
                    # print("DIRECTION IS UP")
                    # thing = not any(i[1] - dist < 0 for i in self.points) and not self.will_collide(0, -dist, cars)
                    # if thing:
                    #     print("CAN GO UP")
                    # else:
                    #     print("CANNOT GO UP")
                    return not any(i[1] - dist < 0 for i in self.points) and not self.will_collide(0, -dist, cars)
                if dir == "down":
                    # thing = not any(i[1] + dist > 5 for i in self.points) and not self.will_collide(0, dist, cars)
                    # if thing:
                    #     print("CAN GO DOWN")
                    # else:
                    #     print("CANNOT GO DOWN")
                    return not any(i[1] + dist > 5 for i in self.points) and not self.will_collide(0, dist, cars)
        if self.direction == "horizontal":
            # print("Direction is horizontal")
            if dir not in ("right", "left"):
                # print("not left or right")
                return False
            else:
                if dir == "right":
                    # self_movement = not any(i[0] + dist > 5 for i in self.points)
                    # collision_movement = self.will_collide(dist, 0, cars)
                    # print(f"CAN MOVE SELF: {self_movement}")
                    # print(f"WILL COLLIDE: {collision_movement}")
                    # thing = not any(i[0] + dist > 5 for i in self.points) and not self.will_collide(dist, 0, cars)
                    # if thing:
                    #     print("CAN GO RIGHT")
                    # else:
                    #     print("CANNOT GO RIGHT")
                    return not any(i[0] + dist > 5 for i in self.points) and not self.will_collide(dist, 0, cars)
                if dir == "left":
                    # print(self.points)
                    # self_movement = not any(i[0] - dist < 0 for i in self.points)
                    # collision_movement = self.will_collide(-dist, 0, cars)
                    # print(f"CAN MOVE SELF: {self_movement}")
                    # print(f"WILL COLLIDE: {collision_movement}")
                    # thing = not any(i[0] - dist < 0 for i in self.points) and not self.will_collide(-dist, 0, cars)
                    # if thing:
                    #     print("CAN GO LEFT")
                    # else:
                    #     print("CANNOT GO LEFT")
                    return not any(i[0] - dist < 0 for i in self.points) and not self.will_collide(-dist, 0, cars)


