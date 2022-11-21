
# image-to-text
CLI python application that extracts the text within an image to another *.txt* file. The image has to have some text in order for this app to work.

The application receives the path to the image wanted to extract the text, and generates a *.txt* file containing the correspondent text.

This project is intended to see the potential of AI, specifically digital image processing.


## Getting Started
### *1.	Installation process*
In order to have character recognition capabilities in this application, it is necessary to install ***pytesseract** Optical Character Recognition* library.

```bash
pip install pytesseract
```

The library (if used on Windows OS) requires the tesseract.exe binary to be also present for proper installation of the library. During the [installation](https://github.com/UB-Mannheim/tesseract/wiki) of the aforementioned executable, we would be prompted to specify a path for it. This path needs to be remembered as it would be utilized later on in the code. For most installations the path would be *C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe*

###  *2. Running the application*
