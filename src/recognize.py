import os
import dlib
import numpy as np
import trainer as trainer
from imutils import paths
import glob
import pyautogui
import datetime
from PIL import Image
from skimage import io
from PIL import ImageDraw
from PIL import ImageFont
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
#from src import generate_report as gr



#*********////////////////PWEDE NA ICOMMENT YUNG CODE BELOW IF TAPOS NA MAGTRAIN NE (DI AKO GALIT)/////****

#trainer.train("D:/Pycharm/integration2/9315-kornbip19/Cropped")
#*****////////////// PARA DI MABAGAL MAG PROCESS YUNG PYCHARM NE TYS   /////////////////////******///////////////////////////
ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
ROOT = ROOT_DIR.replace("\\","/")

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(ROOT + "/src/shape_predictor_68_face_landmarks.dat")
model = dlib.face_recognition_model_v1(ROOT + "/src/dlib_face_recognition_resnet_model_v1.dat")

PATH_CROPPED = list(paths.list_images(ROOT + "/app/Uploads"))
imagePaths = list(paths.list_images(ROOT + "/app/Uploads"))
names = trainer.get_recorded_names()
allFaces = trainer.get_recorded_image_representations()


ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
ROOT = ROOT_DIR.replace("\\", "/")
path = ROOT+'/LabeledScreenshots/'

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
        try:
            os.mkdir(tempPath, 0o666)
            print("directory created")
        except Exception:
            print("May folder na daw na ganon")
    return



# clean up lang pwede na yata alisin tow
def cleanUp(faces):
    return filter(None, faces)


ext = ['png', 'jpg']

# method for the the computation of distance of landmark differences
def findDistance(db_image_representation, to_compare_representation):
    dis = db_image_representation - to_compare_representation
    dis = np.sum(np.multiply(dis, dis))
    dis = np.sqrt(dis)
    return dis


#determining who the person is
def determineWho(img_rep):
    cleanedUpFaces = cleanUp(allFaces)

    threshold = .5
    tempDis = 1
    distances = [[]]
    index = 0
    tempIndex = -5
    for person in cleanedUpFaces:
        tempList = []
        for face in person:
            dis = findDistance(face, img_rep)
            tempList.append(dis)

            if dis < threshold:
                if dis < tempDis:
                    tempDis = dis
                    tempIndex = index

        index += 1
        distances.append(tempList)
        tempList.clear()
    if tempIndex == -5:
        return "Unknown"

    return names[tempIndex]



def recognize(image, imageShape):
    image_aligned = dlib.get_face_chip(image, imageShape)
    value = determineWho(np.array(model.compute_face_descriptor(image_aligned)))
    return value


hog_face_detector = dlib.get_frontal_face_detector()


# screen cap face recognition
def readImage(path, d3):
    imej = dlib.load_rgb_image(path)
    gray = io.imread(path)
    aasdf = hog_face_detector(imej)
    img = Image.open(path)
    present = []
    for face in aasdf:
        face_landmarks = sp(imej, face)
        img_np = np.array(imej)
        name = recognize(img_np, face_landmarks)
        present.append(name)
        # writing of names sa pic
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(ROOT + "/Roboto-Regular.ttf", 24)
        draw.text((face_landmarks.part(67).x, face_landmarks.part(67).y), name, (0, 0, 0), font=font)
    filename = str(path).split('ScreenShots')[1]
    print(filename.split('/')[0])
    makeDir(ROOT + "/LabeledScreenshots/{}".format(d3))

    img.save(ROOT + "/LabeledScreenshots/{}/{}".format(d3,filename.split('screengrab_')[1]))
    return present;




# model evaluation
def evaluate():
    testFilesFolder = ROOT + "/Test"
    y_actual = []
    y_predict = []
    for i in names:
        items = testFilesFolder+'/'+i+'/'
        print('inside i loop')
        print("items ")
        print(items)
        files = []
        [files.extend(glob.glob(items + '*.' + e)) for e in ext]
        print(files)
        for images in files:

            path = testFilesFolder + '/' + i + images

            img = dlib.load_rgb_image(images)

            # gray = io.imread(images)

            gray = io.imread(images)
            aasdf = hog_face_detector(img)
            print("From evaluation method")
            print(path)
            print(img)
            print(aasdf)
            for face in aasdf:
                face_landmarks = sp(gray, face)
                img_np = np.array(gray)
                name = recognize(img_np, face_landmarks)
                print("Y pred ")
                y_actual.append(i)
                y_predict.append(name)
                print(name)
    #y_actual = cleanUp(y_actual)
    #y_predict = cleanUp(y_predict)
    print(classification_report(y_predict,y_predict))
    print(confusion_matrix(y_actual, y_predict))
    return
# list  = ['kes']
# list.append(readImage(ROOT + '/ScreenShots/07-21-21/screengrab_0803_09.5.png','test'))
# print (list)
#evaluate()

# saveIntoFile()
# readFile()









# img1 = dlib.load_rgb_image(img1_path)
# img2 = dlib.load_rgb_image(img2_path)
#
# img1_detected = detector(img1, 1)
# img2_detected = detector(img2, 1)
#
# img1_shape = sp(img1, img1_detected[0])
# img2_shape = sp(img2, img2_detected[0])
#
# img1_aligned = dlib.get_face_chip(img1, img1_shape)
# img2_aligned = dlib.get_face_chip(img2, img2_shape)

# plt.imshow(img1_aligned)
# plt.show()
# plt.imshow(img2_aligned)
# plt.show()

# img1_representation = np.array(model.compute_face_descriptor(img1_aligned))
# img2_representation = np.array(model.compute_face_descriptor(img2_aligned))
#


