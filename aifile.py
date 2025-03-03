import webbrowser, cv2, numpy as np, tkinter as t, pickle as pk
# webbrowser.open('C:\\Windows\\system32\\cmd.exe')

framevid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
face_detect = False
labels = {}

with open('labels.pickle', 'rb') as f:
	get_labels = pk.load(f)
	labels = {v:k for k,v in get_labels.items()}

def seen(x,y,w,h):
	string = False
	if x and y and w and h:
		string = True
	return string

run = True

color = (0,255,0)

thick = 3

while run:
	msg, frame = framevid.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	id_, conf = recognizer.predict(gray)
	for (x,y,w,h) in faces:                                                                                                                                                                                                                                                                                                                   
		roi = frame[y:y+h, x:x+w]
		cv2.rectangle(frame, (x,y) , (x + w,y + h), color, thick)
		# cv2.putext(labels[id_], )
		if conf >= 45 and conf <= 85:
			cv2.putText(frame, labels[id_], (x+60,y-10), cv2.FONT_HERSHEY_COMPLEX,
			 1,(255,0,0), 2, cv2.LINE_AA)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		run = False
framevid.release()
cv2.destroyAllWindows()
