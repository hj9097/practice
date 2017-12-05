# =======================================================================
# import GPIO library and time module
# =======================================================================

import RPi.GPIO as GPIO
import time

# ======================================================================
# import setup to get pins and True or False
# The motor set to go
# The import motor module to move
# ======================================================================
import setup

# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward without any limitation of running_time
# =======================================================================

def go_forward(speed):

    setup.leftmotor(setup.forward0)
    setup.rightmotor(setup.forward0)
    setup.Left_Pwm.ChangeDutyCycle(speed)
    setup.Right_Pwm.ChangeDutyCycle(speed)

# =======================================================================
# define the stop module
# =======================================================================

def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(setup.Motor_Left_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(setup.Motor_Right_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    setup.Left_Pwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    setup.Right_Pwm.ChangeDutyCycle(0)


def pwm_setup():
    # left and right motor pwm will set 0 to be stable
    setup.Left_Pwm.start(0)
    setup.Right_Pwm.start(0)

# if there is unexpected occurrence
def pwm_low():
    stop()
    GPIO.cleanup()

# =======================================================================
# perform right swing turn of 90 degree
# =======================================================================
def right_turn(speed, running_time):

    setup.leftmotor(setup.forward0)
    GPIO.output(setup.Motor_Left_PWM,GPIO.HIGH)
    GPIO.output(setup.Motor_Right_PWM,GPIO.LOW)
    setup.Left_Pwm.ChangeDutyCycle(speed)
    setup.Right_Pwm.ChangeDutyCycle(0)
    time.sleep(running_time)


def right_turn2(speed, running_time):

    setup.leftmotor(setup.forward0)
    GPIO.output(setup.Motor_Left_PWM,GPIO.HIGH)
    setup.rightmotor(setup.backward0)
    GPIO.output(setup.Motor_Right_PWM,GPIO.LOW)
    setup.Left_Pwm.ChangeDutyCycle(speed)
    setup.Right_Pwm.ChangeDutyCycle(speed)
    time.sleep(running_time)


# =======================================================================
# perform left swing turn of 90 degree
# =======================================================================
def left_turn(speed, running_time):

    setup.rightmotor(setup.forward0)
    GPIO.output(setup.Motor_Right_PWM,GPIO.HIGH)
    GPIO.output(setup.Motor_Left_PWM,GPIO.LOW)
    setup.Right_Pwm.ChangeDutyCycle(speed)
    setup.Left_Pwm.ChangeDutyCycle(0)
    time.sleep(running_time)


