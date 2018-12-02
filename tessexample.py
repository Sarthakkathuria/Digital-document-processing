
import pyautogui
import pytesseract
import cv2
import numpy
import PIL

pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files (x86)\\tesseract.ocr\\tesseract-ocr-w64-setup-v4.0.0.20181030"


def tesser_image(image):
	image =cv2.resize(image,(0,0),fx=2,fy=2)
	ret,image=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

	image=PIL.Image.fromarray(image,'RGB')
	txt=pytesseract.image_to_string(image)
	txt=txt.replace(",","")
	txt=txt.replace(" ","")


	return (txt)

def screengrab_as_numpy_array(Location):
	im=numpy.array(PIL.ImageGrab.grab(bbox=(Location[0],Location[1],Location[2],Location[3])))	
	im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
	cv2.waitKey(0)
	return(im)
print(tesser_image(screengrab_as_numpy_array((1812,1042,1850,1058))))
