#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("furiusisomount", "src", "/usr/share/furiusisomount/src")

def install():
    pisitools.dobin("furiusisomount")
    pisitools.dodoc("doc/*")
    for i in ["pix", "res", "src"]: pisitools.insinto("/usr/share/furiusisomount/%s" % i, "%s/*" % i)
    for i in ["bg", "da", "de", "el", "es", "fr", "hrx", "it", "nl", \
              "pl", "pt", "pt_BR", "ru", "sl", "sv", "tr", "zh_CN"]:
        pisitools.insinto("/usr/share/locale/%s/LC_MESSAGES" %i, "locale/%s/LC_MESSAGES/*" % i)