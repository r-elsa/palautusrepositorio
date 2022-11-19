from player import Player
import requests
import datetime 

  


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

   
    def filterFunc(player_dict):
        if player_dict['nationality']=='FIN':
            return True
        else:
            return False
                
            
         

    print(f"Players from FIN {datetime.datetime.now()}")


    players = filter(filterFunc, response)
    
    for p in players:
        player = Player(
                    p['name'],
                    p['team'],
                    p['goals'],
                    p['assists'])
          
        print(player.__str__())

if __name__ == "__main__":
    main()
