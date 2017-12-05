import maze_move
# go_right()  go_left()  U_turn()
import go_turn_stop
# go_forward(speed)  stop()  pwm_setup()  right_turn(speed, running_time)  left_turn(speed, running_time)
import setup
# rightmotor(forward)  leftmotor(forward)
import recog_line
# get_01()  line_status(led_list)
import time
# sleep(time)


status = recog_line.get_01()
speed = 50
# little time
turn_time = 0.5
try:
    while True :
        line = recog_line.line_status(status)
        print(line)

        if line == "inLine":
            go_turn_stop.go_forward(speed)

        elif line == "right" :
            go_turn_stop.right_turn(speed, turn_time)
        elif line == "left" :
            go_turn_stop.left_turn(speed, turn_time)

        elif line == "Uturn":
            maze_move.U_turn()

        elif line == "right turn" :
            maze_move.go_right()

        elif line == "left or straight" :
            maze_move.go_left()
        else:
            pass
        
except :
    go_turn_stop.pwm_low()
