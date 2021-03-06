"""Boundary correction utilities."""

import numpy
from scipy.special import erf


def cut_and_normalise_gaussian(x, p, sigma, xmin=None, xmax=None):
    """Cut and normalise boundary correction for a Gaussian kernel.

    Parameters
    ----------
    x: numpy.array
        locations for normalisation correction

    p: numpy.array
        probability densities for normalisation correction

    sigma: float
        bandwidth of KDE

    xmin, xmax: float
        lower/upper prior bound
        optional, default None

    Returns
    -------
    p: numpy.array
        corrected probabilities

    """
    correction = numpy.ones_like(x)

    if xmin is not None:
        correction *= 0.5*(1 + erf((x - xmin)/sigma/numpy.sqrt(2)))
        correction[x < xmin] = numpy.inf
    if xmax is not None:
        correction *= 0.5*(1 + erf((xmax - x)/sigma/numpy.sqrt(2)))
        correction[x > xmax] = numpy.inf
    return p/correction
