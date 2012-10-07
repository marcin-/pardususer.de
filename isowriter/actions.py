#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="isowriter-"+get.srcVERSION()


def install():
    pisitools.domo("po/de.po","de","isowriter.mo")
    pisitools.domo("po/nl.po","nl","isowriter.mo")
    pisitools.domo("po/fr.po","fr","isowriter.mo")
    pisitools.domo("po/tr.po","tr","isowriter.mo")
    pisitools.domo("po/es.po","es","isowriter.mo")
    pisitools.domo("po/pl.po","pl","isowriter.mo")
    pisitools.domo("po/ru.po","ru","isowriter.mo")


    pisitools.dobin("isowriter")

    pisitools.dodoc("COPYING","TODO","dependencies.txt")

    pisitools.dolib("lib/*","/usr/lib/isowriter/")

    pisitools.insinto("/usr/share/","share/*")