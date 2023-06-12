import pyautogui
from PIL import Image
from pytesseract import *
import time

pytesseract.tesseract_cmd =  r"F:\Program Files\Tesseract-OCR\tesseract.exe"

def sanitize(text):
    if(b"\n" in bytes(text.encode())):
        text = bytes(text.encode()).replace(b"\n",b" ")
        text = text.decode()
    if(b"\xef\xac\x81" in bytes(text.encode())):
        text = bytes(text.encode()).replace(b"\xef\xac\x81",b"fi")
        text = text.decode()
    if("  " in text):
        text = text.replace("  "," ")
    if("~" in text):
        text = text.replace("~","-")
    text = text.strip()
    return text
        

def findText():
    numScreen = pyautogui.screenshot(region=(640,936,3170-640,1322-936))
    numScreen.save(".\\text.png")

    img = Image.open(".\\text.png")

    output_num = pytesseract.image_to_string(img)
    output_num = sanitize(output_num)
    return str(output_num)

time.sleep(2)
text = findText()

pyautogui.click(660,970)
pyautogui.write(text, interval=0.0001)

