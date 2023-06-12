from screeninfo import get_monitors
import pyautogui
from PIL import Image
from pytesseract import *
import time 
import mouse

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
    if(";" in text):
        text = text.replace(";","")
    if("~" in text):
        text = text.replace("~","-")
    # text = text.lower()
    text = text.strip()
    return text

for m in get_monitors():
    if(m.is_primary==True):
        monitor = m

width = monitor.width
height = monitor.height

def findText(x1,y1,x2,y2):
    numScreen = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))
    numScreen.save(".\\text.png")

    img = Image.open(".\\text.png")

    # new_size = tuple(4*x for x in img.size)
    # img = img.resize(new_size, Image.ANTIALIAS)

    output_num = pytesseract.image_to_string(img)
    output_num = sanitize(output_num)
    print(output_num)
    return str(output_num)

clicks = 0

pos = []

def app():
    pos.append(pyautogui.position())
    # print(pyautogui.position())


mouse.on_click(app)

if(len(pos)>2):
    print(pos)



time.sleep(4)
text = findText(pos[0].x,pos[0].y,pos[1].x,pos[1].y)

pyautogui.click(pos[2].x,pos[2].y)
pyautogui.write(text,interval = 0.0001)
# pyautogui.write(text)


# X:  640 Y:  936 RGB: ( 76, 154, 216)

# X: 3170 Y: 1322 RGB: (213, 231, 246)
# pyautogui.displayMousePosition()