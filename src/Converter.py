import Reader
import Writer

print("Type the path of the file: ", end='')

image_path = r'{}'.format(input())

reader = Reader.Reader(image_path)

text = reader.get_text()

writer = Writer.Writer(image_path, text)

print("\033[94mText text extracted from image in path -> {}\033[0m".format(writer.get_path()))
