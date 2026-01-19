import time

from picarx import Picarx

from status.action import Action


class Movement:
    """Low level class responsible for the movement of the car."""
    def __init__(self):
        self.picar = Picarx()
        self.distance = 1

    def stop(self):
        """Stops the car"""
        print("Stopping the car")
        self.picar.stop()


    def forward(self):
        """Moves the car forward"""
        print("Moving forward")
        self.picar.forward(self.distance)
        time.sleep(0.25)
        self.set_servo_angle(0)
        time.sleep(0.6)
        self.stop()

    def backward(self):
        """Moves the car backward"""
        print("Moving backward")
        self.picar.backward(self.distance)

    def turn(self, direction, angle):
        """
            Turns the car in the specified direction by the given angle

        Args:
            direction (Action): Direction to turn ('LEFT' or 'RIGHT')
            angle (int): Angle in degrees to turn
        """
        print(f"Turning {direction} by {angle} degrees")
        self.set_servo_angle(angle)
        self.forward()

    def calibrate_motors(self, motor_index, direction):
        """Rotates the car

        Args:
            motor_index (int): Index of the motor to calibrate (1 left or 2 right)
            direction (int): Direction to set for calibration (1 forward or -1 backward)
        """

        if motor_index in [1, 2] and direction in [1, -1]:
            self.picar.motor_direction_calibrate(motor_index, direction)


    def set_servo_angle(self, angle):
        """
            Sets the steering servo to the specified angle.
        Args:

            angle(int): Angle in degrees to set the servo
        """
        self.picar.set_dir_servo_angle(angle)