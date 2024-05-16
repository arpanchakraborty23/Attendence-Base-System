import dlib
import cv2
import os,sys
from datetime import datetime

from src.exception.exception import CustomException
import logging
import face_recognition

def face_detection(image_path):
    try:
        """
        Detect faces in an image.

        :param image_path: Path to the image file
        :return: A list of tuples containing the coordinates of each detected face (top, right, bottom, left)
        """
        # Load the image
        image = face_recognition.load_image_file(image_path)

        # Find face locations in the image
        face_locations = face_recognition.face_locations(image)

        return face_locations




    except Exception as e:
        print(e)
        raise CustomException(sys,e)