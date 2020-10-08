# -*- coding: utf-8 -*-


# !pip install face_recognition pillow

from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import face_recognition
import cv2

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("media/sample.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    right_eye=face_landmarks["right_eye"]
    left_eye=face_landmarks["left_eye"]
    
    right_max=[0,0]
    right_min=[float('inf'),float('inf')]
    for x,y in right_eye:
        if x>right_max[0]:
          right_max[0]=x
        if x<right_min[0]:
          right_min[0]=x

        if y>right_max[1]:
          right_max[1]=y
        if y<right_min[1]:
          right_min[1]=y

    left_max=[0,0]
    left_min=[float('inf'),float('inf')]

    for x,y in left_eye:
        if x>left_max[0]:
          left_max[0]=x
        if x<left_min[0]:
          left_min[0]=x

        if y>left_max[1]:
          left_max[1]=y
        if y<left_min[1]:
          left_min[1]=y

# Show the picture

plt.rcParams["figure.figsize"] = (16,16)
plt.imshow(image)

left_eye = image[left_min[1]:left_max[1],left_min[0]:left_max[0]]
plt.imshow(left_eye)
plt.savefig('media/left.jpg',bbox_inches='tight')

right_eye = image[right_min[1]:right_max[1],right_min[0]:right_max[0]]
plt.imshow(right_eye)
plt.savefig('media/right.jpg',bbox_inches='tight')