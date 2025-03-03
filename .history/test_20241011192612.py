import cv2

video = cv2.VideoCapture(0)

run = True

def some(x):
	pass

cv2.namedWindow('canny')
cv2.createTrackbar('1t', 'canny', 0, 600, some)
cv2.createTrackbar('2t', 'canny', 0, 600, some)

while run:

	msg,frame = video.read()
	x         = cv2.getTrackbarPos('1t', 'canny')
	y         = cv2.getTrackbarPos('2t', 'canny')
	cannyvid  = cv2.Canny(frame, x, y)
	cv2.imshow('app',cannyvid)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		run = False
video.release()
cv2.destroyAllWindows()