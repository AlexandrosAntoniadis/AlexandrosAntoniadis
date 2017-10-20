from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdulist = fits.open('vesta_harps_comb_rv.fits')

print(hdulist)
hdu = hdulist[0]
crval = hdu.header['CRVAL1']

cdel = hdu.header['CDELT1']

size = hdu.header['NAXIS1']

wavelength = crval + cdel * np.arange(size)

print("hello")

plt.xlabel("wavelength")
plt.ylabel("flux")

plt.plot(wavelength, hdulist[0].data)
plt.show()
