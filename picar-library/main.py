#from hardware.movement import Movement
from models.yolo import YOLOModel
import ctypes

#from status.action import Action

if __name__=="__main__":
    # Code for testing the Movement class
    """move = Movement()

    move.forward()
    move.forward()
    move.turn(Action.LEFT, 30)
    move.turn(Action.RIGHT, 30)
    move.stop()
    move.backward()
    move.stop()"""

    # Code for testing the model
    trainer = YOLOModel()
    trainer.run_training()

    # 3. Check the performance of the models you just trained
    print("\nTraining finished. Now checking performance...")
    trainer.check_performance()

    print("\nProcess complete.")
    print("Your trained models (best.pt) and all charts (results.png)")
    print("are saved in the 'runs/detect/' directory.")

