from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
         # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostoskori = {}
       

    def tavaroita_korissa(self):
            # kertoo korissa olevien tavaroiden lukumäärän
            # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
            # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
            tavaroita = 0
            for i in list(self.ostoskori):
                tavaroita += self.ostoskori[i].lukumaara()
            return tavaroita 

       

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        summa = 0
        for i in list(self.ostoskori):
            summa += self.ostoskori[i].hinta()
        return summa

        
    def lisaa_tuote(self, lisattava: Tuote):
        ostosolio =Ostos(lisattava)
        tuotteennimi = ostosolio.tuotteen_nimi()      

        if tuotteennimi in self.ostoskori.keys():
            self.ostoskori[tuotteennimi].muuta_lukumaaraa(1)
        else:
            self.ostoskori[tuotteennimi] = ostosolio
         
    def tuotteen_nimi(self):
        return self.tuote.nimi()
        
    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        tuotteennimi = poistettava.nimi()
        if tuotteennimi in self.ostoskori.keys():
            self.ostoskori[tuotteennimi].muuta_lukumaaraa(-1)

            if self.ostoskori[tuotteennimi].lukumaara()==0:
                del self.ostoskori[tuotteennimi]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostoskori.clear()
        

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        lista = []
        for key, value in self.ostoskori.items():
            lista.append((key,value.lukumaara()))
        return lista
        
      
