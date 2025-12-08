import os

import cv2
from ultralytics import YOLO
from vilib import Vilib

from status.prediction import Prediction


class CheckpointDetector:
    """Detects visual checkpoints or letters on track."""

    def __init__(self, model=None):
        """ Initialize the CheckpointDetector with the trained YOLO model. """
        base_dir = os.path.dirname(os.path.dirname(__file__))  # goes up from 'vision/' to project root
        model_path_v8n = os.path.join(base_dir, "models", "best_v8n.pt")
        model_path_v12n = os.path.join(base_dir, "models", "best_v12n.pt")

        self.model_v8n = YOLO(model_path_v8n) if model is None else model
        self.model_v12n = YOLO(model_path_v12n) if model is None else model

    def detect_checkpoint_frame(self, frame) -> list[Prediction]:
        """
        Run YOLO inference on a single frame (numpy image)

        Args:
            frame: The raw image frame from the camera.

        Returns:
            detections: List of detected objects with bounding boxes, confidence, and class label.
        """
        results = self.model_v12n(frame, verbose=False)[0]

        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])

            if conf <= 0.6:
                continue  # Skip low-confidence detections

            cls = int(box.cls[0])
            label = self.model_v12n.names[cls]

            predicted_checkpoint = Prediction(
                bounding_box=(x1, y1, x2, y2),
                confidence=conf,
                class_label=label
            )

            detections.append(predicted_checkpoint)
        return detections

    def detect_save_checkpoints_video(self):
        """
        DEPRECATED. Use only while debugging the model.

        Returns a list of detected checkpoints:
        [ {'label': 'A', 'position': (x, y), 'confidence': 0.9}, ... ]
        """

        i = 0

        print("Starting Camera... Please wait.")
        Vilib.camera_start(vflip=True, hflip=False)
        Vilib.display(local=False, web=True)

        detections_output = []

        try:
            print("Detection loop started. Press Ctrl+C to stop.")
            while True:
                # Capture frame
                frame = Vilib.picam2.capture_array()

                if frame is None:
                    continue

                # Run YOLO inference
                results = self.model_v8n(frame, verbose=False)[0]

                current_detections = []

                for box in results.boxes:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])

                    # Label from your YOLO class names
                    label = self.model_v8n.names[cls]

                    # Draw bounding boxes on the 'frame' variable
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                    # Compute center of bounding box (x, y)
                    cx = int((x1 + x2) / 2)
                    cy = int((y1 + y2) / 2)

                    det = {
                        "label": label,
                        "position": (cx, cy),
                        "confidence": conf
                    }
                    current_detections.append(det)

                    # Print detection to terminal so you know it's working
                    print(f" [!] DETECTED: {label} ({conf:.2f}) at pos: {cx},{cy}")

                # Update the Vilib web buffer with the frame just drew on.
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                Vilib.img = frame_rgb
                cv2.imwrite(f"bounding_boxes_frames/2nd_attempt/debug_detection{i}.jpg", frame)
                i += 1

                detections_output = current_detections

        except KeyboardInterrupt:
            print("\nUser stopped execution (Ctrl+C).")

        finally:
            Vilib.camera_close()
            print("[Detector] Camera closed.")

        return detections_output