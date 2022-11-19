import requests
class Player:
    def __init__(self, name,nationality, team, goals, assists):
        self.name = name
        self.nationality =nationality,
        self.team = team
        self.goals=goals
        self.assists=assists
        self.tot = self.assists+self.goals
    
    def __gt__(self, other):
        return self.tot < other.tot
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.tot:2} "


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []
        self.do = self.get_players(self.url)
    
        
    def get_players(self,url):
        response = requests.get(url).json()
       
        for p in response:
            player = Player(
                        p['name'],
                        p['nationality'],
                        p['team'],
                        p['goals'],
                        p['assists'])
            self.players.append(player)
    
    def __str__(self):
        return (f"f{[i for i in self.players]}")
     
           

class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
    
             
    
    def top_scorers_by_nationality(self,n):
        res = []
        for i in self.reader.players:
            if i.nationality[0] == n:
                res.append(i)
        res.sort()
        return res

      
    



    

          
      