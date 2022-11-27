from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        self.ostoksia={}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
            return (sum(self.ostoksia.values()))
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hintojensumma = sum(i.hinta() for i in self.ostoskori)
        return hintojensumma
        

    def lisaa_tuote(self, lisattava: Tuote):
        ostosolio =Ostos(lisattava)
        self.ostoskori.append(ostosolio)

        tuotenimi = ostosolio.tuotteen_nimi()

        if tuotenimi in self.ostoksia:
            self.ostoksia[tuotenimi] +=1
        else:
            self.ostoksia[tuotenimi]=1


    def tuotteen_nimi(self):
        return self.tuote.nimi()
        

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.ostoskori)
        
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
