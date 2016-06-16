#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from functions import ConfigSectionMap, Initialize
import SensoreTRH

DBPosition = ConfigSectionMap("DATABASE")['posizione']
DBUser = ConfigSectionMap("DATABASE")['utente']
DBPassword = ConfigSectionMap("DATABASE")['password']
DBName = ConfigSectionMap("DATABASE")['nome']
con = Initialize(DBPosition, DBUser, DBPassword, DBName)
PinTInt = ConfigSectionMap("PIN")['temperaturainterna']
SensoreTInt = ConfigSectionMap("PIN")['sensoretemperaturainterna']
GPIO.setmode(GPIO.BCM)
SensoreInterno = SensoreTRH.SensoreTRH(SensoreTInt, PinTInt)
SensoreInterno.SelectType()
while True:
    SensoreInterno.Misure(con)
    time.sleep(10)
GPIO.cleanup()
