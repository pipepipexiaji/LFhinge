# -*- coding: utf-8 -*-
# @Author: zyc
# @Date:   2017-05-27 10:25:53
# @Last Modified by:   zyc
# @Last Modified time: 2017-05-28 00:04:00
# Usage: python rmsd.py dir/pro*.dat.xyz

import numpy as np
import MDAnalysis
from MDAnalysis.tests.datafiles import PSF, DCD

import os
import os.path
import sys
import matplotlib.pyplot as plt

## Load xyz-trajectory file
# if len(sys.argv) > 1:
#    base.Logger.log("Usage is %strajectory" % sys.argv[0], base.Logger.CRITICAL)
#    sys.exit()

u = MDAnalysis.Universe("300i65/pro_65.dat.xyz")
all = u.select_atoms("all")

time = len(u.trajectory)
Rgyr = []
RMSF = []
for ts in u.trajectory:
   Rgyr.append((u.trajectory.time, all.radius_of_gyration()))
Rgyr = np.array(Rgyr)

ax = plt.subplot(111)
ax.plot(Rgyr[:,0], Rgyr[:,1], 'r--', lw=2, label=r"$R_G$")
ax.set_xlabel("time (ps)")
ax.set_ylabel(r"radius of gyration $R_G$ ($\AA$)")
ax.figure.savefig("Rgyr.pdf")
plt.draw()

#### RMSF ####
##############

