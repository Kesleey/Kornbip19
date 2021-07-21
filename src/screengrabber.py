import time
from playsound import playsound
from PIL import ImageGrab
from datetime import datetime
from datetime import date
import os.path
from os import path
interval = 2
screenshots = 5

ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
ROOT = ROOT_DIR.replace("\\", "/")
path = ROOT+'/ScreenShots/'

print(path)

# initializer
def ScreenGrabber():
    return

# initializer
def ScreenGrabber(newInterval, newScreenshots):
    interval = newInterval
    screenshots = newScreenshots

# checker if folder exists
def dirExist(dirname):
    return os.path.exists(os.path.join(path,dirname))

# method for folder creation
def makeDir(dirname):
    tempPath = os.path.join(path,dirname)
    if (dirExist(path+dirname)):
        print(tempPath)
        print('exists')
        return
    else:
        os.mkdir(tempPath, 0o666)
        print("directory created")
    return

# date today
today = date.today()
# mm/dd/y
d3 = today.strftime("%m-%d-%y")
print("d3 =", d3)




# invoked every run
makeDir(d3)





time.sleep(2)
# screen grabber
while screenshots != 0:
    im = ImageGrab.grab()
    dt = datetime.now()
    playsound(ROOT + '/src/shutter.mp3')
    fname = "{}/{}/screengrab_{}.{}.png".format(path, d3, dt.strftime("%H%M_%S"), dt.microsecond // 100000)
    im.save(fname, 'png')
    while interval != 0:
       interval = interval - 1

    time.sleep(1)
    screenshots = screenshots - 1
