
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:13:01 2017

@author: zhang
"""

#import numpy as np
import cv2
#from matplotlib import pyplot as plt

clean_face_path ='/Users/zhang/developer/users_face_file/'
cascade_fn = '/Users/zhang/miniconda2/pkgs/opencv-3.1.0-np112py27_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_fn)
#eye_cascade = cv2.CascadeClassifier('/Users/zhang/anaconda/pkgs/opencv-2.4.11-py27_1/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml')


def face_detect(img, cascade):
    face = cascade.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=4, minSize=(30, 30)) 
    return face


def eyes_detect(img,eye_cascade):
    eyes = eye_cascade.detectMultiScale(img)
    return eyes
    
def draw_face(img, faces, color):
    for x,y,w,h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    
def draw_eyes(img,eyes,color):
    for x,y,w,h in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  
    
if __name__ == '__main__':
    color = (0,0,255)#red
    point1 = ()
    cap = cv2.VideoCapture(0)
    i = 1
    usr_id = 1000
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        rectangle = face_detect(gray,cascade)
        draw_face(frame,rectangle,color)
        
        #eyes = eyes_detect(gray,eye_cascade)
        #draw_eyes(frame,eyes,color)
        cv2.imshow('人脸检测',frame)
        # if cv2.waitKey(10) & 0xFF == ord('s'):     # 当按下"s"键时，将保存当前画面
        #     for x, y, w, h in rectangle:
        #         cv2.imwrite('/Users/zhang/faceset/clean_face'+ clean_face_count +'.jpg', frame)
        #         clean_face_count = clean_face_count + 1
        # elif cv2.waitKey(10) & 0xFF == ord('q'):
        #         break
       
             # 当按下"s"键时，将保存当前画面

            
        for x, y, w, h in rectangle:
            cutImg = gray[y:y+h,x:x+w]      #保存灰度人脸图像
            #grayImg = cv2.cvtColor(cutImg, cv2.COLOR_BAYER_BG2GRAY)
            resizeImg = cv2.resize(cutImg, (100,100),interpolation = cv2.INTER_AREA)
            #保存样本数量为100
            if cv2.waitKey(25)&0xFF == ord('x'):    #按下‘x’键，切换识别用户
                usr_id += 1
            else:
                pass
            while(i > 100):
                i = 1
                cv2.imwrite('{0}{1}{2}{3}{4}'.format(clean_face_path,str(usr_id),'_',str(i),'.jpg'), resizeImg)
                i += 1
                break
            while(i <= 100):
                cv2.imwrite('{0}{1}{2}{3}{4}'.format(clean_face_path,str(usr_id),'_',str(i),'.jpg'), resizeImg)
                i += 1
                break
            
        if cv2.waitKey(25)&0xFF == 32:            #按下空格键暂停摄像头
            cv2.waitKey(0)
            
            
        if cv2.waitKey(25) & 0xFF == ord('q'):   # 当按下'q'键时，将退出循环
            break
        

cap.release()
cv2.destroyAllWindows()
exit()