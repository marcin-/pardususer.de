#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="otrdecoder-bin-linux-Ubuntu_8.04-i686-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/opt/otrdecoder", "*")
    pisitools.dosym ("/opt/otrdecoder/otrdecoder-gui","/usr/bin/otrdecoder-gui")
    pisitools.dosym ("/opt/otrdecoder/otrdecoder","/usr/bin/otrdecoder")
