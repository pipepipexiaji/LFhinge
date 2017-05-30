# -*- coding: utf-8 -*-
# @Author: zyc
# @Date:   2017-05-29 08:50:21
# @Last Modified by:   pipepipexiaji
# @Last Modified time: 2017-05-29 20:17:50

import numpy as np
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import PSF, DCD, CRD
import MDAnalysis.analysis.rms

import sys,os
import matplotlib.pyplot as plt
#import pandas as pd

#u = mda.Universe('/Users/zyc/dropbox/sharedfolder/nanohinge-oxDNA/t300/pro_300.dat.xyz')
u = mda.Universe(sys.argv[1]) # Read traj file

atom_matrix = u.select_atoms('all')
means = np.zeros((len(atom_matrix), 3))

sumsq = np.zeros_like(means)

for k, ts in enumerate(u.trajectory):
    sumsq += (k/(k+1.0)) * (atom_matrix.positions - means)**2
    means[:] = (k*means + atom_matrix.positions)/(k+1.0)
rmsf = np.sqrt(sumsq.sum(axis=1)/(k+1.0))

#fig = plt.figure()
ax = plt.subplot(111)
ax.plot(ts, rmsf, 'r--', lw=2,  label="all")
#plt.plot(ts, rmsf)
#ax.legend(loc="best")
ax.set_xlabel("time (ps)")
ax.set_ylabel(r"rmsf ($\AA$)")
ax.figure.savefig("rmsf_all_t300i50.png")
plt.draw()





