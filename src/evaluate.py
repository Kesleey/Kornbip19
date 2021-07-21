#
# def evaluate():
#     testFilesFolder = "D:/Pycharm/dlib/9315-kornbip19/Test"
#     y_actual = []
#     y_predict = []
#     for i in names:
#         items = testFilesFolder+'/'+i+'/'
#         print('inside i loop')
#         print("items ")
#         print(items)
#         files = []
#         [files.extend(glob.glob(items + '*.' + e)) for e in ext]
#         print(files)
#         for images in files:
#
#             path = testFilesFolder + '/' + i + images
#
#             img = dlib.load_rgb_image(images)
#
#             # gray = io.imread(images)
#
#             gray = io.imread(images)
#             aasdf = hog_face_detector(img)
#             print("From evaluation method")
#             print(path)
#             print(img)
#             print(aasdf)
#             for face in aasdf:
#                 face_landmarks = sp(gray, face)
#                 img_np = np.array(gray)
#                 name = recognize(img_np, face_landmarks)
#                 print("Y pred ")
#                 y_actual.append(i)
#                 y_predict.append(name)
#                 print(name)
#     #y_actual = cleanUp(y_actual)
#     #y_predict = cleanUp(y_predict)
#     print(classification_report(y_predict,y_predict))
#     print(confusion_matrix(y_actual, y_predict))
#     return