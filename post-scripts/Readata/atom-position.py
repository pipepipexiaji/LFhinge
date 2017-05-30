# -*- coding: utf-8 -*-
# @Author: pipepipexiaji
# @Date:   2017-05-29 17:41:45
# @Last Modified by:   pipepipexiaji
# @Last Modified time: 2017-05-29 17:46:11
# Split xyz of atoms for bio3d analysis

import numpy as np
import MDAnalysis as mda
import sys, os

u = mda.Universe(sys.argv[1])
r = u.atoms
pos = r.positions
out = open("atom-position.dat", "w")

for i in range(1, 2572):
   print >> out, pos[i]

out.close()
