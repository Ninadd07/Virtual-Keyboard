import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone 
from pynput.keyboard import Controller


cap = cv2.VideoCapture(0) 
cap.set (3, 1280)
cap.set (4, 720)

detector = HandDetector(detectionCon = 0.8)

keys = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L","."],
        ["Z", "X", "C", "V", "B", "N", "M", ","]]

finalText = ""

keyboard = Controller ()

# def drawAll(img, buttonList) :

#     for button in buttonList :
#         x , y = button.pos
#         w , h = button.size
#         cv2.rectangle(img,button.pos, (x+w, y+h), (255,0,255), cv2.FILLED)
#         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
#     return img

def drawAll(img, buttonList) :
    imgNew = np.zeros_like(img, np.uint8)
    

    # cv2.rectangle(img, (0,0), (1280 , 720), (87,28,0), cv2.FILLED)


    cvzone.cornerRect(imgNew, (250, 450, 85, 85),20, rt=0)
    cv2.rectangle(imgNew ,(250 , 450), (1035 , 535), (139,0,0), cv2.FILLED)
    cv2.putText(imgNew, " ", (435 , 455), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 3)


    cvzone.cornerRect(imgNew, (1050, 450, 85, 85),20, rt=0)
    cv2.rectangle(imgNew ,(1050 , 450), (1135 , 535), (139,0,0), cv2.FILLED)
    cv2.putText(imgNew, "C", (1070 , 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 3)


    cvzone.cornerRect(imgNew, (950, 350, 185, 85),20, rt=0)
    cv2.rectangle(imgNew ,(950 , 350), (1135 , 435), (139,0,0), cv2.FILLED)
    cv2.putText(imgNew, "Back", (970 , 415), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 3)


    cvzone.cornerRect(imgNew, (150, 450, 85, 85),20, rt=0)
    cv2.rectangle(imgNew ,(150 , 450), (235 , 535), (139,0,0), cv2.FILLED)
    cv2.putText(imgNew, "c", (170 , 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 3)


    for button in buttonList :
        x , y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),20, rt=0)
        cv2.rectangle(imgNew ,button.pos, (x+button.size[0], y+button.size[1]), (139,0,0), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 40, y + 60), cv2.FONT_HERSHEY_PLAIN, 4, (230,216,173), 3)
    

    out = img.copy()
    alpha = -0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out



class Button() :
    def __init__(self , pos , text , size = [85,85]) :
        self.pos = pos
        self.size = size
        self.text = text



buttonList = []
for i in range (len(keys)) :
    for j , key in enumerate(keys [i]) :
        buttonList.append(Button([j*100+150,100*i+50], key))


space = " "


while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)
    # print(lmList)


    if lmList :
        l,_, _ = detector.findDistance(8,4, img, draw = False)
        if l < 40 : 
            if 250 < lmList[8][0] < 1035 and 450 < lmList [8][1] < 535 :
                keyboard.press(space)
                cv2.rectangle(img,(250 , 450), (1035, 535), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (255, 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)
                finalText += space
                sleep (1)
            

            if 150 < lmList[8][0] < 235 and 450 < lmList [8][1] < 535 :
                keyboard.press(key)
                cv2.rectangle(img,(150 , 450), (235, 535), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (170 , 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)
                
                keys[1][0] = "q"
                keys[1][1] = "w"
                keys[1][2] = "e"
                keys[1][3] = "r"
                keys[1][4] = "t"
                keys[1][5] = "y"
                keys[1][6] = "u"
                keys[1][7] = "i"
                keys[1][8] = "o"
                keys[1][9] = "p"

                keys[2][0] = "a"
                keys[2][1] = "s"
                keys[2][2] = "d"
                keys[2][3] = "f"
                keys[2][4] = "g"
                keys[2][5] = "h"
                keys[2][6] = "j"
                keys[2][7] = "k"
                keys[2][8] = "l"

                keys[3][0] = "z"
                keys[3][1] = "x"
                keys[3][2] = "c"
                keys[3][3] = "v"
                keys[3][4] = "b"
                keys[3][5] = "n"
                keys[3][6] = "m"

                buttonList = []
                for i in range (len(keys)) :
                    for j , key in enumerate(keys [i]) :
                        buttonList.append(Button([j*100+150,100*i+50], key))

                img = drawAll(img, buttonList)
                sleep (1)


            if 1050 < lmList[8][0] < 1135 and 450 < lmList [8][1] < 535 :
                keyboard.press(key)
                cv2.rectangle(img,(150 , 450), (235, 535), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (170 , 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)
                
                keys[1][0] = "Q"
                keys[1][1] = "W"
                keys[1][2] = "E"
                keys[1][3] = "R"
                keys[1][4] = "T"
                keys[1][5] = "Y"
                keys[1][6] = "U"
                keys[1][7] = "I"
                keys[1][8] = "O"
                keys[1][9] = "P"

                keys[2][0] = "A"
                keys[2][1] = "S"
                keys[2][2] = "D"
                keys[2][3] = "F"
                keys[2][4] = "G"
                keys[2][5] = "H"
                keys[2][6] = "J"
                keys[2][7] = "K"
                keys[2][8] = "L"

                keys[3][0] = "Z"
                keys[3][1] = "X"
                keys[3][2] = "C"
                keys[3][3] = "V"
                keys[3][4] = "B"
                keys[3][5] = "N"
                keys[3][6] = "M"

                buttonList = []
                for i in range (len(keys)) :
                    for j , key in enumerate(keys [i]) :
                        buttonList.append(Button([j*100+150,100*i+50], key))

                img = drawAll(img, buttonList)
                sleep (1)
                

            if 950 < lmList[8][0] < 1135 and 350 < lmList [8][1] < 435 :   
                keyboard.press(key)
                cv2.rectangle(img,(950 , 350), (1135, 435), (0,255,0), cv2.FILLED)
                cv2.putText(img, "Back", (170, 415), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)
                finalText = finalText[0:len(finalText)-1]
                sleep (1)


        for button in buttonList :
            x , y = button.pos
            w , h = button.size


            if 150 < lmList[8][0] < 235 and 450 < lmList [8][1] < 535 :
                cv2.rectangle(img ,(150 , 450), (240, 540), (169,0,0), cv2.FILLED)
                cv2.putText(img, "c", (170, 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)


            if 1050 < lmList[8][0] < 1135 and 450 < lmList [8][1] < 535 :
                cv2.rectangle(img ,(1050 , 450), (1140, 540), (169,0,0), cv2.FILLED)
                cv2.putText(img, "C", (1070, 515), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)


            if 250 < lmList[8][0] < 1035 and 450 < lmList [8][1] < 535 :
                cv2.rectangle(img ,(250 , 450), (1040, 540), (169,0,0), cv2.FILLED)
            

            if 950 < lmList[8][0] < 1135 and 350 < lmList [8][1] < 435 :
                cv2.rectangle(img ,(950 , 350), (1140, 440), (169,0,0), cv2.FILLED)
                cv2.putText(img, "Back", (970, 415), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)


            if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h :
                cv2.rectangle(img ,button.pos, (x+button.size[0]+5, y+button.size[1]+5), (169,0,0), cv2.FILLED)
                # cv2.rectangle(img,(x-10, y-10), (x+w+10, y+h+10), (175,0,175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)
                l,_, _ = detector.findDistance(8,4, img, draw = False)
                # print(l)


                #when clicked
                if l < 40 : 
                    keyboard.press(button.text)
                    cv2.rectangle(img,button.pos, (x+w, y+h), (0,255,0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (238,244,21), 4)
                    finalText += button.text
                    sleep (1)
                    

    cv2.rectangle(img, (50 , 560), (1035 , 645), (87,28,0), cv2.FILLED)
    cv2.putText(img, finalText, (50 , 625), cv2.FONT_HERSHEY_PLAIN, 5, (0,103,255), 5)

    cv2.imshow("Image" , img)
    cv2.waitKey(1)
    
