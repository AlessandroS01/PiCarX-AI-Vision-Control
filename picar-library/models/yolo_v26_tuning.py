from ultralytics import YOLO
import yaml

model = YOLO('yolo26n.pt')

# YOLO  built-in hyperparameter tuning 
model.tune(
    data='models/datasets/final_augmented_dataset/yolo/data.yaml',
    epochs=30,
    iterations=100,  # Number of tuning iterations
    optimizer='AdamW',
    plots=False,
    save=False,
    val=False
)

with open('runs/detect/tune/best_hyperparameters.yaml', 'r') as f:
    best_params = yaml.safe_load(f)

print(best_params)
