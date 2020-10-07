import cv2
from PIL import Image, ImageDraw, ImageOps
from matplotlib import pyplot as plt
import face_recognition
import tensorflow.keras
import numpy as np

def get(path):
    vidcap = cv2.VideoCapture(path)

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
            detection = eye_detection(path,'tmp_eye')
            if detection == 0:
                return_data["true"]+=1
            elif detection == 1:
                return_data['lie']+=1
            else:
                return_data['nature']+=1      
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
    save_path = 'media/'+file_name+'.jpg'
    plt.savefig(save_path,bbox_inches='tight')
    prediction = lie_classifier(save_path)
    if prediction == 'true':
        ret = 0
    elif prediction =='lie':
        ret = 1
    else:
        ret = 2

    return ret

def lie_classifier(img_path):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model('contents/lie_detector/keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(img_path)

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    
    state_true = prediction[0][0]
    state_lie = prediction[0][1]
    state_nature = prediction[0][2]
    if state_true>state_lie:
        res = state_true
        tag = 'true' 
    else:
        res = state_lie
        tag = 'lie'
    if res<state_nature:
        res = state_nature
        tag = 'nature' 

    print(tag,res)
    return tag