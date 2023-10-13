from time import sleep
import threading as thr

from task_db.load_and_dump import Dump
from misc.shared.glob_dbs import *


g_localStoragePth = "tasks.db"
g_autoSavePeriod = 20
g_autoSaveThr: thr.Thread = None
g_autoSaveThrEvnt: thr.Event = thr.Event()


def StartPeriodicAutoSave():
    global g_autoSaveThr
    g_autoSaveThr = thr.Thread(
        target=PeriodicAutoSave,
        args=(g_autoSaveThrEvnt, g_autoSavePeriod,),
    )
    g_autoSaveThr.start()


def PeriodicAutoSave(evnt, period):
    count = 0
    while not evnt.is_set():
        if count == 0:
            print("PeriodicAutoSave", "(auto save!)")
            Dump(g_localStoragePth)
        count = (count + 1) % period
        sleep(1)
    print("AutoSave terminated")


def StopPeriodicAutoSave():
    if g_autoSaveThr is not None:
        g_autoSaveThrEvnt.set()
        g_autoSaveThr.join()
