import sys
# import csv
import ConfigParser
import MySQLdb as mdb


Config = ConfigParser.ConfigParser()
try:
    Config.read("./CONFIG")
    print 1
except e:
    print "Errore nell'apertura del file"
    print "Tipo di errore:"
    print e
    sys.exit("Controlla il file CONFIG e riavvia il programma")


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s" % option)
            dict1[option] = None
    return dict1


def Initialize(DBPosition, DBUser, DBPassword, DBName):
    try:
        con = mdb.connect(DBPosition, DBUser, DBPassword, DBName)
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        ver = cur.fetchone()
        print "Database version: %s" % ver
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

