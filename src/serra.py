#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from functions import ConfigSectionMap, Initialize
import SensoreTRH
import urwid
import thread


def exit(scelta):
    if scelta in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def interfaccia(con):
    print 1
    try:
        thread.start_new_thread(misura, (con, ))
    except:
        "errore nell'apertura dei thread"
    txt = urwid.Text(u"SerraPi 0.1")
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill, unhandled_input=exit)
    loop.run()


def misura(con):
    print 2
    PinTInt = ConfigSectionMap("PIN")['temperaturainterna']
    SensoreTInt = ConfigSectionMap("PIN")['sensoretemperaturainterna']
    GPIO.setmode(GPIO.BCM)
    SensoreInterno = SensoreTRH.SensoreTRH(SensoreTInt, PinTInt)
    SensoreInterno.SelectType()
    while True:
        SensoreInterno.Misure(con)
        time.sleep(10)
    GPIO.cleanup()

if __name__ == "__main__":
    DBPosition = ConfigSectionMap("DATABASE")['posizione']
    DBUser = ConfigSectionMap("DATABASE")['utente']
    DBPassword = ConfigSectionMap("DATABASE")['password']
    DBName = ConfigSectionMap("DATABASE")['nome']
    con = Initialize(DBPosition, DBUser, DBPassword, DBName)
    interfaccia(con)
