import unittest
from table_tennis_ladder import match_played

class TestMatchCreate(unittest.TestCase):
    def test_both_players_on_winner_ahead(self):
        winner = "Ben"
        loser = "Dan Rathbone"
        ladder = ["Ben", "Dan Rathbone"]
        new_ladder = match_played(winner, loser, ladder)
        self.assertEqual("Ben", new_ladder[0]) 

    def test_both_players_on_loser_ahead(self):
        loser = "Ben"
        winner = "Dan Rathbone"
        ladder = ["Ben", "Dan Rathbone"]
        new_ladder = match_played(winner, loser, ladder)
        self.assertEqual("Dan Rathbone", new_ladder[0]) 

if __name__ == '__main__':
    unittest.main()
