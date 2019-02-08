import cv2

class imageProcessor():
    def __init__(self):
        pass
    
    def autoAdustment(self, src, dst, clip_hist_percent=0):
        cv2.CV_Assert(clip_hist_percent >=0)
        cv2.CV_assert(src.type() == cv2.CV_SUC1 or (src.type() == cv2.CV_SUC3) or )
