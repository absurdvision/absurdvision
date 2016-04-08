import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_low', 'image', 0, 255, nothing)
cv2.createTrackbar('S_low', 'image', 0, 255, nothing)
cv2.createTrackbar('V_low', 'image', 0, 255, nothing)
cv2.createTrackbar('H_high', 'image', 0, 255, nothing)
cv2.createTrackbar('S_high', 'image', 0, 255, nothing)
cv2.createTrackbar('V_high', 'image', 0, 255, nothing)


while (1):

	# get current positions of four trackbars
	hmin = cv2.getTrackbarPos('H_low', 'image')
	smin = cv2.getTrackbarPos('S_low', 'image')
	vmin = cv2.getTrackbarPos('V_low', 'image')
	hmax = cv2.getTrackbarPos('H_high', 'image')
	smax = cv2.getTrackbarPos('S_high', 'image')
	vmax = cv2.getTrackbarPos('V_high', 'image')

	# define range of blue color in HSV
	lower_hsv = np.array([hmin, smin, vmin])
	upper_hsv = np.array([hmax, smax, vmax])

	# Capture frame-by-frame
	ret, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)

	cv2.imshow('image', mask)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
