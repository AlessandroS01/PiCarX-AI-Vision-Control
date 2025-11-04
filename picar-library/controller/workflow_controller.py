from controller.camera_controller import CameraController
from controller.navigation_controller import NavigationController


class WorkflowController:
    """Controller managing communication between CameraController and NavigationController."""
    def __init__(self):
        self.camera_controller = CameraController()
        self.navigation_controller = NavigationController()

    def start_workflow(self):
        """Start the workflow by getting predicted action from CameraController and passing it to NavigationController."""
        predicted_action = self.camera_controller.predict_action()
        # TODO Can integrate action control manager for navigation controller input (IF-SWITCH etc...)
        self.navigation_controller.perform_action(predicted_action)