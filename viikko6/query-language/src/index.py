
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan
from stats import Statistics

def main():
    url =  "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    """  matcher = And(
        HasFewerThan(5, "goals"),
        HasFewerThan(5, "assists"),
        PlaysIn("PHI")
    ) """ 

    matcher1 = And(
    Not(HasAtLeast(1, "goals")),
    PlaysIn("NYR")
)

    matcher2 = And(
    HasFewerThan(1, "goals"),
    PlaysIn("NYR")
)


    """ matcher = And(
    Not(HasAtLeast(1, "goals")),
    PlaysIn("NYR")
    ) """ 

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    for player in stats.matches(matcher1):
        print(player) 
    
    print(" ")

    for player in stats.matches(matcher2):
        print(player) 


if __name__ == "__main__":
    main()
