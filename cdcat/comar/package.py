#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/lib/7z.so"):
        os.system("ln -s /usr/lib/p7zip/7z.so /usr/lib/7z.so")
