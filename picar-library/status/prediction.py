class Prediction:
    """Class representing the checkpoint, confidence and position obtained by the vision system."""

    def __init__(self, bounding_box, confidence, class_label):
        """
            Initializes a Prediction object.

        Args:
            bounding_box: Bounding box of the detected checkpoint.
            confidence: Confidence score of the detected checkpoint.
            class_label: Class label of the detected checkpoint.
        """
        self.bounding_box = bounding_box
        self.confidence = confidence
        self.class_label = class_label

    def get_bounding_box(self):
        """ Returns the bounding box of the detected checkpoint. """
        return self.bounding_box
    def get_confidence(self):
        """ Returns the confidence score of the detected checkpoint. """
        return self.confidence
    def get_class_label(self):
        """ Returns the class label of the detected checkpoint. """
        return self.class_label