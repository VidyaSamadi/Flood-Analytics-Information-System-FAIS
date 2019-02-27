import cv2
import numpy as np
class imageProcessor():
    def __init__(self):
        pass
    
    def autoAdustment(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equ = cv2.equalizeHist(gray)
        return equ

