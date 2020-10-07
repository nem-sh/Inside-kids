import cv2
vidcap = cv2.VideoCapture('media/video')
 
count = 0
 
while True:
    ret, image = vidcap.read()
    if not ret:
        break
    if(int(vidcap.get(1)) % 20 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("media/images/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1
 
vidcap.release()