import cv2
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import face_recognition


def get():
    vidcap = cv2.VideoCapture('media/video')

    count = 0
    return_data = {
        "true":0,
        "lie":0,
        "nature":0,
    }
    while True:
        ret, image = vidcap.read()
        if not ret:
            break
        if(int(vidcap.get(1)) % 20 == 0):
            print('Saved frame number : ' + str(int(vidcap.get(1))))
            path = "media/images/tmp_frame.jpg"
            cv2.imwrite(path, image)
            eye_detection(path,'tmp_eye')            
            print('Analyzed frame%d' % count)
            count += 1
    
    vidcap.release()
    return return_data

def eye_detection(img_path,file_name):
    image = face_recognition.load_image_file(img_path)

    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    if len(face_landmarks_list) != 1:
        return -1
    print('eye_detect')
    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for face_landmarks in face_landmarks_list:
        right_eye=face_landmarks["right_eye"]
        
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


    # Show the picture

    plt.rcParams["figure.figsize"] = (16,16)
    plt.imshow(image)


    right_eye = image[right_min[1]:right_max[1],right_min[0]:right_max[0]]
    plt.imshow(right_eye)
    plt.savefig('media/'+file_name+'.jpg',bbox_inches='tight')

    return 1