# @Author: zyc
# @Date:   2017-05-23 21:56:26
# @Last Modified by:   zyc
# @Last Modified time: 2017-05-23 23:50:54


#cd /Users/zyc/Dropbox/SharedFolder/NanoHinge_oxDNA

## Generate last_conf.dat.pdb
python /Users/zyc/Downloads/oxDNA/UTILS/traj2pdb_large.py ./last_conf.dat /Users/zyc/Documents/LFnanohinge/compiled-generator/cadnano.top

## Genarate traj.xyz

python /Users/zyc/Downloads/oxDNA/UTILS/traj2xyz.py pro*.dat /Users/zyc/Documents/LFnanohinge/compiled-generator/cadnano.top

cd ..
