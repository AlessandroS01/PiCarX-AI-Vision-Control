import time

from picarx import Picarx

from status.action import Action


class Movement:
    """Low level class responsible for the movement of the car."""
    def __init__(self):
        self.picar = Picarx()
        self.distance = 2

    def stop(self):
        """Stops the car"""
        print("Stopping the car")
        self.picar.stop()


    def forward(self, distance=20):
        """Moves the car forward"""
        print("Moving forward")
        time.sleep(0.25)
        self.picar.forward(self.distance)

    def backward(self, distance=80):
        """Moves the car backward"""
        print("Moving backward")
        self.picar.backward(self.distance)

    def turn(self, direction, angle, distance=20):
        """
            Turns the car in the specified direction by the given angle

        Args:
            direction (Action): Direction to turn ('LEFT' or 'RIGHT')
            angle (int): Angle in degrees to turn
            distance (int): Distance to move forward after turning
        """
        print(f"Turning {direction} by {angle} degrees")
        self.set_servo_angle(angle)
        self.forward()
        self.set_servo_angle(0)

    def set_servo_angle(self, angle):
        """
            Sets the steering servo to the specified angle.
        Args:

            angle(int): Angle in degrees to set the servo
        """
        self.picar.set_dir_servo_angle(angle)