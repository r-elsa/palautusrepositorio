import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(),0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        porkkana = Tuote("Porkkana", 7)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.hinta(),7)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        porkkana = Tuote("Porkkana", 7)
        salaatti = Tuote("Salaatti", 1.35)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(salaatti)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        porkkana = Tuote("Porkkana", 7)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuplasti_tuotteen_hinta(self):
        porkkana = Tuote("Porkkana", 7)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.hinta(),2*porkkana.hinta())

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):   
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(ostos[0],"Maito")
        self.assertEqual(ostos[1],1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 7)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()),1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_ostos_sama_nimi_lukumaara_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual((self.kori.ostokset()[0][0]),"Maito")
        self.assertEqual((self.kori.ostokset()[0])[1],2)
    

    def test_korissa_kaksi_tuotetta_ja_yhden_tuotteen_poistamisen_jalkeen_koriin_jaa_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual((self.kori.ostokset()[0][1]),1)
    
    def test_koriin_lisatty_tuote_ja_sama_tuote_poistetaan_kori_jalleen_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()),0)
    
    def test_koriin_lisatty_tuote_ja_sama_tuote_poistetaan_kori_jalleen_tyhja(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 7)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.kori.poista_tuote(porkkana)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()),0)
   



     
    




