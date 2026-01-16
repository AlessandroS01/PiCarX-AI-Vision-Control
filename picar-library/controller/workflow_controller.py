import time

from vilib import Vilib

from controller.camera_controller import CameraController
from controller.navigation_controller import NavigationController
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
        last_prediction = None # track history of last prediction

        while selected_checkpoint not in ["A", "B", "C"]:
            selected_checkpoint = input("Select checkpoint to detect (A, B, C): ").upper()

            if selected_checkpoint not in ["A", "B", "C"]:
                print("Invalid selection. Please choose A, B, or C.")

            else:
                try:
                    print("Detection loop started. Press Ctrl+C to stop.")
                    while True:
                        # Capture frame
                        time.sleep(0.5)  # Small delay to allow camera to stabilize
                        frame = self.camera_controller.get_camera_image()

                        if frame is None:
                            continue

                        # Make prediction from captured frame
                        predicted_checkpoints = self.camera_controller.make_prediction(frame)

                        for prediction in predicted_checkpoints:
                            print(f""
                                  f"Detected: {prediction.class_label} with confidence {prediction.confidence:.2f}"
                                  f" at {prediction.bounding_box}")

                        if selected_checkpoint in [p.class_label for p in predicted_checkpoints]:
                            self.navigation_controller.perform_action(predicted_checkpoints, selected_checkpoint)
                        else:
                            print(""
                                  "[Navigation] Selected checkpoint not found in current frame. "
                                  "Using history to navigate."
                            )
                            self.navigation_controller.perform_on_history(last_prediction, selected_checkpoint)

                        last_prediction = predicted_checkpoints
                except KeyboardInterrupt:
                    print("\nUser stopped execution (Ctrl+C).")

                finally:
                    Vilib.camera_close()
                    print("[Detector] Camera closed.")