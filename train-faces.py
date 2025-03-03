import os, numpy as np, cv2, pickle as pk
from PIL import Image

cur_dir = os.path.dirname(os.path.abspath(__file__))
# cur_file_dir = os.path.join(cur_dir, __file__)
image_dir = os.path.join(cur_dir, 'images')
# print(image_dir)

face_cascade = cv2.CascadeClassifier('cascades\\data\\haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
labels = []
face_list = []
id_face = {}

for maindir, subdirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith('jpg'):
			image_file_path = os.path.join(maindir, file)
			label = os.path.basename(maindir).lower()

			if label not in id_face:
				id_face[label] = current_id
				current_id += 1

			id_ = id_face[label]
			encoded_img = Image.open(image_file_path).convert('L')
			image_array = np.array(encoded_img, 'uint8')
			faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
			for x,y,w,h in faces:
				roi = image_array[y+h : x+w]
				face_list.append(roi)
				labels.append(id_)

# with open('labels.pickle', 'wb') as f:
# 	pk.dump(id_face, f)

# recognizer.train(face_list, np.array(labels))
# recognizer.save('trainer.yml')

print(id_face)
