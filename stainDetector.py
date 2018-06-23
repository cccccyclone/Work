import cv2
import numpy as np
from matplotlib import pyplot as plt
def round2(data):
    result = []
    for member in data:
        r = []
        for temp in member:
            r.append(int(temp))
        result.append(r)
    return result

def stainDetect(img):
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.maxThreshold = 220
    params.thresholdStep = 10
    params.minArea = 500
    params.maxArea = 8000
    params.filterByColor = False
    params.filterByConvexity = False
    params.filterByInertia = False
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("img", img)
    # plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    is_cv3 = cv2.__version__.startswith("3.")
    if is_cv3:
        detector = cv2.SimpleBlobDetector_create(params)
    else:
        detector = cv2.SimpleBlobDetector(params)
    key_points = detector.detect(img)
    column = img.shape[0]
    row = img.shape[1]
    center_column = column-1
    center_row = row/2
    #print(row,column)
    newKeyPoints = []
    for item in key_points:
        x = int(item.pt[0])
        y = int(item.pt[1])
        print(img[y][x])
        print(x,y,int(item.size))
        #if img[y][x]<220:
        newKeyPoints.append(item)

    output_img = cv2.drawKeypoints(img, newKeyPoints,np.array([]),  (0, 0, 255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("output_img", output_img)
    cv2.waitKey(0)


# print(sum(img[216][155])/3)
# print(sum(img[160][196])/3)
# print(sum(img[106][234])/3)
#
# for item in key_points:
#     x = int(item.pt[0])
#     y = int(item.pt[1])
#     print(x,y,int(item.size),int(sum(img[x][y])/3))

if  __name__ == '__main__' :
    img = cv2.imread("test0.jpg")
    stainDetect(img)
