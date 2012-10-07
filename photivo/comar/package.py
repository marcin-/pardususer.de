#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    ls = os.listdir('/home')
    for it in ls:
        if os.path.isdir('/home/' + it):
            dir = '/home/' + it + '/.gimp-2.6/plug-ins'
            if os.path.isdir(dir) and not os.path.isfile(dir + '/ptGimp'):
                os.symlink('/usr/lib/gimp/2.0/plug-ins/ptGimp',  dir + '/ptGimp')
