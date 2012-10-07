#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/share/cups/model/brdcp350c.ppd"):
        os.system("/usr/local/Brother/Printer/dcp350c/cupswrapper/cupswrapperdcp350c -i")

def preRemove():
    if os.path.exists("/usr/share/cups/model/brdcp350c.ppd"):
        os.system("/usr/local/Brother/Printer/dcp350c/cupswrapper/cupswrapperdcp350c -e")
