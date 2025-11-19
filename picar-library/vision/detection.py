import cv2
import numpy as np
import os

from ultralytics import YOLO
from vilib import Vilib


class CheckpointDetector:
    """Detects visual checkpoints or letters on track."""

    def __init__(self, model=None):
        base_dir = os.path.dirname(os.path.dirname(__file__))  # goes up from 'vision/' to project root
        model_path = os.path.join(base_dir, "models", "best_yolo_model.pt")

        self.model = YOLO(model_path) if model is None else model

    def detect_checkpoint_frame(self, frame):
        """
        Run YOLO inference on a single frame (numpy image)

        Args:
            frame: The raw image frame from the camera.

        Returns:
            detections: List of detected objects with bounding boxes, confidence, and class IDs.
        """
        results = self.model(frame)[0]

        detections = []
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            detections.append({
                "bbox": (x1, y1, x2, y2),
                "confidence": conf,
                "class_id": cls
            })
        return detections

    def detect_checkpoint_video(self):
        """
        Returns a list of detected checkpoints:
        [ {'label': 'A', 'position': (x, y), 'confidence': 0.9}, ... ]
        """

        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=True, web=True)

        detections_output = []  # final return list

        while True:
            frame = Vilib.picam2.capture_array()

            results = self.model(frame)[0]  # YOLO inference
            current_detections = []

            for box in results.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                # Label from your YOLO class names
                label = self.model.names[cls]

                # Compute center of bounding box (x, y)
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                det = {
                    "label": label,
                    "position": (cx, cy),
                    "confidence": conf
                }
                current_detections.append(det)

                # Draw bounding boxes on video
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            detections_output = current_detections

            # Show real-time preview
            cv2.imshow("Checkpoint Detection", frame)

            # Quit with 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        Vilib.camera_close()

        print("[Detector] Stopping camera.")
        return detections_output