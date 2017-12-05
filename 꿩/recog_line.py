
# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
#  leftL2    leftL1     center     rightL1     rightL2
#   16         18         22         40           32
# =======================================================================

leftL2 = 16 #1
leftL1 = 18 #2
centerL = 22 #3
rightL1 = 40 #4
rightL2 = 32 #5

#========================================================================
# setup - senser
#========================================================================

GPIO.setup(leftL2, GPIO.IN)
GPIO.setup(leftL1, GPIO.IN)
GPIO.setup(centerL, GPIO.IN)
GPIO.setup(rightL1, GPIO.IN)
GPIO.setup(rightL2, GPIO.IN)

#========================================================================
# L2     L1    Center    R1    R2
#========================================================================
def get_01():
    L2 = GPIO.input(leftL2)
    L1 = GPIO.input(leftL1)
    Center = GPIO.input(centerL)
    R1 = GPIO.input(rightL1)
    R2 = GPIO.input(rightL2)

    led_list = [L2, L1, Center, R1, R2]
    return led_list

inLine = [[1,1,0,1,1], [1,0,0,1,1], [1,1,0,0,1]]
left = [[0,1,1,1,1], [0,0,1,1,1],[1,0,1,1,1]]
right = [[1,1,1,1,0], [1,1,1,0,0],[1,1,1,0,1]]
rightTurn = [[0,0,0,0,0], [1,1,0,0,0], [1,0,0,0,0]]

def line_status(led_list) :
    # 3
    if led_list in inLine:
        status = "inLine"
    # 2,2
    elif led_list in left :
        status = "left"
    elif led_list in right :
        status ="right"
    # 2
    elif led_list in rightTurn :
        status = "right turn"
    # 1
    elif led_list == [0,0,0,1,1] :
        status = "left or straight"
    # 1
    elif led_list == [1,1,1,1,1] :
        status = "Uturn"

    else:
        status = "???"
    return status
