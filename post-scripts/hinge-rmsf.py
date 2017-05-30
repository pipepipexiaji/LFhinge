# -*- coding: utf-8 -*-
# @Author: zyc
# @Date:   2017-05-29 08:50:21
# @Last Modified by:   pipepipexiaji
# @Last Modified time: 2017-05-29 22:45:07

import numpy as np
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import PSF, DCD, CRD
from MDAnalysis.analysis import rms


import sys,os
import matplotlib.pyplot as plt
#import pandas as pd

#u = mda.Universe("/Universe/zyc/dropbox/sharedfolder/nanohinge-oxDNA/t300/pro_300.pdb","/Users/zyc/dropbox/sharedfolder/nanohinge-oxDNA/t300/pro_300.dat.xyz")
u = mda.Universe(sys.argv[1], sys.argv[2]) # Read traj file
#[1]: pdb; [2]:xyz

al = u.select_atoms('segid C or segid A')
means = np.zeros((len(u.trajectory), 3))
sumsq = np.zeros_like(means)
output = open("./rmsf.dat", "w")

#for ts in enumerate(u.trajectory):

for k,ts in enumerate(u.trajectory):
    sumsq += (k/(k+1.0)) * (atom_matrix.positions - means)**2
    means[:] = (k*means + atom_matrix.positions)/(k+1.0)

rmsf = np.sqrt(sumsq.sum(axis=1)/(k+1.0))



print >>output, np.ndarray.all(rmsf)
output.close()

#fig = plt.figure()
ax = plt.subplot(111)
ax.plot(ts.frame, rmsf, 'r--', lw=2,  label="all")
#plt.plot(ts, rmsf)
ax.legend(loc="best")
ax.set_xlabel("time (ps)")
ax.set_ylabel(r"rmsf ($\AA$)")
ax.figure.savefig("rmsf_all_t300i50.png")
plt.draw()
print (ts)


########################################
############# RMSD ##################

rd= rms.RMSD(al, filename=sys.argv[3])
rd.run()
rd.save()

rmsd=rd.rmsd.T
time=rmsd[1]

import  seaborn.apionly as sns

plt.style.use('ggplot')
sns.set_style('ticks')

fig=plt.figure(figuresize=(6, 6))
ax=fig.add_subplot(111)
ax.plot(time, rmsd[2], 'b--', linewidth=2, label="All")
ax.fill_between(protein.atoms.ids, R.rmsf, color="red", alpha=0.1)
sns.despine(ax=ax, offset=10)
sns.despine(ax=ax, offset=10)
ax.set_xlabel("Time (ps)")
ax.set_ylabel("RMSD ($\AA$)")
fig.savefig()