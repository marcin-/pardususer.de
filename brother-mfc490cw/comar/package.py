#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/share/cups/model/brmfc490cw.ppd"):
        os.system("/usr/local/Brother/Printer/mfc490cw/cupswrapper/cupswrappermfc490cw -i")

def preRemove():
    if os.path.exists("/usr/share/cups/model/brmfc490cw.ppd"):
        os.system("/usr/local/Brother/Printer/mfc490cw/cupswrapper/cupswrappermfc490cw -e")
