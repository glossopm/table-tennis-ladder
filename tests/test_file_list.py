import unittest
from io.file_list import FileList

class FileMock:
    def __init__(self, text):
        self.text = text
    def read(self, filename):
        return self.text
    def write(self, filename, text): 
        self.text = text

class TestFileList(unittest.TestCase):
    def test_file_return_list(self):
        file_mock = FileMock("Ben,Lee,Dan")
        file_list = FileList(file_mock)
        ladder = file_list.read()
        self.assertEqual("Ben", ladder[0])
        self.assertEqual("Lee", ladder[1])
        self.assertEqual("Dan", ladder[2])

    def test_file_write_to_comma_delimited_file(self):
        file_mock = FileMock("")
        file_list = FileList(file_mock) 
        ladder = ["Ben", "Lee", "Dan"]
        file_list.write(ladder)
        self.assertEqual(file_mock.text, "Ben,Lee,Dan")

if __name__ == '__main__':
    unittest.main()
