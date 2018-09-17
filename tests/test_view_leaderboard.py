import unittest
from io.printer import Printer
from table_tennis_ladder import view_leaderboard

class PrinterMock:
    text = ""
    def display(self, text): 
        self.text += str(text)

class TestFileList(unittest.TestCase):
    def test_leaderboard_name_is_output(self):
        printer = PrinterMock()
        lb_dict = {
            'leaderboard1': ["Ben", "Lee", "Dan"]
        }

        default_lb_name = "leaderboard1"
        args = ["--view"]
        view_leaderboard(lb_dict, default_lb_name, args, printer)

        self.assertIn(default_lb_name.upper(), printer.text)


if __name__ == '__main__':
    unittest.main()
