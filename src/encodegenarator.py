import cv2
import pickle
from datetime import datetime
import os,sys
import logging
import PIL.Image
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"
from src.exception.exception import CustomException
from src.utils.utils import face_detection


# import images
imag_folder_path='images'
path_list=os.listdir(imag_folder_path)
print(path_list)
img_list=[]
studentId=[]
for path in path_list:
    img_list.append(cv2.imread(os.path.join(imag_folder_path,path)))
    id=os.path.splitext(path)[0]
    studentId.append(id)

def finencoding(img_list):
    try:
        encode_list=[]
        for img in img_list:
            img=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
            encode=cv2.imencode(img=img)[0]
            encode_list.append(encode)

        return encode_list
    except Exception as e:
        
        raise CustomException(sys,e)
    
en=finencoding(img_list=img_list)
print('encode complete')
