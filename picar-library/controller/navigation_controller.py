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
        self.navigation.perform_action(predictions, selected_checkpoint)

    def perform_on_history(self, last_prediction: list[Prediction], selected_checkpoint: str):
        """ Takes the last prediction and performs a "random" search if the checkpoint is not found in the current frame
        Args:
            last_prediction: The last captured prediction from the camera.
            selected_checkpoint: The checkpoint the user has selected to find.
        """

        if selected_checkpoint in [p.class_label for p in last_prediction]:
            self.navigation.turning_on_history(last_prediction, selected_checkpoint)
        else:
            self.navigation.turning_randomly()