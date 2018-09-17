class File:
    filename = ""

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        list_file = open(self.filename, "r")
        list_str = list_file.read()
        list_file.close()
        return list_str

    def write(self, write_str):
        list_file = open(self.filename, "w")
        list_file.write(write_str)
        list_file.close()


