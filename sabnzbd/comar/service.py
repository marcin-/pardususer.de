#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/licenses/gpl-3.0.txt

from comar.service import *

serviceType="server"
serviceDesc = _({"en": "sabnzbd",
                 "tr": "sabnzbd",
                 "fr": "sabnzbd"})

@synchronized
def start():
    startService(command="/usr/bin/sabnzbd",
                 args="start",
                 pidfile="/var/run/sabnzbd.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/sabnzbd",
                args="stop",
                donotify=True)
                
def status():
    return isServiceRunning("/var/run/sabnzbd.pid")
