#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

# Package Name : cuneiform
# Version : 1.1.0
# Summary : A commandline OCR system for more than 20 languages

def setup():
    # fix libdir for x86_64
    pisitools.dosed("install_files.cmake", "(set\(LIBDIR \"lib)(64)(\"\))", r"\1\3")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/usr", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dodoc("readme.txt")
    shelltools.cd("build")
    cmaketools.install()
 