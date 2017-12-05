import go_turn_stop
import recog_line
import time

# back wheel go to turning point
forward_speed = 10
forward_time =0.5

turn_speed = 10
turn_time1 = 0.5
turn_time2 = 0.1

def go_right() :
    # while back wheel on the line
    go_turn_stop.go_forward(forward_speed)
    time.sleep(forward_time)
    # first 70 turn
    go_turn_stop.right_turn(turn_speed, turn_time1)
    # plus turn
    while recog_line.get_01()[2] != 0:
        go_turn_stop.right_turn(turn_speed, turn_time2)


def go_left() :
    go_turn_stop.go_forward(forward_speed)
    time.sleep(forward_time)

    # this code go remove is OK??
    status = recog_line.get_01()
    print("this is ", status)

    if status == [1, 1, 1, 1, 1]:
        # first 70 turn
        go_turn_stop.left_turn(turn_speed, turn_time1)
        while status[2] != 0:
            # plus turn
            go_turn_stop.left_turn(turn_speed, turn_time2)
    elif status == [1, 1, 0, 1, 1]:
        return

def U_turn() :
    go_turn_stop.go_forward(forward_speed)
    time.sleep(0.5)
    go_turn_stop.right_turn(turn_speed, turn_time1)
    while recog_line.get_01()[2] != 0:
        go_turn_stop.right_turn(turn_speed, turn_time2)
