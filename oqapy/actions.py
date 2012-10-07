# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

src_name = get.srcNAME()
src_version = get.srcVERSION()

def install():
    for fi in ["*.py", "*.qm", "*.pro", "*.ts", src_name]:
        pisitools.insinto("/usr/share/%s-%s" % (src_name, src_version), fi)
    pisitools.insinto("/usr/share/%s-%s/medias" % (src_name, src_version), "medias/*")
    pisitools.insinto("/usr/share/%s-%s/configPages" % (src_name, src_version), "configPages/*")
    pisitools.insinto("/usr/share/%s-%s/VWidgets" % (src_name, src_version), "VWidgets/*")
    pisitools.dosed(src_name + ".desktop", "_ic_48", ".png")
    pisitools.dosed(src_name + ".desktop", "^(Version).*", r"\1=%s" % get.srcVERSION())
    pisitools.insinto("/usr/share/applications", "*.desktop")
    pisitools.dosym("/usr/share/%s-%s/medias/oqapy_ic_48.png" % (src_name, src_version), "/usr/share/pixmaps/%s.png" % src_name)
    pisitools.dosym("/usr/share/%s-%s/%s" % (src_name, src_version, src_name), "/usr/bin/%s" % src_name)
    pisitools.dodoc("doc/README")
