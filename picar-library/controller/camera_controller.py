from hardware.camera import Camera
from status.prediction import Prediction
from vision.vision_system import VisionSystem

class CameraController:
    """Controller for managing camera in PiCarX-AI-vision-Control."""
    def __init__(self):
        self.camera = Camera()
        self.vision = VisionSystem()

    def start_camera(self):
        """Start the camera."""
        self.camera.start_camera()

    def get_camera_image(self):
        """
        Capture a real time image from the camera.

        Returns:
            frame: The captured image frame.
        """
        return self.camera.get_frame()

    def make_prediction(self, frame) -> list[Prediction]:
        """
            Passes a frame to the vision system as input to the model.

        Args:
            frame: The raw image frame from the camera.

        Returns:
            prediction: List of Prediction objects each containing checkpoint class, confidence and position.
        """

        return self.vision.make_prediction(frame)