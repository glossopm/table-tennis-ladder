import unittest
from table_tennis_ladder import *


class TestAddNewPlayer(unittest.TestCase):

    def test_add_new_player_no_duplicates_no_invalid_chars(self):
        all_players = ["Gareth", "Melissa", "Harvey", "Beth"]
        new_players = ["John"]

        players, added, duplicates, failed = add_new_players_list(list(all_players), new_players)

        self.assertListEqual(new_players, added)
        self.assertListEqual(failed, [])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(players, all_players + new_players)

    def test_add_new_player_duplicate(self):
        all_players = ["Gareth", "Melissa", "Harvey", "Beth"]
        new_players = ["Gareth"]

        players, added, duplicates, failed = add_new_players_list(list(all_players), new_players)

        self.assertListEqual(added, [])
        self.assertListEqual(failed, [])
        self.assertListEqual(duplicates, ["Gareth"])
        self.assertListEqual(players, all_players)

    def test_add_new_player_invalid_chars(self):
        all_players = ["Gareth", "Melissa", "Harvey", "Beth"]
        new_players = ["!!--!/!%"]

        players, added, duplicates, failed = add_new_players_list(list(all_players), new_players)

        self.assertListEqual(added, [])
        self.assertListEqual(failed, ["!!--!/!%"])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(players, all_players)

    def test_add_multiple_players_no_duplicates_no_invalid_chars(self):
        all_players = ["Gareth", "Melissa", "Harvey", "Beth"]
        new_players = ["Bob", "Mary", "Owen"]

        players, added, duplicates, failed = add_new_players_list(list(all_players), new_players)

        self.assertListEqual(added, ["Bob", "Mary", "Owen"])
        self.assertListEqual(failed, [])
        self.assertListEqual(duplicates, [])
        self.assertListEqual(players, all_players + new_players)

    def test_add_multiple_players_duplicates_no_invalid_chars(self):
        all_players = ["Gareth", "Melissa", "Harvey", "Beth"]
        new_players = ["Bob", "Mary", "Melissa", "Jack", "Gareth"]

        players, added, duplicates, failed = add_new_players_list(list(all_players), new_players)

        self.assertListEqual(added, ["Bob", "Mary", "Jack"])
        self.assertListEqual(failed, [])
        self.assertListEqual(duplicates, ["Melissa", "Gareth"])
        self.assertListEqual(players, all_players + added)

    def test_add_multiple_players_duplicates_invalid_chars(self):
        all_players = ["Gareth", "Melissa", "Harvey", "Beth"]
        new_players = ["Bob", "Mary", "$$!!??", "Melissa", "Jack", "Gareth", "--%!!"]

        players, added, duplicates, failed = add_new_players_list(list(all_players), new_players)

        self.assertListEqual(added, ["Bob", "Mary", "Jack"])
        self.assertListEqual(failed, ["$$!!??", "--%!!"])
        self.assertListEqual(duplicates, ["Melissa", "Gareth"])
        self.assertListEqual(players, all_players + added)


if __name__ == "__main__":
    unittest.main()