#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

# Package Name : flasm
# Version : 1.62
# Summary : Disassembler tool for SWF bytecode.

WorkDir="."

def build():
    autotools.make()

def install():
    pisitools.dobin("flasm")
    pisitools.dodoc("*.TXT")
