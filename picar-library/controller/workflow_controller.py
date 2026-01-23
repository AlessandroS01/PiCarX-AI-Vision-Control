import time

import cv2

from vilib import Vilib

from controller.camera_controller import CameraController
from controller.navigation_controller import NavigationController
from status.prediction import Prediction
from vision.vision_system import VisionSystem


class WorkflowController:
    """Controller managing communication between CameraController and NavigationController."""
    def __init__(self):
        self.camera_controller = CameraController()
        self.navigation_controller = NavigationController()
        self.vision_model = VisionSystem()

    def start_workflow(self):
        """
            Controls the whole workflow by getting prediction from CameraController and passing it to
            NavigationController.
        """

        self.camera_controller.start_camera()
        selected_checkpoint = ""



        """ Remove this comments to enable sliding window history functionality """
        # last_predictions_window = [] # track history of last prediction

        """ Remove this comments to enable last frame history functionality """
        last_predicted_checkpoints = None

        while selected_checkpoint not in ["A", "B", "C"]:

            predicted_initial_checkpoints = self.frame_capture_prediction()[0]
            self.checkpoints_printout(predicted_initial_checkpoints)

            selected_checkpoint = input("Select checkpoint to detect (A, B, C): ").upper()
            predicted_checkpoints, frame = self.frame_capture_prediction()

            if selected_checkpoint not in ["A", "B", "C"]:
                print("Invalid selection. Please choose A, B, or C.")

            else:
                try:
                    print("Detection loop started. Press Ctrl+C to stop.")
                    while True:
                        predicted_checkpoints = self.frame_capture_prediction()[0]
                        
                        self.checkpoints_printout(predicted_checkpoints)

                        if selected_checkpoint in [p.class_label for p in predicted_checkpoints]:
                            self.navigation_controller.perform_action(
                                predicted_checkpoints,
                                selected_checkpoint
                            )
                        else:
                            boundary_found = self.vision_model.detect_red_bottom(frame, red_threshold=5000)

                            if boundary_found:
                                print("[Red Detection] Red area detected in bottom region spotted.")
                                self.navigation_controller.boundary_avoidance()

                            print(""
                                  "[Navigation] Selected checkpoint not found in current frame. "
                                  "Using history to navigate."
                            )

                            """self.navigation_controller.perform_on_history(
                                last_predicted_checkpoints,
                                selected_checkpoint
                            )"""

                        # self.sliding_window_manager(last_predictions_window, predicted_checkpoints, size=5)

                        """ Remove this comments to enable sliding window functionality """
                        # last_predictions_window.append(predicted_checkpoints)

                        last_predicted_checkpoints = predicted_checkpoints

                        # time.sleep(1) # Delay between impulses to make the camera stabilize

                except KeyboardInterrupt:
                    print("\nUser stopped execution (Ctrl+C).")

                finally:
                    Vilib.camera_close()
                    print("[Detector] Camera closed.")

    def frame_capture_prediction(self):
        """
            Captures frame from CameraController and gets prediction from VisionSystem.
        """
        frame = self.camera_controller.get_camera_image()
        prediction = self.vision_model.make_prediction(frame)
        return prediction, frame

    def sliding_window_manager(self, window: list, prediction: list[Prediction], size=5):
        """
            Manages a sliding window of predictions to keep track of recent history.

        Args:
            window: Current list of predictions in the sliding window.
            prediction: New prediction to add to the window.
            size: Maximum size of the sliding window.
        Returns:
            Updated sliding window with the new prediction added.
        """
        window.append(prediction)
        if len(window) > size:
            window.pop(0)  # Remove the oldest prediction to maintain the window size
        return window

    def checkpoints_printout(self, predicted_initial_checkpoints: list[Prediction]):
        """
            Prints out the detected checkpoints with their confidence and bounding box.

            Args:
                predicted_initial_checkpoints: List of Prediction objects.
                """
        for prediction in predicted_initial_checkpoints:
            print(f""
                  f"Detected: {prediction.class_label} with confidence {prediction.confidence:.2f}"
                  f" at {prediction.bounding_box}")
