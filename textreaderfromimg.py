import cv2, numpy as np, os, pickle as pk, tkinter as t, pytesseract as pt

pt.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('some.png')          
final_image = cv2.resize(img, (500,500))
print(pt.image_to_string(img))
cv2.imshow('frame', img)
# cv2.imwrite('testtest.png', final_image)
cv2.waitKey(0)
