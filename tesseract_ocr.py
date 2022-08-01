# -*- coding: utf-8 -*-

from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


image_to_ocr = cv2.imread('D:\\program\\cloud-and-ai\\id_card.jpg')

preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)

preprocessed_img = cv2.threshold(preprocessed_img,0 ,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

cv2.imwrite('temp_img.jpg', preprocessed_img)

preprocessed_pil_img = Image.open('temp_img.jpg')

text_extracted = pytesseract.image_to_string(preprocessed_pil_img, lang="khm")

print(text_extracted)

cv2.imshow("image", image_to_ocr)