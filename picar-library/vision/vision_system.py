from status.prediction import Prediction
from vision.detection import CheckpointDetector


class VisionSystem:
    """Top-level vision controller that integrates capture and detection."""

    def __init__(self):
        self.checkpoint_detector = CheckpointDetector()

    def make_prediction(self, frame) -> list[Prediction] :
        """
            Feed the raw frame to the model.

        Args:
            frame: The raw image frame from the camera.

        Returns:
            List of prediction objects containing bounding box, confidence and class id.
        """
        return self.checkpoint_detector.detect_checkpoint_frame(frame)

    def detect_tape(self):
        pass
        # TODO  Implement tape detection method
