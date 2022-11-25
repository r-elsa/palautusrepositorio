# testikoodi tänne jos tarvetta
from tuote import Tuote
from ostos import Ostos
from ostoskori import Ostoskori


def init():
    tuote = Tuote("valion plusmaito", 0.80)
    tuote2 = Tuote("vehnäjauhoja", 0.55)
    ostos = Ostos(tuote)
    ostos2 = Ostos(tuote2)
    print(ostos.tuote)
    print(ostos2.tuote)
    ostoskori = Ostoskori()
    print(ostoskori.tavaroita_korissa())


if __name__=="__main__":
    init()