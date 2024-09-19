import cv2
import pytesseract
import random
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

harscade = r"D:\ai project\number_plate\haarcascade_russian_plate_number.xml"
# Camera Configuration
cam = cv2.VideoCapture(0)
cam.set(3,640) # height
cam.set(4,480) # width
min_area = 500

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def cap():
    _,img = cam.read()  
     
    plate_cascade = cv2.CascadeClassifier(harscade)
    
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    plates = plate_cascade.detectMultiScale(img_gray,1.1,4) 
    
    for(x,y,w,h) in plates:
        area = w*h
        if area > min_area:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,'Number Plate Detect',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
            img_roi = img[y:y+h,x:x+w]
            cv2.imshow('ROI',img_roi)
            # while True:
            #     cv2.imwrite(f'{random.random()}.jpg',img_roi)
            #     info = recText(img_roi)
            #     file = open('result.txt','w')
            #     file.write(info)
            #     file.close()
    cv2.imshow('Number Plate',img) # Show Image

# Program Start
while True:
    cap()
    if cv2.waitKey(1) == ord('q'): # interrupt
        break

cam.release()    
cv2.destroyAllWindows()
            