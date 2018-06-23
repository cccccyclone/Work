# -*- coding: UTF-8 -*-

import numpy as np
import cv2
# -*- coding: utf-8 -*-
import cv2

img= cv2.imread("20180602-230646.jpg")
img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#标准鼠标交互函数
def onmouse(event, x, y, flags, param):
    # 当鼠标移动时
    if event==cv2.EVENT_MOUSEMOVE:
        print(x,y,img[x,y])

def pixelDetect():
    cv2.namedWindow("img")
    cv2.setMouseCallback("img", onmouse)
    while True:
        cv2.imshow("img",img)
        # 按下‘q'键，退出
        if cv2.waitKey() == ord('q'):
            break
        cv2.destroyAllWindows()

if __name__ == '__main__':          #运行
    pixelDetect()