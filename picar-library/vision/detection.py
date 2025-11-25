import cv2
import numpy as np
import os

from sympy import false
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
        Vilib.display(local=false, web=True)

        detections_output = []  # final return list

        print("Starting Camera... Please wait.")
        Vilib.camera_start(vflip=False, hflip=False)

        # CRITICAL FIX: set local=False to prevent "qt.qpa.xcb" crash
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
                results = self.model(frame, verbose=False)[0]  # verbose=False keeps terminal clean

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

                    # --- VISUALIZATION (Optional) ---
                    # Note: These drawings modify 'frame', but Vilib web stream
                    # usually shows the raw feed. To see these boxes, you would
                    # need to send this specific frame to the web buffer.
                    # For now, we keep the calculation but skip the display.

                    # Print detection to terminal so you know it's working
                    print(f" [!] DETECTED: {label} ({conf:.2f}) at pos: {cx},{cy}")

                detections_output = current_detections

                # --- GUI DISPLAY (DISABLED TO FIX CRASH) ---
                # cv2.imshow("Checkpoint Detection", frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break

        except KeyboardInterrupt:
            print("\nUser stopped execution (Ctrl+C).")

        finally:
            # This block runs whether the code crashes or finishes
            # cv2.destroyAllWindows() # Not needed since we didn't open windows
            Vilib.camera_close()
            print("[Detector] Camera closed.")

        return detections_output