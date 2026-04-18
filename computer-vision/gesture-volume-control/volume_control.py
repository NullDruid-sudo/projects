import cv2 as cam
import time as tm
import mediapipe as mp
import subprocess
import numpy as np

handsH = mp.solutions.hands
hands = handsH.Hands(min_detection_confidence=0.5)
mpdr = mp.solutions.drawing_utils

green_lines = mpdr.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)
red_lines = mpdr.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)

ptime = 0
imger = cam.VideoCapture(0)

def set_volume(percent):
        subprocess.run(["pactl","set-sink-volume","@DEFAULT_SINK@",f"{int(percent)}%"])

while True:
        success, img = imger.read()
        if not success:
                continue
        img = cam.flip(img,1)
        clr = cam.cvtColor(img,cam.COLOR_BGR2RGB)
        img.flags.writeable = False
        results = hands.process(clr)
        img.flags.writeable = True
        if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                        h,w,_ = img.shape
                        mpdr.draw_landmarks(img,handLms,handsH.HAND_CONNECTIONS,red_lines,green_lines)
                        thumb = handLms.landmark[4]
                        index = handLms.landmark[8]
                        tx,ty = int(thumb.x*w), int(thumb.y*h)
                        ix,iy = int(index.x*w), int(index.y*h)
                        cam.circle(img,(tx,ty),8,(255,0,255),cam.FILLED)
                        cam.circle(img,(ix,iy),8,(255,0,255),cam.FILLED)
                        mx,my = int((tx+ix)/2), int((ty+iy)/2)
                        dist = ((tx-ix)**2 + (ty-iy)**2)**0.5
                        cam.line(img,(tx,ty),(ix,iy),(255,0,255),2)
                        cam.circle(img,(mx,my),8,(0,255,255) if dist > 50 else (0,0,0),cam.FILLED)
                        vol = np.interp(dist,[30,200],[0,100])
                        set_volume(vol)
                        cam.putText(img,f"Dist : {int(dist)}",(10,90),cam.FONT_HERSHEY_DUPLEX,1,(255,0,255),1)

        ctime = tm.time()
        fps = 1/(ctime-ptime)
        ptime = ctime

        cam.putText(img,f"FPS : {int(fps)}",(10,30),cam.FONT_HERSHEY_DUPLEX,1,(255,0,255),1)

        cam.imshow("Camera",img)

        if cam.waitKey(1) & 0xFF == 27:
                break

imger.release()
cam.destroyAllWindows()
