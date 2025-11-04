from hardware.movement import Movement


class Navigation:
    """High level class responsible for the movement of the car"""

    def __init__(self):
        self.movement = Movement()

    def stop(self):
        """Stops the car"""
        self.movement.stop()

    def forward(self):
        """Moves the car forward"""
        self.movement.forward()

    def backward(self):
        """Moves the car backward"""
        self.movement.backward()

    def turn(self, direction, angle):
        """Turns the car in the specified direction by the given angle"""
        self.movement.turn(direction, angle)