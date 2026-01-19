from controller.workflow_controller import WorkflowController

"""def movement_test():
    move = Movement()
    move.forward()
    time.sleep(1)
    move.forward()
    time.sleep(1)
    move.turn(Action.LEFT, 30)
    time.sleep(1)
    move.turn(Action.RIGHT, 30)
    time.sleep(1)
    move.stop()
    time.sleep(1)
    move.backward()
    time.sleep(1)
    move.stop()
"""

if __name__=="__main__":
    start = WorkflowController()
    start.start_workflow()



