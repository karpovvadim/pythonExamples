class Seat:
    def __init__(self, type):
        self.i_type = type

    def __str__(self):
        return f"Seat type: {self.i_type}"


class Engine:
    def __init__(self, size):
        self.i_size = size

    def __str__(self):
        return f"Engine: {self.i_size}"


class Car:
    def __init__(self, color, end_size, seat_type):
        self.i_color = color
        self.engine = Engine(end_size)
        self.seat = Seat(seat_type)

    def print_me(self):
        print(f"Car with color {self.i_color} with {self.engine} and {self.seat}")


if __name__ == "__main__":
    car = Car("blue", "2.5L", "later")
    car.print_me()
    print(car.engine)
    print(car.seat)
    print(car.i_color)
    print(car.engine.i_size)
    print(car.seat.i_type)
