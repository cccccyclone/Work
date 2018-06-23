import cv2  
import time  
  
# cap=cv2.VideoCapture(0)
# #读取摄像头，0表示系统默认摄像头
#
# while True:
#     ret,photo=cap.read()
#     #读取图像
#     cv2.imshow('Please Take Your Photo!!',photo)
#     #将图像传送至窗口
#
#     key=cv2.waitKey(2)
#     #设置等待时间，若数字为0则图像定格
#
#     if key==ord(" "):
#     #按空格获取图像
#         filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"
#         #以当前时间存储
#         cv2.imwrite(filename,photo)
#         #保存位置
#
#     if key==ord("q"):
#     #按“q”退出程序
#         break

import cv2
import time

def snapShot(delay=10):
    cap = cv2.VideoCapture(0)
    # 读取摄像头，0表示系统默认摄像头
    while True:
        ret, photo = cap.read()
        # 读取图像
        # cv2.imshow('Please Take Your Photo!!',photo)
        # 将图像传送至窗口

        if delay == 0:
            # 按空格获取图像
            filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"
            # 以当前时间存储
            cv2.imwrite(filename, photo)
            # 保存位置
            break
        delay = delay - 1

if __name__ == '__main__':          #运行
    snapShot()