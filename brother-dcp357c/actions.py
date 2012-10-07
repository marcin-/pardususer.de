#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

WorkDir = "brother-dcp350c"

def install():


    pisitools.dobin("usr/local/Brother/Printer/dcp350c/lpd/filterdcp350c", "/usr/local/Brother/Printer/dcp350c/lpd")
    pisitools.dobin("usr/local/Brother/Printer/dcp350c/lpd/brdcp350cfilter", "/usr/local/Brother/Printer/dcp350c/lpd")
    pisitools.dobin("usr/local/Brother/Printer/dcp350c/lpd/psconvertij2", "/usr/local/Brother/Printer/dcp350c/lpd")

    pisitools.dobin("usr/local/Brother/Printer/dcp350c/inf/setupPrintcapij", "/usr/local/Brother/Printer/dcp350c/inf")

    pisitools.dobin("usr/local/Brother/Printer/dcp350c/cupswrapper/cupswrapperdcp350c", "/usr/local/Brother/Printer/dcp350c/cupswrapper")
    pisitools.dobin("usr/local/Brother/Printer/dcp350c/cupswrapper/brcupsconfpt1", "/usr/local/Brother/Printer/dcp350c/cupswrapper")

    # Install bcm profiles

    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brio06aa.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brio06ab.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brio06ac.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brio06af.bcm")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brio06ag.bcm")

    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brdcp350cfunc")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brdcp350crc")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/brPrintListij2")
    pisitools.insinto("/usr/local/Brother/Printer/dcp350c/inf", "usr/local/Brother/Printer/dcp350c/inf/paperinfij2")

    # Install so file
    pisitools.dolib_so("usr/lib/libbrcompij2.so.1.0.2")

    pisitools.dosym("/usr/lib/libbrcompij2.so.1.0.2", "/usr/lib/libbrcompij2.so.1")
    pisitools.dosym("/usr/lib/libbrcompij2.so.1.0.2", "/usr/lib/libbrcompij2.so")

