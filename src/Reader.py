from PIL import Image
from pytesseract import pytesseract


class Reader:
    def __init__(self, path):
        self._path = path
        self._text = ""
        self.convert()

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text

    def convert(self):
        try:
            image = Image.open(self._path)
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = path_to_tesseract
            self.set_text(pytesseract.image_to_string(image))
        except Exception as e:
            print(e)


# # Defining paths to tesseract.exe
# # and the image we would be using
# path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# #image_path = r'C:\Users\PC\Desktop\test.jpg'
# print('Path de la imagen: ')
# image_path = r'{}'.format(input())

# # Opening the image & storing it in an image object
# img = Image.open(image_path)

# # Providing the tesseract executable
# # location to pytesseract library
# pytesseract.tesseract_cmd = path_to_tesseract

# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
# text = pytesseract.image_to_string(img)

# # Displaying the extracted text
# print(text[:-1])

# [1] https://www.geeksforgeeks.org/how-to-extract-text-from-images-with-python/
