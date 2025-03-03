import cv2, numpy as np, os, pickle as pk
from PIL import Image

cur_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(cur_dir, 'images')
face_cascade = cv2.CascadeClassifier('cascades\\data\\haarcascade_frontalface_alt2.xml')
trainer = cv2.face.LBPHFaceRecognizer_create()

ids = []
id_face = {}
cur_id = 0
face_list = []

for maindir, subdirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith('jpg'):
			images_path = os.path.join(maindir, file)
			# print(images_path)
			label = os.path.basename(maindir).replace(' ', '-').lower()
			if label not in id_face:
				id_face[label] = cur_id
				cur_id += 1
			_id = id_face[label]
			images_encoded = Image.open(images_path).convert('L')
			final_images = images_encoded.resize((600,600), Image.ANTIALIAS)
			numpy_images = np.array(images_encoded, 'uint8')
			print(numpy_images.shape)
			faces = face_cascade.detectMultiScale(numpy_images,
				scaleFactor=1.5, minNeighbors=5)
			for x,y,w,h in faces:
				face = numpy_images[y+h : x+w]
				face_list.append(face)
				ids.append(_id)

with open('labels.pickle', 'wb') as f:
	pk.dump(id_face, f)

print(os.path.exists(images_path))

trainer.train(face_list, np.array(ids))
trainer.save('trainer.yml')
