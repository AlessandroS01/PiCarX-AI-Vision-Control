from typing import Any

from hardware.movement import Movement
from status.action import Action
from status.prediction import Prediction


class Navigation:
    """High level class responsible for the movement of the car"""

    def __init__(self):
        self.movement = Movement()

    def perform_action(self, predictions: list[Prediction]):
        """
            Performs action according to the predicted list of checkpoints

        Args:
            predictions: Prediction object containing frame and detected checkpoints
        """

        # TODO implement how to decide which detected object to take into consideration
        bbox = predictions[0].bounding_box
        action = self.decide_action(bbox)

        if action == Action.FORWARD:
            self.forward()
        elif action == Action.BACKWARD:
            self.backward()
        elif action == Action.LEFT:
            angle = self.angle_retrieval(bbox)
            self.turn(Action.LEFT, angle)
        elif action == Action.RIGHT:
            angle = self.angle_retrieval(bbox)
            self.turn(Action.RIGHT, angle)
        self.stop()


    def decide_action(self, bounding_box) -> Action:
        """
            Decides the action to perform based on the predictions

        Args:
            bounding_box: Checkpoint bounding box

        Returns:
            action: Action to perform
        """
        x1, y1, x2, y2 = bounding_box

        # TODO implement safe stopping here

        if x1 < 640 / 2 and x2 < 640 / 2:
            action = Action.LEFT
        elif x1 > 640 / 2 and x2 > 640 / 2:
            action = Action.RIGHT
        else:
            action = Action.FORWARD


        return action

    def angle_retrieval(self, bounding_box) -> int:
        """
            Handler for steering angle prediction according to the given action

        Args:
            bounding_box: Checkpoint bounding box

        Returns:
            angle: Angle in degrees to turn
        """
        x1, y1, x2, y2 = bounding_box

        # LEFT
        if x1 < 640 / 8:
            angle = -35
        elif x1 < 640 / 4:
            angle = -20
        elif x1 < 640 / 2:
            angle = -10
        # RIGHT
        elif x1 > 640 / 8:
            angle = 35
        elif x1 > 640 / 4:
            angle = 20
        else:
            angle = 10

        return angle

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
        """
            Turns the car in the specified direction by the given angle

        Args:
            direction (Action): Direction to turn ('LEFT' or 'RIGHT')
            angle (int): Angle in degrees to turn
        """
        self.movement.turn(direction, angle)