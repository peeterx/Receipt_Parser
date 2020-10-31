import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract

filenames = os.listdir('D:/images/')
print(filenames)

img = cv2.imread("D:/images/example.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fig = plt.figure(figsize=[10, 10])
height, width, channel = img.shape
plt.imshow(img)

print(type(img))
print(height, width, channel)

text = pytesseract.image_to_string(img)
print(text)

file = open('examplePNG.txt', 'a')
file.write(text)
file.close()
