from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdulist = fits.open('../solar_spectra/vesta_harps_comb_rv.fits')

print(hdulist)
hdu = hdulist[0]
crval = hdu.header['CRVAL1']

cdel = hdu.header['CDELT1']

size = hdu.header['NAXIS1']

wavelength = crval + cdel * np.arange(size)

data_med = np.median(hdulist[0].data)


plt.xlabel("wavelength")
plt.ylabel("norm. flux")

plt.plot(wavelength, hdulist[0].data / data_med)
plt.show()
