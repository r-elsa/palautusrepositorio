class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_komento = None

    def miinus(self, arvo, komento):
        self.tulos = self.tulos - arvo
        self.edellinen_komento = komento
      

    def plus(self, arvo, komento):
        self.tulos = self.tulos + arvo
        self.edellinen_komento = komento
      

    def nollaa(self, komento):
        self.tulos = 0
        self.edellinen_komento = komento


    def aseta_arvo(self, arvo):
        self.tulos = arvo
    
    def kumoa(self):
        if self.edellinen_komento is not None:
            self.edellinen_komento.kumoa()
            self.edellinen_komento = None
        else:
            pass
    
    def get_tulos(self):
        return self.tulos
   


      
class Summa:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka, syote):
        self.sovelluslogiikka= sovelluslogiikka
        self.syote = syote
        self.viimeisin_syote = None

    def suorita(self):
        self.viimeisin_syote = int(self.syote())
        self.sovelluslogiikka.plus(self.viimeisin_syote, self)
       
    
    def kumoa(self):
        self.sovelluslogiikka.miinus(self.viimeisin_syote, self)


class Erotus:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka, syote):
        self.sovelluslogiikka= sovelluslogiikka
        self.syote = syote
        self.viimeisin_syote = None

    def suorita(self):
        self.viimeisin_syote = int(self.syote())
        self.sovelluslogiikka.miinus(self.viimeisin_syote, self)
    
    def kumoa(self):
        self.sovelluslogiikka.plus(self.viimeisin_syote, self)

class Nollaus:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka, syote):
        self.sovelluslogiikka= sovelluslogiikka
        self.syote = syote
        self.viimeisin_syote = None

    def suorita(self):
        self.viimeisin_syote = self.sovelluslogiikka.get_tulos()
        self.sovelluslogiikka.nollaa(self)
    
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.viimeisin_syote)


class Kumoa:
    def __init__(self, sovelluslogiikka:Sovelluslogiikka, syote):
        self.sovelluslogiikka= sovelluslogiikka
        self.syote = syote
     
    def suorita(self):
        self.sovelluslogiikka.kumoa()
       


  