from ultralytics import YOLO

class YOLOModel:
    """A class to handle YOLO model loading, training and prediction."""

    def __init__(self,
                 model_path='yolov8n.pt',
                 model_path12='yolo12n.pt',
                 epochs: int = 10,
                 batch_size: int = 5):
        """
            Initialize the YOLO models and store models paths

        Args:
        :param model_path: yolov8n model path
        :param model_path12: yolo12n model path
        :param epochs: number of epochs for training
        :param batch_size: batch size for training
        """

        """ UNCOMMENT TO TRAIN MODEL v8n"""
        # self.model8 = YOLO(model_path)
        # self.model8_augmented = YOLO(model_path)

        """ UNCOMMENT TO USE DIFFERENT DATASETS """
        # self.data_path_normal = 'models/datasets/yolo_dataset/data.yaml'
        # self.data_path_augmented = 'models/datasets/augmented_noised_yolo_dataset/data.yaml'

        self.model12 = YOLO(model_path12)
        self.data_path_final = 'models/datasets/final_augmented_dataset/yolo/data.yaml'
        self.epochs = epochs
        self.batch_size = batch_size

    def run_training_final_dataset(self):
        """
          Train self.model12 using the final yolo dataset
        """
        print("\n--- Starting YOLOv12n Training ---")
        self.model12.train(
            data=self.data_path_final,
            epochs=self.epochs,
            imgsz=640,
            batch=self.batch_size,
            name='yolov12n-final-model'
        )
        print("--- YOLOv8 Training Complete ---")