#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.insinto("/opt/mediathek","*")
	#pisitools.insinto("/opt/mediathek","/Copyright")
	#pisitools.insinto("/opt/mediathek","/lib")
	#pisitools.insinto("/opt/mediathek","Bitte_lesen.txt")
	#pisitools.insinto("/opt/mediathek","Kurzanleitung.pdf")
	#pisitools.insinto("/opt/mediathek","make.txt")
	#pisitools.insinto("/opt/mediathek","Mediathek.jar")
	#pisitools.insinto("/opt/mediathek","Mediathek_2.4.0.zip")
	#pisitools.insinto("/opt/mediathek","releases.txt")
