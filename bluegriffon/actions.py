#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("tar -jxvf %s-%s-Linux-%s.tar.bz2" % (get.srcNAME(), get.srcVERSION(), get.ARCH().replace("i6",  "x")))

def install():
    pisitools.insinto("/opt/%s" % get.srcNAME(), "%s/*" % get.srcNAME())
