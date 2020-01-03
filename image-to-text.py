#image to text conversion using opencv and pytesseract
#OpenCV to do any kind of image transformations - pip install opencv-python
#Tesseract is an optical character recognition engine for various operating systems. It is free software.
#install Tesseract software before installing pytesseract library
#install pytesseract - pip install pytesseract

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
