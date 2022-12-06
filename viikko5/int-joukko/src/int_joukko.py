class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvu=5):
        self.kapasiteetti = kapasiteetti
        self.kasvu=kasvu
        self.joukko = []
       

    def kuuluu(self, alkio):
        return alkio in self.joukko


    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            if self.kapasiteetti - 1 >= self.mahtavuus():
                self.kapasiteetti += self.kasvu

                joukko = []
                for i in self.joukko:
                    joukko.append(i)
                joukko.append(alkio)
                self.joukko = joukko
            else:
                self.joukko.append(alkio)
            
            return True
        return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            self.joukko.remove(alkio)
            return True
        return False
    
    def mahtavuus(self):
        return len(self.joukko)

    def to_int_list(self):
        return self.joukko

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        for i in a.to_int_list():
            yhdiste_joukko.lisaa(i)
        for i in b.to_int_list():
            yhdiste_joukko.lisaa(i)
        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                leikkaus_joukko.lisaa(i)
        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        for i in a.to_int_list():
            if not b.kuuluu(i):
                erotus_joukko.lisaa(i)
        return erotus_joukko

    def __str__(self):
        if len(self.joukko)<1:
            return "{}"
        return str(set(self.joukko))



