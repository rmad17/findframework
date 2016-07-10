# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad
#
# Distributed under terms of the MIT license.

"""

"""
import os

direct = "/home/rmad/repos/testd/"
fpath = os.path.join(direct, "manage.py")
with open(fpath, "r") as f:
    contents = f.readlines()
    for line in contents:
        if 'from django' in line:
            print("Django Project Found. Yaaaaay!")
