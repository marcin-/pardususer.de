#!/usr/bin/python 

import os
from comar.service import * 

serviceType = "server" 
serviceDesc = _({"en": "vnstat daemon"}) 

PIDFILE = "/var/run/vnstat.pid"

@synchronized 
def start(): 
    startService(command="/usr/sbin/vnstatd",
                 args="--pidfile %s --daemon" % PIDFILE,
                 makepid=True, 
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized 
def stop(): 
    stopService(pidfile=PIDFILE,
                donotify=True)
    try:
        os.unlink(PIDFILE)
    except:
        pass

def status(): 
    return isServiceRunning(PIDFILE)
