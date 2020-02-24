#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:26:42 2020

@author: aantoniadis
"""


import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import sys
from PyAstronomy import pyasl



def read_data(fname):
    
#    if np.shape(i)==(2,):
#        i=i[0]
    flux = fits.getdata(fname)
    hdr = fits.getheader(fname)
    w0, dw, N = hdr['CRVAL1'], hdr['CDELT1'], hdr['NAXIS1']
    wavelength = w0 + dw * np.arange(N)
    
    return wavelength, flux



waveline = float(sys.argv[1])
space =  float(sys.argv[2])

nirspectralist = np.loadtxt('nirspectralist.dat', dtype=str)



i=0

for item in nirspectralist:
    i=i+1
    
    wavelength, flux = read_data(item)
     #wavelength, flux = cut_data(wavelength, flux, waveline-space, waveline+space)
     
    set_res = 10
    #plt.figure()

    plt.subplot(2,2,i) 
    plt.title(item)
    plt.plot(wavelength, flux)
    plt.axvline(waveline, linestyle='--', color='C3')
    plt.axvline(waveline-space, color='C2')
    plt.axvline(waveline+space, color='C2')
    plt.xlim([waveline-space, waveline+space])
    plt.ylim([0.6,1.7])
    plt.rcParams["axes.spines.right"] = True
    plt.rcParams["axes.spines.top"] = True
    plt.subplots_adjust(top=0.92, bottom=0.11,left=0.11,right=0.99,hspace=0.3)
    
#    plt.xlabel(r"Wavelength [$\AA$]",fontsize=set_res*1.3)
#    plt.ylabel("Flux",fontsize=set_res*1.3)
#    plt.tick_params(axis='both',labelsize=set_res*1.3)
#    plt.plot(clip_box=True, clip_on=True)
#    plt.tight_layout()
#    plt.savefig('name.png')
plt.show()


