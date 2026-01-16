from navigation.navigation import Navigation
from status.prediction import Prediction


class NavigationController:
    """Controller for managing navigation"""
    def __init__(self):
        self.navigation = Navigation()

    def perform_action(self, predictions: list[Prediction], selected_checkpoint: str):
        """ Takes a prediction and passes it to the navigation system to perform the correspondent action
        Args:
            predictions: List of prediction checkpoints containing bounding box, confidence and label.
            selected_checkpoint: The checkpoint the user has selected to find.
        """
        #self.navigation.perform_action(predictions, selected_checkpoint)
        self.navigation.rotate()