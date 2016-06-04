import sys
import ConfigParser
import MySQLdb as mdb

# TODO Far diventare questa parte una funzione (o una classe)

Config = ConfigParser.ConfigParser()
e = ""
DebugPrint = ""
try:
    Config.read("./CONFIG")
    print 1
except e:
    print "Errore nell'apertura del file"
    print "Tipo di errore:"
    print e
    sys.exit("Controlla il file CONFIG e riavvia il programma")


def ConfigSectionMap(section):
    """
    Lettura dei file di configurazione

    Legge il file di configurazione nella sezione prescelta

    Args:
        section:    La sezione da ricercare

    Returns:
        Un dizionario con il valore della sezione prescelta
    """
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
    """
    Funzione di inizializzazione del programma

    Inizializza il database e le funzioni principali del programma

    Args:
        DBPosition: La posizione del server MySQL
        DBUser: L'utente del database
        DBPassword: La password per accedere al database
        DBName: Il nome del database

    Raises:
        mdb.Error, e
    """
    try:
        con = mdb.connect(DBPosition, DBUser, DBPassword, DBName)
        with con:
            cur = con.cursor()
            cur.execute("SHOW TABLE STATUS FROM testdb")
            if (cur.rowcount < 1):
                TRHInt = "CREATE TABLE TRHInt("
                TRHInt += "Id INT PRIMARY KEY AUTO_INCREMENT, "
                TRHInt += "Time DATETIME, "
                TRHInt += "T FLOAT, "
                TRHInt += "RH FLOAT"
                TRHInt += ");"
                cur.execute(TRHInt)
            return con
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
