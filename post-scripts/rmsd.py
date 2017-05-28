# -*- coding: utf-8 -*-
# @Author: zyc
# @Date:   2017-05-28 17:37:44
# @Last Modified by:   zyc
# @Last Modified time: 2017-05-28 18:02:57

import numpy as np
from numpy.linalg import norm
import MDAnalysis as mda
from MDAnalysis.tests.datafiles import PSF, DCD

import sys, os
import matplotlib.pyplot as plt
import re

u = mda.Universe(sys.argv[1]) #trajectory.dat.xyz

## print(u.atoms)
# <AtomGroup [<Atom 1: S of type S resid 1 and segid SYSTEM>, <Atom 2: O of type O resid 1 and segid SYSTEM>, <Atom 3: S of type S resid 1 and segid SYSTEM>, ..., <Atom 2570: O of type O resid 1 and segid SYSTEM>, <Atom 2571: K of type K resid 1 and segid SYSTEM>, <Atom 2572: O of type O resid 1 and segid SYSTEM>]>
##################################################################

def load(fileName)

