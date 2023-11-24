import cv2 as cv
from threading import Thread


class GetVideo:
    def __init__(self, data, source=0):
        self.isRunning = False
        self.__data = data
        self.__stream = None
        self.__source = source

    def start_fetch(self):
        self.isRunning = True
        # self.__stream = cv.VideoCapture(self.__source)
        if isinstance(self.__source, int):
            self.__stream = cv.VideoCapture(self.__source)
        else:
            self.__stream = cv.VideoCapture(self.__source)
            
        if not self.__stream.isOpened():
            self.__stream.open(self.__source)
        self.__stream.set(cv.CAP_PROP_BUFFERSIZE, 1)
        Thread(target=self.get_frame, args=()).start()

    def get_frame(self):
        while self.isRunning == True:
            ret, img = self.__stream.read()
            if ret:
                self.__data.setImage(True,img)

    def stop_fetch(self):
        self.isRunning = False
        self.__stream.release()


class ShowVideo:
    def __init__(self, data, title="Video"):
        self.isRunning = False
        self.__data = data
        self.__title = title

    def start(self):
        self.isRunning = True
        Thread(target=self.show, args=()).start()

    def show(self):
        while self.isRunning:
            if self.__data.getImage() is not None:
                cv.imshow(self.__title, self.__data.getImage())
            if cv.waitKey(1) == ord('q'):
                self.isRunning = False
                break

    def stop(self):
        self.isRunning = False
        cv.destroyAllWindows()


class VideoData:
    def __init__(self):
        self.__exist = False
        self.__image = None

    def setImage(self, exist, image):
        self.__exist = exist
        self.__image = image

    def getImage(self):
        return self.__exist, self.__image
