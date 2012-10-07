#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.dosym("/usr/lib/libpopt.so.0.0.0", "/usr/libpopt.so.0")

    pisitools.insinto("/usr/share/cups/model", "usr/share/cups/model/canonmp600.ppd")

    pisitools.dolib_so("usr/lib/libcnbpcmcm295.so.6.50.1")
    pisitools.dolib_so("usr/lib/libcnbpcnclapi295.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclbjcmd295.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpcnclui295.so.3.3.0")
    pisitools.dolib_so("usr/lib/libcnbpess295.so.3.0.9")
    pisitools.dolib_so("usr/lib/libcnbpo295.so.1.0.2")

    pisitools.dosym("/usr/lib/libcnbpcmcm295.so.6.50.1", "/usr/lib/libcnbpcmcm295.so.6")
    pisitools.dosym("/usr/lib/libcnbpcmcm295.so.6.50.1", "/usr/lib/libcnbpcmcm295.so")
    pisitools.dosym("/usr/lib/libcnbpcnclapi295.so.3.3.0", "/usr/lib/libcnbpcnclapi295.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclapi295.so.3.3.0", "/usr/lib/libcnbpcnclapi295.so")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd295.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd295.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclbjcmd295.so.3.3.0", "/usr/lib/libcnbpcnclbjcmd295.so")
    pisitools.dosym("/usr/lib/libcnbpcnclui295.so.3.3.0", "/usr/lib/libcnbpcnclui295.so.3")
    pisitools.dosym("/usr/lib/libcnbpcnclui295.so.3.3.0", "/usr/lib/libcnbpcnclui295.so")
    pisitools.dosym("/usr/lib/libcnbpess295.so.3.0.9", "/usr/lib/libcnbpess295.so.3")
    pisitools.dosym("/usr/lib/libcnbpess295.so.3.0.9", "/usr/lib/libcnbpess295.so")
    pisitools.dosym("/usr/lib/libcnbpo295.so.1.0.2", "/usr/lib/libcnbpo295.so.1")
    pisitools.dosym("/usr/lib/libcnbpo295.so.1.0.2", "/usr/lib/libcnbpo295.so")
    

    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cifmp600.conf")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnb_2950.tbl")
    pisitools.insinto("/usr/lib/bjlib", "usr/lib/bjlib/cnbpname295.tbl")

    for f in shelltools.ls("usr/local/bin"):
        pisitools.insinto("/usr/local/bin", "usr/local/bin/%s" % f)

    for f in shelltools.ls("usr/local/share/cngpijmonmp600/pixmaps"):
        pisitools.insinto("/usr/local/share/cngpijmonmp600/pixmaps", "usr/local/share/cngpijmonmp600/pixmaps/%s" % f)

    for f in shelltools.ls("usr/local/share/printuimp600"):
        pisitools.insinto("/usr/local/share/printuimp600", "usr/local/share/printuimp600/%s" % f)
