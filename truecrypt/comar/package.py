#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postRemove():
    os.system("pkexec --user root /usr/bin/truecrypt-uninstall.sh")
