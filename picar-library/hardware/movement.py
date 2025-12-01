from picarx import Picarx
from status.action import Action


class Movement:
    """Low level class responsible for the movement of the car."""
    def __init__(self):
        self.picar = Picarx()

    def stop(self):
        """Stops the car"""
        print("Stopping the car")
        self.picar.stop()


    def forward(self, distance=80):
        """Moves the car forward"""
        print("Moving forward")
        self.picar.set_dir_servo_angle(0)
        self.picar.forward(distance)

    def backward(self, distance=80):
        """Moves the car backward"""
        print("Moving backward")
        self.picar.set_dir_servo_angle(0)
        self.picar.backward(distance)

    def turn(self, direction, angle, distance=80):
        """
            Turns the car in the specified direction by the given angle

        Args:
            direction (Action): Direction to turn ('LEFT' or 'RIGHT')
            angle (int): Angle in degrees to turn
            distance (int): Distance to move forward after turning
        """
        print(f"Turning {direction} by {angle} degrees")
        if direction == Action.LEFT:
            self.picar.set_dir_servo_angle(-angle)
            self.picar.forward(distance)
        elif direction == Action.RIGHT:
            self.picar.set_dir_servo_angle(angle)
            self.picar.forward(distance)