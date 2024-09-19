try :
    from PIL import Image
except ImportError:
    import Image

from plate import * 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

# info = recText('ram.png')
# print(info)
# file = open('result.txt','w')
# file.write(info)
# file.close()
# print('Written Successfully')

while True:
    cap()
    info = recText('1.jpg')
    print(info)
    if cv2.waitKey(1) == ord('q'): # interrupt
        break

cam.release()    
cv2.destroyAllWindows()