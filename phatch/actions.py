#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules

# Package Name : phatch
# Version : 0.2.7.1
# Summary : Phatch is a simple to use cross-platform GUI Photo Batch Processor.

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
