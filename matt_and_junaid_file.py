class File:

    def read(self, filename):
        list_file = open(filename, "r")
        list_str = list_file.read()
        list_file.close()
        return list_str

    def write(self, filename, write_str):
        list_file = open(self.filename, "w")
        list_file.write(write_str)
        list_file.close()



class FileMock:
    def read(self, filename):
        return text
