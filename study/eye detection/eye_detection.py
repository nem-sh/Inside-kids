# -*- coding: utf-8 -*-


# !pip install face_recognition pillow

from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import face_recognition
import cv2

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("/gdrive/My Drive/colab/test3.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    # for facial_feature in face_landmarks.keys():
    #     print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
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
          


print(left_max,left_min,right_max,right_min)

# Show the picture

plt.rcParams["figure.figsize"] = (16,16)
plt.imshow(image)
plt.show()

left_eye = image[left_min[1]:left_max[1],left_min[0]:left_max[0]]
plt.imshow(left_eye)

right_eye = image[right_min[1]:right_max[1],right_min[0]:right_max[0]]
plt.imshow(right_eye)

right_eye = image[right_min[1]:right_max[1],right_min[0]:right_max[0]]
plt.imshow(right_eye)

left_eye = image[left_min[1]:left_max[1],left_min[0]:left_max[0]]
plt.imshow(left_eye)