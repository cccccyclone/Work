#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np



#小车电机引脚定义
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
ServoPin = 4
buzzer = 8

#设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)

#忽略警告信息
GPIO.setwarnings(False)

#电机引脚初始化操作
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    global pwm_servo
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(buzzer,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(ServoPin,GPIO.OUT)
    #设置pwm引脚和频率为2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_servo = GPIO.PWM(ServoPin,50)
    pwm_servo.start(0)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5+10*pos/180)

#小车前进	
def run(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)

#小车后退
def back(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)

#小车左转	
def left(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)

#小车右转
def right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)
#
def spin_left(delaytime):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(20)
    pwm_ENA.ChangeDutyCycle(20)
    time.sleep(delaytime)
    
#小车原地右转
def spin_right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(20)
    pwm_ENB.ChangeDutyCycle(20)
    time.sleep(delaytime)

#小车停止	
def brake(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)

def whistle():
    GPIO.output(buzzer,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(0.001)


def stainDetect(img):
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 230
    params.thresholdStep = 10
    params.minArea = 500
    params.maxArea = 8000
    params.filterByColor = False
    params.filterByConvexity = False
    params.filterByInertia = False

    is_cv3 = cv2.__version__.startswith("3.")
    if is_cv3:
        detector = cv2.SimpleBlobDetector_create(params)
    else:
        detector = cv2.SimpleBlobDetector(params)
    key_points = detector.detect(img)
    return key_points


def snapShot(delay=10,cat=0):
    cap = cv2.VideoCapture(0)
    # 读取摄像头，0表示系统默认摄像头
    while True:
        ret, photo = cap.read()
        # 读取图像
        # cv2.imshow('Please Take Your Photo!!',photo)
        # 将图像传送至窗口

        if delay == 0:
            #如果选择了保存图像
            if cat ==1:
                filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"
                # 以当前时间存储
                cv2.imwrite(filename, photo)
            break
        delay = delay - 1
    return photo

def select(key_points):
    if len(key_points)==0:
        return 0
    L = []
    for item in key_points:
        L.append([int(item.pt[0]),int(item.pt[1]),int(item.size)])


#延时2s	
time.sleep(2)
count = 0
#try/except语句用来检测try语句块中的错误，
#从而让except语句捕获异常信息并处理。
#
#原地右转3s，停止1s。
try:
    while True:
        pass



    # motor_init()
    # whistle()
    # whistle()
    # whistle()
    # servo_appointed_detection(180)
    #run(0.5)
    #back(0.5)
    #spin_left(0.5)
    #spin_right(0.5)
except KeyboardInterrupt:
    pass
pwm_ENA.stop()
pwm_ENB.stop()
pwm_servo.stop()
GPIO.cleanup() 

