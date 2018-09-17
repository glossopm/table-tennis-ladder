import unittest
from table_tennis_ladder import *


class TestMatchPlayed(unittest.TestCase):
    
    def test_match_played_both_in_leaderboard_winner_higher(self):
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

'''
    def test_match_played_both_in_leaderboard_loser_higher(self):
        winner = "Beta"
        loser = "Alpha"
        ladder = ["Gamma", "Alpha", "Beta", "Delta"]
        expected = ["Gamma", "Beta", "Alpha", "Delta"]

        new_ladder = match_played(winner, loser, ladder)
        self.assertListEqual(expected, new_ladder)

    def test_match_played_winner_in_leaderboard_loser_not_in_leaderboard(self):
        winner = "Alpha"
        loser = "Beta"
<<<<<<< HEAD
        ladder = ["Gamma", "Sigma", "Delta"]
        new_ladder = match_played(winner, loser, ladder)       
        self.assertEqual("Alpha", new_ladder[3])
        self.assertEqual("Beta", new_ladder[4])
=======
        ladder = ["Gamma", "Alpha", "Delta"]
        expected = ["Gamma", "Alpha", "Delta", "Beta"]

        new_ladder = match_played(winner, loser, ladder)
        self.assertListEqual(expected, new_ladder)

    def test_match_played_winner_not_in_leaderboard_loser_in_leaderboard(self):
        winner = "Alpha"
        loser = "Beta"
        ladder = ["Gamma", "Beta", "Delta"]
        expected = ["Gamma", "Alpha", "Beta", "Delta"]

        new_ladder = match_played(winner, loser, ladder)
        self.assertListEqual(expected, new_ladder)

    def test_match_played_neither_in_leaderboard(self):
        winner = "Alpha"
        loser = "Beta"
        ladder = ["Gamma", "Delta"]
        expected = ["Gamma", "Delta", "Alpha", "Beta"]

        new_ladder = match_played(winner, loser, ladder)
        self.assertListEqual(expected, new_ladder)
'''
>>>>>>> 9b0d9093b07217b7579e3615d00c1a4f9b044c67

if __name__ == "__main__":
    unittest.main()
