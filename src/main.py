import cv2
import os

cap=cv2.VideoCapture(0) # web cam dectect
cap.set(3,640) # width
cap.set(4,480) # height

imgbackground=cv2.imread('src\Resources\\background.png')

# extract all images by for loop
modes_folder_path='src\Resources\Modes'
img_list=[]
mode_path=os.listdir(modes_folder_path)
for path in mode_path:
    img_list.append(cv2.imread(os.path.join(modes_folder_path,path)))
    
print(len(img_list))

while True:
    success, img = cap.read()
    
    imgbackground[162:162+480,55:55+640]=img
    imgbackground[44:44+633,808:808+414]=img_list[0]

    #cv2.imshow('webcam', img)
    cv2.imshow('Face Attendance', imgbackground)
    cv2.waitKey(1)
