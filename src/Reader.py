from PIL import Image
from pytesseract import pytesseract


class Reader:
    def __init__(self, path):
        self.__path = path
        self.__text = ""
        self.convert()

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    def convert(self):
        try:
            image = Image.open(self.path)
            PATH_TO_TESSERACT = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = PATH_TO_TESSERACT
            self.text = pytesseract.image_to_string(image)
        except Exception as e:
            print(e)


# [1] https://www.geeksforgeeks.org/how-to-extract-text-from-images-with-python/
