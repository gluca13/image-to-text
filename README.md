
# image-to-text
CLI python application that extracts the text within an image to a *.txt* file. The image must have some text in it for this app to work.

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
The application is run by executing the following command in the terminal, positioned in */src* folder:

**Linux**
```bash
    python3 Converter.py
```

**Windows**
```bash
    python Converter.py
```

The application will prompt the user to enter the path to the image file. The path can be entered as follows:

**1. Entering the path to the image file directly**

Example:

```bash
    Type the path to the image file: C:\Users\Gianluca\Desktop\test.jpg
```

**2. Entering the path to the image file by dragging and dropping the file into the terminal**

Example:

```bash
    Type the path to the image file: c:\Users\Gianluca\Desktop\test.jpg
```

###  *3. Output*

The application will generate a *.txt* file containing the text extracted from the image. The file will be saved in the same directory as the image file and the path will be prompted in the terminal.

## Tests

The application was tested with the following image:

>![test](https://user-images.githubusercontent.com/65744020/203184537-1224f584-ed06-4690-b5da-81e37b07acd0.jpg)

The output of the application was the following:
> Home
>
>Stefan Weil edited this page on Jul 13 - 79 revisions
>
>Tesseract at UB Mannheim
>
>The Mannheim University Library (UB Mannheim) uses Tesseract to perform text recognition (OCR = optical character
>recognition) for historical German newspapers (Allgemeine PreuBische Staatszeitung, Deutscher Reichsanzeiger). The latest
>results with text from more than 700000 pages are available online.
>
>Tesseract installer for Windows
>
>Normally we run Tesseract on Debian GNU Linux, but there was also the need for a Windows version. That's why we have built
>a Tesseract installer for Windows.
>
>WARNING: Tesseract should be either installed in the directory which is suggested during the installation or in a new
>directory. The uninstaller removes the whole installation directory. If you installed Tesseract in an existing directory, that
>directory will be removed with all its subdirectories and files.
>
>The latest installers can be downloaded here:
>
>� tesseract-ocr-w32-setup-v5.2.0.202207 12.exe (32 bit) and
>�  tesseract-ocr-w64-setup-v5.2.0.20220712.exe (64 bit) resp.
>
>There are also older versions available.
>
>In addition, we also provide documentation which was generated by Doxygen.
>

## Built With
* Python
* Tesseract 5.1.0

## Authors

* Gianluca Gibellato
* Marcelo Caracas
