"""
agridies.py should ask on run "Do you need to run the initial setup"
if the user answers yes, this script should execute.
if the user answers no, we should assume we're already configured for this year
"""
import os.path
from datetime import datetime, tzinfo
from agridiesdb import dbsetup

def checkdb():
    dbname=("agridieslog-"+str(datetime.today().year)+".db")
    if os.path.isfile(dbname):
        print("DB Exists")
    else:
        print("DB Doesn't exist, running dbsetup")
        dbsetup()

def setstation():
    Ocall = input("What is your Station Callsign: ").upper()
    Ocat = input("What is your Category: ").upper()
    Osec = input("What is your Section: ").upper()

# Stretch goal - we should hook ourselves up to hamlib/rigctl
checkdb()
