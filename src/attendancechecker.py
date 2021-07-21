from datetime import date
import glob
from src import recognize as recognizer
from src import generate_report as gr
import os

ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
ROOT = ROOT_DIR.replace("\\", "/")


def check():
    ext = ['png', 'jpg', 'jpeg']
    present = []
    today = date.today()
    # mm/dd/y
    d3 = today.strftime("%m-%d-%y")
    path = ROOT + '/ScreenShots/' + d3 + '/'
    print(path)
    files = []
    [files.extend(glob.glob(path + '*.' + e)) for e in ext]
    print('lahat')
    for item in files:
        print(item)
    for images in files:
        print(images)
        try:
            present += recognizer.readImage(images, d3)
        except Exception as e:
            print(e)
            print('may error daw')
    repPath = ROOT + "/app/static/Attendance.csv"
    print(present)
    gr.updateCSV(present, repPath)