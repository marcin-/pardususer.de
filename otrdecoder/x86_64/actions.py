#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="otrdecoder-bin-x86_64-unknown-linux-gnu-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/opt/otrdecoder", "*")
    pisitools.dosym ("/opt/otrdecoder/otrdecoder-gui","/usr/bin/otrdecoder-gui")
    pisitools.dosym ("/opt/otrdecoder/otrdecoder","/usr/bin/otrdecoder")
