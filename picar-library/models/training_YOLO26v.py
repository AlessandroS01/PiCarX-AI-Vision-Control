from ultralytics import YOLO
from pathlib import Path


class YOLOModel:
    """A class to handle YOLO model loading, training and prediction."""

    def __init__(self,
                 model_path='yolov8n.pt',
                 model_path26='yolo26n.pt',
                
                 epochs: int = 200,           # ↑ from 10
                 batch_size: int = 16,        # ↑ from 5  

                 lr0: float= 0.01,
                 lrf:  float=0.01,
                 momentum:  float=0.937,
                 weight_decay:  float=0.0005,
                 warmup_epochs:  float=3.0,
                 warmup_momentum: float=0.8,
                 box:  float=7.5,
                 cls:  float=0.5,
                 dfl:  float=1.5,
hsv_h:  float=0.015,
hsv_s:  float=0.7,
hsv_v:  float=0.4,
degrees:  float=0.0,
translate:  float=0.1,
scale:  float=0.5,
shear:  float=0.0,
perspective:  float=0.0,
flipud:  float=0.0,
fliplr:  float=0.5,
bgr:  float=0.0,
mosaic:  float=1.0,
mixup:  float=0.0,
cutmix:  float=0.0,
copy_paste: float=0.0,
close_mosaic: int=10,
patience: int = 30,          # Early stopping patience
save_period: int = 20,       # Save every 20 epochs
device: str = 'cpu'         
             

):
        """
            Initialize the YOLO models and store models paths

        Args:
        :param model_path: yolov8n model path
        :param model_path26: yolo26n model path
        :param epochs: number of epochs for training
        :param batch_size: batch size for training
        """

        """ UNCOMMENT TO TRAIN MODEL v8n"""
        # self.model8 = YOLO(model_path)
        # self.model8_augmented = YOLO(model_path)

        """ UNCOMMENT TO USE DIFFERENT DATASETS """
        # self.data_path_normal = 'models/datasets/yolo_dataset/data.yaml'
        # self.data_path_augmented = 'models/datasets/augmented_noised_yolo_dataset/data.yaml'
        
        self.model26 = YOLO(model_path26)
        self.data_path_final = r"picar-library\models\datasets\final_augmented_dataset\yolo\data.yaml"
        print("CWD =", Path().absolute())
        print("data path =", self.data_path_final)
        print("exists? =", Path(self.data_path_final).exists())
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr0 = lr0
        self.lrf = lrf  
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.warmup_epochs = warmup_epochs
        self.warmup_momentum = warmup_momentum
        self.box = box
        self.cls = cls
        self.dfl = dfl
        self.hsv_h = hsv_h
        self.hsv_s = hsv_s
        self.hsv_v = hsv_v
        self.degrees = degrees
        self.translate = translate
        self.scale = scale
        self.shear = shear
        self.perspective = perspective
        self.flipud = flipud
        self.fliplr = fliplr
        self.bgr = bgr
        self.mosaic = mosaic
        self.mixup = mixup
        self.cutmix = cutmix
        self.copy_paste = copy_paste
        self.close_mosaic = close_mosaic
        self.patience = patience
        self.save_period = save_period
        self.device = device


    def run_training_final_dataset(self):
        """
          Train self.model26 using the final yolo dataset
        """
        print("\n--- Starting YOLOv26n Training ---")
        
        self.model26.train(
    data=self.data_path_final,
    epochs=self.epochs,
    imgsz=640,
    batch=self.batch_size,
    lr0=self.lr0,
    lrf=self.lrf,
    momentum=self.momentum,
    weight_decay=self.weight_decay,
    warmup_epochs=self.warmup_epochs,
    warmup_momentum=self.warmup_momentum,
    box=self.box,
    cls=self.cls,
    dfl=self.dfl,
    hsv_h=self.hsv_h,
    hsv_s=self.hsv_s,
    hsv_v=self.hsv_v,
    degrees=self.degrees,
    translate=self.translate,
    scale=self.scale,
    shear=self.shear,
    perspective=self.perspective,
    flipud=self.flipud,
    fliplr=self.fliplr,
    bgr=self.bgr,
    mosaic=self.mosaic,
    mixup=self.mixup,
    cutmix=self.cutmix,
    copy_paste=self.copy_paste,
    close_mosaic=self.close_mosaic,
    patience=self.patience,          # NEW: early stopping
    save_period=self.save_period,    # NEW: regular saves
    device=self.device,              # NEW: explicit device
)

        print("--- YOLOv8 Training Complete ---")
if __name__ == "__main__":
    yolo_model = YOLOModel()
    yolo_model.run_training_final_dataset()
