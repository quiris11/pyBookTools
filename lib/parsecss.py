#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of epubQTools, licensed under GNU Affero GPLv3 or later.
# Copyright © Robert Błaut. See NOTICE for more information.
#

from __future__ import print_function
import os
import tinycss

parser = tinycss.make_parser()
with open(os.path.join(os.path.expanduser('~'), 'style.css')) as f:
    content = f.read()
# print(content)
ss = parser.parse_stylesheet(content)
# print(ss)
for r in ss.rules:
    for d in r.declarations:
        if d.name == 'font-family':
            for t in d.value:
                if t.type == 'STRING' or t.type == 'IDENT':
                    print(r.selector, d.name, t.type, t.value)