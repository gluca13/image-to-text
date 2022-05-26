
class Writer:
    def __init__(self, path, text):
        self._path = path
        self._text = text
        self.fix_path()
        self.convert()


# C:\Users\PC\Desktop\pap\test.jpg


    def get_text(self):
        return self._text

    def get_path(self):
        return self._path

    def fix_path(self):
        try:
            for i in range(len(self._path)-1, -1, -1):
                if self._path[i] == '.':
                    self._path = self._path[:i]
                    print(self._path)
                    break
            self._path += '.txt'
        except Exception as e:
            print(e)

    def convert(self):
        try:
            with open(self._path, 'w') as f:
                f.write(self._text)
        except Exception as e:
            print(e)
