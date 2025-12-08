from vilib import Vilib

from controller.camera_controller import CameraController
from controller.navigation_controller import NavigationController
from utils.checkpoint_selection import choose_element_visual
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

        selected_checkpoint = choose_element_visual()

        if selected_checkpoint == "A" or selected_checkpoint == "B" or selected_checkpoint == "C":

            try:
                print("Detection loop started. Press Ctrl+C to stop.")
                while True:
                    # Capture frame
                    frame = self.camera_controller.get_camera_image()

                    if frame is None:
                        continue

                    # Make prediction from captured frame
                    predicted_checkpoints = self.camera_controller.make_prediction(frame)

                    for prediction in predicted_checkpoints:
                        print(f""
                              f"Detected: {prediction.class_label} with confidence {prediction.confidence:.2f}"
                              f" at {prediction.bounding_box}")


                    #if len(predicted_checkpoints) == 0:
                    #    continue

                    #self.navigation_controller.perform_action(predicted_checkpoints, selected_checkpoint)

            except KeyboardInterrupt:
                print("\nUser stopped execution (Ctrl+C).")

            finally:
                Vilib.camera_close()
                print("[Detector] Camera closed.")
        else:
            print("No valid checkpoint selected. Exiting workflow.")