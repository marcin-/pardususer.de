#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    with open("/etc/passwd") as f:
        for line in f:
            cols = line.strip().split(':')
            if int(cols[2]) >999: os.system("pkexec --user %s milena_say skonfigurowane dla %s" % (cols[0], cols[0]))
