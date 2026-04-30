import pywhatkit as kit

import cv2

handwritten = input("Enter your text to convert in Handwriting: ")

kit.text_to_handwriting(handwritten, save_to="text_to_handwriting.png")
img = cv2.imread('text_to_handwriting.png')
cv2.imshow("Python Coding", img)
cv2.waitKey(0)
cv2.destroyAllWindows()