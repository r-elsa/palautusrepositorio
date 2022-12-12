
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or
from query_builder import QueryBuilder
from stats import Statistics


def main():
  
    url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    #matcher = query.build()
    #matcher = query.playsIn("NYR").build()
    #matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()

    matcher = (
      query
      .playsIn("NYR")
      .hasAtLeast(10, "goals")
      .hasFewerThan(20, "goals")
      .build()
    )

    for player in stats.matches(matcher):
        print(player)


    """ matcher = Or(
    HasAtLeast(45, "goals"),
    HasAtLeast(70, "assists")
    ) """

    """ matcher3 = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
    )
    """
    """  matcher = And(
        HasFewerThan(5, "goals"),
        HasFewerThan(5, "assists"),
        PlaysIn("PHI")
    ) """ 

    """ matcher1 = And(
    Not(HasAtLeast(1, "goals")),
    PlaysIn("NYR")
    )
     """
    """  matcher2 = And(
    HasFewerThan(1, "goals"),
    PlaysIn("NYR")
    ) """


    """ matcher2 = And(
    Not(HasAtLeast(1, "goals")),
    PlaysIn("NYR")
    ) """ 

    """ filtered_with_all = stats.matches(All())
    print(len(filtered_with_all)) """

    """ for player in stats.matches(matcher3):
        print(player) """ 
    
   


if __name__ == "__main__":
    main()
