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

    def detect_red_bottom(self,frame, roi_height_ratio=0.4, threshold=50):
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

    # Define bottom ROI
        #roi_start = int(height * (1 - roi_height_ratio))
        roi = frame[340:480, 0:640]
   
    # Split channels
        b, g, r = cv2.split(roi)

    # Convert ROI to grayscale
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # Red must be dominant
        red_dominant = (r > 120) & (r > g + 30) & (r > b + 30)

    # Grayscale constraint (avoid dark road)
        bright_enough = gray > 80

    # Final red mask
        red_mask = np.zeros_like(gray, dtype=np.uint8)
        red_mask[red_dominant & bright_enough] = 255

    # Clean noise
        kernel = np.ones((5, 5), np.uint8)
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)

        red_pixel_count = cv2.countNonZero(red_mask)
        print("Red pixels:", red_pixel_count)

        red_detected = red_pixel_count > 800  # realistic threshold

        return red_mask, red_detected
    
