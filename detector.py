import cv2

framev = cv2.VideoCapture(0)

casc = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
casceye = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

cascsmile = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')


run = True

while run:
	msg,frame = framev.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cascmain = casc.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=5)
	eyes = casceye.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=20)
	smile = cascsmile.detectMultiScale(frame, scaleFactor=1.5,minNeighbors=40)

	for (x,y,w,h) in cascmain:
		cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,0,0), 3)
	for (x,y,w,h) in eyes:
		cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,0,0), 3)
	for (x,y,w,h) in smile:
		cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (0,0,0), 3)

	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		run = False

framev.release()
cv2.destroyAllWindows()