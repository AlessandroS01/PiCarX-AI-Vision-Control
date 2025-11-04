from navigation.navigation import Navigation
from status.action import Action


class NavigationController:
    """Controller for managing navigation"""
    def __init__(self):
        self.navigation = Navigation()

    def perform_action(self, action: Action):
        """
            Performs action according to the predicted action

        Args:
            action: Action to perform
        """

        if action == Action.FORWARD:
            self.navigation.forward()
        elif action == Action.BACKWARD:
            self.navigation.backward()
        elif action == Action.LEFT:
            angle = self.angle_retrieval(action)
            self.navigation.turn(Action.LEFT, angle)
        elif action == Action.RIGHT:
            angle = self.angle_retrieval(action)
            self.navigation.turn(Action.RIGHT, angle)
        self.navigation.stop()

    def angle_retrieval(self, action: Action):
        """
            Handler for steering angle prediction according to the given action

        Args:
            action: Action to perform
        """
        angle = 10

        # TODO implement how to handle angle creation here

        return angle