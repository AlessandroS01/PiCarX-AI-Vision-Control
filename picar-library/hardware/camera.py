from vilib import Vilib


class Camera:
    """Camera hardware interface."""

    def __init__(self, resolution=(640, 480)):
        """ Initialize the camera with the specified resolution. """
        self.resolution = resolution

    def start_camera(self):
        """Start the camera with specified resolution."""
        Vilib.camera_start(vflip=False, hflip=True)
        Vilib.display(local=False, web=True)

    def get_frame(self):
        """Capture a single frame from the camera.
        Returns:
            frame: The captured image frame.
        """
        frame = Vilib.picam2.capture_array()
        return frame