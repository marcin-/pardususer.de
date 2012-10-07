#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/share/cups/model/brdcp145c.ppd"):
        os.system("/usr/local/Brother/Printer/dcp145c/cupswrapper/cupswrapperdcp145c -i")

def preRemove():
    if os.path.exists("/usr/share/cups/model/brdcp145c.ppd"):
        os.system("/usr/local/Brother/Printer/dcp145c/cupswrapper/cupswrapperdcp145c -e")
