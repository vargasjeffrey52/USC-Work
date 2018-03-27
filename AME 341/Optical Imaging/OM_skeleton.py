import numpy as np
import matplotlib.pyplots as plt
import glob


working_dir = r'Images\\001\\'


def loadImg(Dir):
    return glob.glob(working_dir + 'img*.jpg')


def IaMean(Ia, Bx, By):
    mean = 0
    for k in range(Bx):
        for l in range(By):
            mean += Ia[k, l]
    return (1 / (Bx * By)) * mean


def IbMean(Ib, Bx, By, i=0, j=0):
    mean = 0
    for k in range(Bx):
        for l in range(By):
            mean += Ib[k + i, l + j]
    return (1 / (Bx * By)) * mean


def correalation(Ia, Ib, Bx, By, Sx, Sy):

    numerator = 0
    denom1 = 0
    denom2 = 0
    IaBar = IaMean(Ia, Bx, By)

    for i in range(Sx - Bx):
        for j in range(Sy - By):
            for k in range(Bx):
                for l in range(By):
                    numerator += ((Ia[k,l] - IaBar) * (Ib[k + i, l + j] - IbMean(Ib, Bx, By, i, j)))
                    denom1 += (Ia[k, l] - IaBar)**2
                    denom2 += (Ib[k + i, l + j] - IbMean(Ib, Bx, By, i, j))**2
    Corr = numerator/np.sqrt(denom1 * denom2)

    return Corr

def searchBox(Ia, Ib, Bx, By, Sx=4 * Bx, =4 * By):
    return None