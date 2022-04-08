# file name ocr_from
import cv2
import pytesseract
from pytesseract import Output

def get_string(_path):
    img = cv2.imread(_path)

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    words = pytesseract.image_to_string(img, config=custom_config)
    return(words)