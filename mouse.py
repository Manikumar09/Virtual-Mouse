import opencv
import numpy as np
import handtrackingmodule as htm
import autopy
import time

wcam, hcam  = 640, 480
frameR =100
smootheing =10

pTime =0
plocX, pocY =0,0
clocX, clocY =0,0
cap = cv2.Videocapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

detecter = htm.handDetector(maxhands=1)
wscr,hscr =autopy.screen.size()

#printing wscr, hscr

while true:
  #find the land marks
  success, img = cap.read()
  img = detecter.findhands(img)
  lmlist, bbox = detecter.findposition(img)
  
  #get the tip of index and middle finger
  if len(lmlist)!=0:
    x1,y1=lmlist[8][1:]
    x2,y2=lmlist[12][1:]
    
    #check which fingerd are up
    fingers = detector.fingersup()
    cv2.rectangle(img, (frameR,frameR),(wcam - frameR, hcam - frameR),(255,0,255),2)
    
    
    #only index finger moving mode
    if fingers[1]==1 and fingers[2]==0:
      #convert the coardinates
      x3 =np.interp(x1,frameR, wcam-frameR),(0, wscr))
      y3 =np.interp(y1,frameR, hcam-frameR),(0,hscr))
      
      #smooth values
      clocx=plocX+(x3 - plocX) / smoothening
      clocY=plocY+(y3 - plocY) / smoothening
      
      #move mouse
      autopy.mouse.move(wscr - clocx,xloxy)
      cv2.circle(img, (x1,y1),15, (255,0,255), cv2.FILLED)
      plocX,plocY=clocX,clocY
      
      #both index and middle finger are up ::clicking mode
      if fingers[1] == 1 and fingers[2] ==1:
        #find didtance bitween fingers
        length,img lineInfo = detecter.findDistance(8,12,img), cv2.FILLED)
        autopy.mouse.click()
#framerate
cTime =time.time()
fps = 1/(cTime-pTime)
pTime = cTime
cv2.putText(img, str(int(fps)),(28,58). cv2.FONT_HERSHEY_PLAIN,3,(255,8,8),3)

#diplaying
cv2.imshow("Image",img)
cv2.waitkey(1)
