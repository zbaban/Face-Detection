import cv2
from random import randrange

#loading pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Chhose an image to dtecet faces in 
#img = cv2.imread('faces.jpg')
#img = cv2.imread('faces.jpg')

#Capture Video from webcam put 0. For video scanning like mp4, replace the 0 with the video name.
webcam = cv2.VideoCapture('People_Walking.mp4')

##### Iterate forever for frames, needed for video only, for img remove it
while  True:
    #read the current frame
    successful_frame_read, frame = webcam.read()

    #must convert to grayscale, for image use img, for video use frame
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect Face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 2)
    
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)

    #Stop
    if key==81 or key==113:
        break

###Relase the VideoCapture object
webcam.release()

print ("Code Complete")

"""
# For image dettection, replace fram with img or grayscaled_img
#Detect Face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 2)

#print(face_coordinates)

#Display the image with the faces
cv2.imshow('Face Detector',grayscaled_img)
key = cv2.waitKey(1)

#Stop
if key ==81 or key ==113:
    break

###Relase the VideoCapture object
webcam.release()


print ("Code Complete")

"""