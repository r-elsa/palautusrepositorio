from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self,query = All()):
        self.query_olio = query
     
    def build(self):
        return self.query_olio

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.query_olio))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.query_olio))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.query_olio))