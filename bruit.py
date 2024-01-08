import numpy as np


def ajout_bbag(signal, snr_db=10.0):
    '''
    Renvoie un nouveau signal bruite.
    snr_db = rapport signal bruit en db
    '''
    puissance_moy_signal = sum(x**2 for x in signal)/len(signal)
    snr_lin = 10**(snr_db/10)

    puissance_bruit = puissance_moy_signal / snr_lin

    bruit = np.random.normal(0, puissance_bruit**0.5, len(signal))

    res = []
    for i in range(len(bruit)):
        res.append(bruit[i] + signal[i])

    return res
