import cv2 as cam
import mediapipe as mp
import time as t

Handsh = mp.solutions.hands
hand = Handsh.Hands()
mpdr = mp.solutions.drawing_utils

green_lines = mpdr.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)
red_lines = mpdr.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)

camera = cam.VideoCapture(0)
ptime = 0

while True:
        success , img = camera.read()
        if not success:
                continue

        img = cam.flip(img,1)
        rgba = cam.cvtColor(img,cam.COLOR_BGR2RGB)

        img.flags.writeable = False
        results = hand.process(rgba)
        img.flags.writeable = True

        lmList = []

        if results.multi_hand_landmarks:
                for i, handLms in enumerate(results.multi_hand_landmarks):

                        handType = results.multi_handedness[i].classification[0].label

                        h,w,_ = img.shape

                        for id, lm in enumerate(handLms.landmark):
                                x = int(lm.x * w)
                                y = int(lm.y * h)
                                lmList.append([id, x, y])

                        mpdr.draw_landmarks(img,handLms,Handsh.HAND_CONNECTIONS,red_lines,green_lines)

                        fingers = []

                        if handType == "Right":
                                if lmList[4][1] > lmList[3][1]:
                                        fingers.append(1)
                                else:
                                        fingers.append(0)
                        else:
                                if lmList[4][1] < lmList[3][1]:
                                        fingers.append(1)
                                else:
                                        fingers.append(0)

                        tipIds = [8,12,16,20]

                        for tip in tipIds:
                                if lmList[tip][2] < lmList[tip-2][2]:
                                        fingers.append(1)
                                else:
                                        fingers.append(0)

                        cam.putText(img,f"{handType} Count : {fingers.count(1)}",(10,50),cam.FONT_HERSHEY_DUPLEX,1,(255,0,255),1)

        ctime = t.time()
        fps = 1/(ctime-ptime)
        ptime = ctime

        cam.putText(img,f"FPS : {int(fps)}",(10,30),cam.FONT_HERSHEY_DUPLEX,1,(255,0,255),1)

        cam.imshow("Camera",img)

        if cam.waitKey(1) & 0xFF == 27:
                break

camera.release()
cam.destroyAllWindows()
