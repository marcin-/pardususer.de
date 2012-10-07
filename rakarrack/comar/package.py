#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import fileinput

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    users = []
    for line in fileinput.input('/etc/passwd', mode = 'r'):
        cols = line.split(':')
        if int(cols[2]) > 999 and cols[0] <> "nobody":
            users.append(cols[0])
    for line in fileinput.input('/etc/group',  inplace = 1):
        line = line.strip()
        if re.search('^jackuser',  line) == None:
            print(line)
        else:
            cols = line.split(':')
            jackusers = cols[3].split(',')
            for u in users:
                notjackuser = True
                for ju in jackusers:
                    if u == ju: notjackuser = False
                if notjackuser: jackusers.append(u)
            newline = '%s:%s:%s:' % (cols[0],  cols[1],  cols[2])
            for it in jackusers: 
                if newline[len(newline)-1] <> ':': newline += ','
                newline += it
            print(newline)
