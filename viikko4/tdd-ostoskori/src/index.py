# testikoodi tänne jos tarvetta
from tuote import Tuote
from ostos import Ostos
from ostoskori import Ostoskori


def init():
    tuote = Tuote("valion plusmaito", 0.80)
    tuote2 = Tuote("vehnäjauhoja", 0.55)
    ostoskori = Ostoskori()
    ostoskori.lisaa_tuote(tuote2)
    ostoskori.lisaa_tuote(tuote2)
    ostoskori.lisaa_tuote(tuote)
    ostoskori.tyhjenna()
    print(ostoskori.ostokset())



if __name__=="__main__":
    init()