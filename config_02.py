import numpy as np

# Set the seed for reproducibility
seed = 123457

Lside       = 20
alpha       = 0.2
beta        = 0.5
PixelNoise  = 0.01

# Setup for correlation function
nbin        = 4*Lside
ndata       = 4*Lside
rmax        = Lside*np.sqrt(2)

# Set number of simulations for summary-based inference
nsims        = 500

# Set ranges
nalpha       = 80
nbeta        = nalpha

alphamin     = 0.
alphamax     = 2.
betamin      = 0.2
betamax      = 0.8

# Construct filenames for output files
u = '_'
extra = '0' if alpha<1 else ''    
extraB = '0' if beta<1 else ''
runid   = str(Lside)+u+extraB+str(np.rint(10*beta).astype(int))+u+extra+str(np.rint(10*alpha).astype(int))+u+ \
    str(nalpha)+u+str(nbeta)+u+str(nsims)+u+str(nbin)+u+str(np.rint(100*PixelNoise).astype(int))+u+str(seed)
fileout = 'figures/Output'+runid
dataout = 'data/Data'+runid
simsout = 'data/Sims'+runid

from os import makedirs
makedirs("figures", exist_ok=True)
makedirs("data", exist_ok=True)

print('Figures saved at',fileout)
print('Simulations saved at',simsout)

# Set contour levels for plots (from Numerical Recipes 15.6)
contour_levels = [-9.21/2,-6.17/2,-4.61/2,-2.30/2,0]
