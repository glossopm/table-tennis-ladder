class FileList:
    def __init__(self, file):
        self.file = file

    def read(self):
        list_str = self.file.read()
        return list_str.split(",")
 
    def write(self, data):
        self.file.write(",".join(data))



class File:
    d
