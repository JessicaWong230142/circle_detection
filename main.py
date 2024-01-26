import cv2
import numpy as np

#reads img file in full color
image = cv2.imread('can.jpg', cv2.IMREAD_COLOR)

#processes img by converting to grayscale and blurs 3x3
def image_processing(image):
    grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurring_img = cv2.blur(grayscale_img, (3, 3))
    return blurring_img

#finds circles in the img and draws them
def find_circles(p_image):
    #detects what is considered a circle
    found_circle = cv2.HoughCircles(p_image, cv2.HOUGH_GRADIENT, dp = 1, minDist = 25, param1 = 55, param2 = 30, minRadius = 40, maxRadius = 500)

    #if circle found, rounds midpoint x and y coords and radius
    rounding = np.around(found_circle)
    found_circle = np.uint16(rounding)

    #for every row(circle) the circle detector finds, it assigns the 1st element as x coord, 2nd element as y coord, and 3rd element as radius
    for single_circle in found_circle[0, :]:
        x_center = single_circle[0]
        y_center = single_circle[1]
        radius = single_circle[2]

        #draws the circle and midpoint on the image
        cv2.circle(image, center = (x_center, y_center), radius = 3, color = (240, 207, 137), thickness = 5)
        cv2.circle(image, center = (x_center, y_center), radius = radius, color = (193, 182, 255), thickness = 6)
        cv2.imshow('Circle', image)
        cv2.waitKey(0)

processed_img = image_processing(image)
circle = find_circles(processed_img)
