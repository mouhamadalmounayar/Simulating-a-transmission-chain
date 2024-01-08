import re
import numpy as np
import scipy.signal as signal


def applique_filtre_reception(signa_bruite, hr, F=16, temp_symbole=1):
    '''
    Applique la reponse impulsionnelle du filtre
    de reception. Celle ci va etre applique au signal
    bruite recu
    Retourne le vecteur temps correspondant.
    '''
    rep_imp = []
    for i in range(len(signa_bruite)):
        rep_imp.append(hr(i))
    result = F*signal.convolve(rep_imp, signa_bruite, mode='full')

    vect_temps = np.arange(
        temp_symbole/F, (len(result))*temp_symbole/F + temp_symbole/F, temp_symbole/(F))

    return result, vect_temps


def decimation(signal_filtre_recu, N=20, F=16, temp_symbole=0.3, L=8):
    '''
    Passage de l'analogique au numerique.
    On lit les valeur de signal_recu au instant t_echantilonage.
    '''
    t_0 = (temp_symbole)*(L)
    result = np.zeros(N)
    for i in range(N):
        result[i] = signal_filtre_recu[t_0+i*F]
    return result


def redonne_bits(signal_decime):
    result = []
    for i in signal_decime:
        if i < 0:
            result.append(0)
        else:
            result.append(1)
    return result
