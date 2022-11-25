import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_parametreilla(self):
      
      
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
    

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_kaksi_eri_tuotetta(self):

       
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id ==2:
                return 15

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "vehnäjauho", 7)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote


        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

       
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 12)
    

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_kaksi_samaa_tuotetta(self):
  
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id ==2:
                return 15

   
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "vehnäjauho", 7)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

     
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

   
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 14)
    

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_tuote_loppu_toinen_varastossa(self):

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id ==2:
                return 15
            if tuote_id ==3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vehnäjauho", 7)
            if tuote_id == 3:
                return Tuote(3, "suola", 2)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

 
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")


        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 7)
    


    def test_aloita_asiointi_nollaa_edellisetn_ostoksen_tiedot(self):

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id ==2:
                return 15
            if tuote_id ==3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vehnäjauho", 7)
            if tuote_id == 3:
                return Tuote(3, "suola", 2)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 12)


        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
    

    def test_uusi_viitenumero_vaaditaan_jokaiselle_asioinnille(self):

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id ==2:
                return 15
            if tuote_id ==3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vehnäjauho", 7)
            if tuote_id == 3:
                return Tuote(3, "suola", 2)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 7)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
    

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("maija", "54321")
        self.pankki_mock.tilisiirto.assert_called_with('maija', 42, '54321', '33333-44455', 5)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("helvi", "541234")
        self.pankki_mock.tilisiirto.assert_called_with('helvi', 42, '541234', '33333-44455', 7)
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)
   
      



    def test_poista_korista(self):

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id ==2:
                return 15
            if tuote_id ==3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "vehnäjauho", 7)
            if tuote_id == 3:
                return Tuote(3, "suola", 2)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

 
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(2)
        kauppa.tilimaksu("pekka", "12345")


        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)




       

       
