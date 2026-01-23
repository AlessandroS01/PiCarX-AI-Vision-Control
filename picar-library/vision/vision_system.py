from status.prediction import Prediction
from vision.detection import CheckpointDetector
import cv2
import numpy as np

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

    def detect_red_bottom(frame, roi_height_ratio=0.4, threshold=50):
        """
    Detect red color only in the bottom region of the frame.

    Args:
        frame (numpy array): BGR image from PiCar-X camera
        roi_height_ratio (float): fraction of image height used as road area
        threshold (int): sensitivity threshold for red detection

    Returns:
        red_mask (numpy array): binary mask of detected red area
        red_detected (bool): True if red is detected in road area
    """

        height, width, _ = [640, 480]

    # Define bottom ROI
        roi_start = int(height * (1 - roi_height_ratio))
        roi = frame[roi_start:height, 0:width]
   
    # Split channels
        b, g, r = cv2.split(roi)

    # Convert ROI to grayscale
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Enhance red regions
        red_emphasis = cv2.subtract(gray, b)

    # Threshold
        _, red_mask = cv2.threshold(
        red_emphasis, threshold, 255, cv2.THRESH_BINARY_INV
    )

    # Remove noise
        kernel = np.ones((5,5), np.uint8)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)

    # Decision: is red present?
        red_pixel_count = cv2.countNonZero(red_mask)
        red_detected = red_pixel_count > 300   # tune for  camera

        return red_mask, red_detected
