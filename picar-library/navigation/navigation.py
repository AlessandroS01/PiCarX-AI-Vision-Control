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
        action = self.decide_action(predictions)

        if action == Action.FORWARD:
            self.forward()
        elif action == Action.BACKWARD:
            self.backward()
        elif action == Action.LEFT:
            angle = self.angle_retrieval(action, predictions[0])
            self.turn(Action.LEFT, angle)
        elif action == Action.RIGHT:
            angle = self.angle_retrieval(action, predictions[0])
            self.turn(Action.RIGHT, angle)
        self.stop()


    def decide_action(self, predictions: list[Prediction]) -> Action:
        """
            Decides the action to perform based on the predictions

        Args:
            predictions: List of Prediction objects containing frame and detected checkpoints.

        Returns:
            action: Action to perform
        """
        action = Action.FORWARD
        # TODO implement how to decide action here

        return action

    def angle_retrieval(self, action: Action, prediction: Prediction) -> int:
        """
            Handler for steering angle prediction according to the given action

        Args:
            action: Action to perform
            prediction: Prediction object containing frame and detected checkpoints.

        Returns:
            angle: Angle in degrees to turn
        """
        angle = 10
        # TODO implement how to handle angle creation here
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