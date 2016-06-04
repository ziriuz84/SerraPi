# coding=utf-8

import time
import Adafruit_DHT


class SensoreTRH:

    def __init__(self, Type="DHT11", Pin=4):
        """
        Funzione di inizializzazione

        Inizializza la classe e i suoi attributi

        Args:
            Type: il tipo di sensore
            Pin: Il pin su cui viene letto il sensore
        """
        self.T = 0.0
        self.RH = 0.0
        self.Type = Type
        self.Pin = Pin
        self.DHT_TYPE = ""

    def SelectType(self):
        """
        Funzione di selezione del tipo di sensore

        Seleziona il tipo di sensore e inizializza il tipo giusto
        """
        if self.Type == "DHT11":
            self.DHT_TYPE = Adafruit_DHT.DHT11

    def Misure(self, con):
        """
        Funzione di misura

        Legge il valore del sensore ogni secondo per  5 volte e ne calcola la
        media, inserendo i valori nel database

        Args:
            con: connettore al database
        """
        RHMean = 0.0
        TMean = 0.0
        for i in range(0, 5):
            RHTemp, TTemp = Adafruit_DHT.read_retry(self.DHT_TYPE, self.Pin)
            RHMean += RHTemp
            TMean += TTemp
            time.sleep(1)
        RHMean /= 5
        TMean /= 5
        self.RH, self.T = RHMean, TMean
        Time = time.strftime("%H:%M:%S")
        TimeSQL = time.strftime("%Y-%m-%d %H:%M:%S")
        print 'Rilevazione delle ', Time
        print "Umidità relativa: ", self.RH, "%"
        print "Temperatura: ", self.T, " °C"
        with con:
            cur = con.cursor()
            sqlstatement = "INSERT INTO TRHInt(Time, T, RH) VALUES ('"
            sqlstatement += TimeSQL
            sqlstatement += "', "
            sqlstatement += str(self.T)
            sqlstatement += ", "
            sqlstatement += str(self.RH)
            sqlstatement += ");"
            cur.execute(sqlstatement)
