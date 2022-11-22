class Writer:
    def __init__(self, path, text):
        self.__path = path
        self.__text = text
        self.fix_path()
        self.convert()

    @property
    def text(self):
        return self.__text

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @text.setter
    def text(self, text):
        self.__text = text

    def fix_path(self):
        try:
            for i in range(len(self.path)-1, -1, -1):
                if self.path[i] == '.':
                    self.path = self.path[:i] + '.txt'
                    break
        except Exception as e:
            print(e)

    def convert(self):
        try:
            with open(self.path, 'w') as f:
                f.write(self.text)
        except Exception as e:
            print(e)
