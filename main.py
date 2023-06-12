import pyautogui
from PIL import Image
from pytesseract import *
import time 

pytesseract.tesseract_cmd = r"F:\Program Files\Tesseract-OCR\tesseract.exe"


def sanitize(text):
    if(b"\n" in bytes(text.encode())):
        text = bytes(text.encode()).replace(b"\n",b" ")
        text = text.decode()
    if(b"\xef\xac\x81" in bytes(text.encode())):
        text = bytes(text.encode()).replace(b"\xef\xac\x81",b"fi")
        text = text.decode()
    # print(bytes(text.encode()))
    if("  " in text):
        text = text.replace("  "," ")
    if("~" in text):
        text = text.replace("~","-")
    # text = text.lower()
    text = text.strip()
    return text



def findText():
    numScreen = pyautogui.screenshot(region=(640,936,3170-640,1322-936))
    numScreen.save(".\\text.png")

    img = Image.open(".\\text.png")

    # new_size = tuple(4*x for x in img.size)
    # img = img.resize(new_size, Image.ANTIALIAS)

    output_num = pytesseract.image_to_string(img)
    print(output_num)
    output_num = sanitize(output_num)
    print(output_num)
    return str(output_num)

time.sleep(2)
text = findText()

pyautogui.click(660,970)
pyautogui.write(text,interval = 0.0001)
# pyautogui.write(text)


# X:  640 Y:  936 RGB: ( 76, 154, 216)

# X: 3170 Y: 1322 RGB: (213, 231, 246)
# pyautogui.displayMousePosition()