import unittest
from table_tennis_ladder import *


class TestMatchPlayed(unittest.TestCase):
    
    def test_match_winner_higher(self):
        winner = "Alpha"
        loser = "Beta"
        ladder = ["Gamma", "Alpha", "Beta", "Delta"]
        new_ladder = match_played(winner, loser, ladder)
        self.assertEqual("Alpha", new_ladder[1])

    def test_match_loser_higher(self):
        winner = "Beta"
        loser = "Alpha"
        ladder = ["Gamma", "Alpha", "Beta", "Delta"]
        new_ladder = match_played(winner, loser, ladder)
        self.assertEqual("Beta", new_ladder[1])

    def test_match_loser_not_listed(self):
        winner = "Beta"
        loser = "Alpha"
        ladder = ["Gamma", "Beta", "Delta"]
        new_ladder = match_played(winner, loser, ladder)
        self.assertEqual("Alpha", new_ladder[3])

    def test_match_winner_not_listed(self):
        winner = "Alpha"
        loser = "Beta"
        ladder = ["Gamma", "Beta", "Delta"]
        new_ladder = match_played(winner, loser, ladder)
        self.assertEqual("Alpha", new_ladder[1])
        self.assertEqual("Beta", new_ladder[2])

    def test_match_both_not_listed(self):
        winner = "Alpha"
        loser = "Beta"
        ladder = ["Gamma", "Sigma" "Delta"]
        new_ladder = match_played(winner, loser, ladder)
        print new_ladder
        self.assertEqual("Alpha", new_ladder[3])
        self.assertEqual("Beta", new_ladder[4])

if __name__ == "__main__":
    unittest.main()
