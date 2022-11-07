import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    

    def test_team(self):
        pl= self.statistics.team("AAA")
        self.assertEqual(pl, [])

        
    def test_searchplayer(self):
        pl= self.statistics.search("Lemieux")
        self.assertEqual(str(pl), 'Lemieux PIT 45 + 54 = 99')

        
    def test_searchplayer_doesnotexist(self):
        pl= self.statistics.search("fdgf")
        self.assertEqual(pl, None) 

    
    def test_sort_by_points(self):
        pl= self.statistics.top(1)
      
        self.assertEqual(pl[0].name, 'Gretzky') 

