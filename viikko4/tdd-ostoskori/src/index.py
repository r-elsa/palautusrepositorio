# testikoodi tänne jos tarvetta
from tuote import Tuote
from ostos import Ostos
from ostoskori import Ostoskori


def init():
    tuote = Tuote("valion plusmaito", 0.80)
    tuote2 = Tuote("vehnäjauhoja", 0.55)
    

    ostoskori = Ostoskori()
    print(ostoskori.tavaroita_korissa())
    ostoskori.lisaa_tuote(tuote)
    ostoskori.lisaa_tuote(tuote2)
    print(ostoskori.ostokset()[0])


if __name__=="__main__":
    init()