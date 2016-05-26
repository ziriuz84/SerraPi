# coding=utf-8

import time
import Adafruit_DHT


class SensoreTRH:

    def __init__(self, Type="DHT11", Pin=4):
        self.T = 0.0
        self.RH = 0.0
        self.Type = Type
        self.Pin = Pin
        self.DHT_TYPE = ""

    def SelectType(self):
        if self.Type == "DHT11":
            self.DHT_TYPE = Adafruit_DHT.DHT11

    def Misure(self):
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
        print 'Rilevazione delle ', time.strftime("%H:%M:%S")
        print "Umidità relativa: ", self.RH, "%"
        print "Temperatura: ", self.T, " °C"
