from time import sleep

import RPi.GPIO as GPIO
from ultraModule import getDistance 
GPIO.setmode(GPIO.BOARD)



MotorLeft_A = 11 
MotorLeft_B = 12
MotorLeft_PWM = 35

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

GPIO.output(MotorLeft_A, GPIO.HIGH)
GPIO.output(MotorLeft_B, GPIO.LOW)
GPIO.output(MotorLeft_PWM, GPIO.HIGH)

GPIO.output(MotorRight_A, GPIO.HIGH)
GPIO.output(MotorRight_B, GPIO.LOW)
GPIO.output(MotorRight_PWM, GPIO.HIGH)

LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)

# sensor init
leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)


# core code
def go(leftSpeed, rightSpeed):
    LeftPwm.start(leftSpeed*2)
    RightPwm.start(rightSpeed*2)
#     sleep(0.0001)


def stop():
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)

def go_forward(speed, running_time):
    global forward0, forward1
    motor.setSpeed(speed)
    motor.motor0(forward0)
    motor.motor1(forward1)
    time.sleep(running_time)
    motor.stop()

def rightPointTurn(speed):  # student assignment (1)

    leftmotor(backward0)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)

    rightmotor(forward0)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)


def leftPointTurn(speed):  # student assignment (2)

    leftmotor(forward0)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    rightmotor(backward0)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)

dis = 20 
SwingPr = 42
SwingTr = 1.0 * 1.47

PointPr = 37
PointTr = 0.8 * 1.9
result = [
    ['01111', 19, 0],
    ['00111', 19, 4],
    ['00011', 19, 6],
    ['10111', 19, 8],
    ['10011', 19, 10],
    ['11110', 0, 20],


    ['11100', 4, 19],
    ['11000', 6, 19],
    ['11101', 8, 19],
    ['11001', 10, 19],
    ['11011', 22, 22],
    ['10001', 22, 22]
    ['00000', 0, 0]
]

try:
    while True:
        sensor = [
            str(GPIO.input(leftmostled)),
            str(GPIO.input(leftlessled)),
            str(GPIO.input(centerled)),
            str(GPIO.input(rightlessled)),
            str(GPIO.input(rightmostled))
        ]

        print(sensor)

        inputStream = "".join(sensor)

        for idx in range(len(result)):
            if inputStream == '11111':
                while inputStream != '01111':
                    go(0, 20)
            elif inputStream == '11000':
                while inputStream != '11110':
                    go(20, 0)
            else:
                inputStream == result[idx][0]
                print(result[idx])
                go(result[idx][2], result[idx][1])
                break
                pass
            pass

         
#         stop()
#         sleep(2)

except KeyboardInterrupt:
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()
