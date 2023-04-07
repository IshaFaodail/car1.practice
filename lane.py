import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(lane_image) :
    gray = cv2.cvtColor(lane_image,cv2.COLOR_BGR2GRAY )
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_intrest(lane_image) :
    height = lane_image.shape[0]
    triangle = np.array([[(200,height), (1100,height),(550,250)]])
    mask = np.zeros_like(lane_image)
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(mask, lane_image)
    return masked_image

def line_display(image, lines):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(image, (x1, y1),(x2, y2), (255, 0, 0), 10)
    return image





frame = cv2.imread('test_image.jpg')
lane_image = np.copy(frame)
canny = canny(lane_image)
region = region_of_intrest(canny)
line = cv2.HoughLinesP(region, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap= 5 )
display = line_display(lane_image, line)

cv2.imshow("road",display )
cv2.waitKey(0)