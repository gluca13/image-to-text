import Reader
import Writer

print("Type the path of the file: ", end='')

image_path = input()

reader = Reader.Reader(image_path)
#C:\Users\Gianluca\Desktop\test.jpg
text = reader.text

writer = Writer.Writer(image_path, text)

print(f"\033[94mText extracted from image in path -> {writer.path}\033[0m")

