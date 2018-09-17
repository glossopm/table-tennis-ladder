import unittest
from table_tennis_ladder import *


class TestFindLeaderboardName(unittest.TestCase):
    def test_find_leaderboard_default_case(self):
        default_lb = "leaderboard1"
        args = []

        lboard_name = find_leaderboard_name(default_lb, args)
        self.assertEqual(lboard_name, "leaderboard1")


    def test_find_leaderboard_args_case(self):
        default_lb = "leaderboard1"
        args = ["--view", "leaderboard2"]

        lboard_name = find_leaderboard_name(default_lb, args)
        self.assertEqual(lboard_name, "leaderboard2")

if __name__ == "__main__":
    unittest.main()