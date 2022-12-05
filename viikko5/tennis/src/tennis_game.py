class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.helpdict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3 : "Forty", 4: "Fifty", "tied": "All", "deuce":"Deuce"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        elif player_name == "player2":
            self.m_score2 = self.m_score2 + 1


    def deuce(self):
        return self.helpdict["deuce"]

    def tied(self):
        return f"{self.helpdict[self.m_score1]}-All"
    
    
    def advantage(self, player):
        return  f"Advantage {player}"
    
    def win(self, player):
        return f"Win for {player}"         
 
    def not_deuce_tied_advantage_or_win(self):
        return f"{self.helpdict[self.m_score1]}-{self.helpdict[self.m_score2]}"
            
    
    def get_score(self):
    
        if self.m_score1 == self.m_score2:
            if self.m_score1==4 and self.m_score2==4:
                return self.deuce()
            else:
                return self.tied()
            
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            difference = self.m_score1-self.m_score2
            player = " "

            if difference > 0:
                player = "player1"
            else:
                player = "player2"

            if abs(difference) <2:
                return self.advantage(player)
            else:
                return self.win(player)
            
        else:
           return self.not_deuce_tied_advantage_or_win()
 
 
