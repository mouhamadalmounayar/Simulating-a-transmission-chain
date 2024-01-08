import functools
import random
import numpy as np
import matplotlib.pyplot as plt
import filtre
import scipy.signal as signal


def genere_information(N=1000):
    '''
    Cree un vecteur de N bits.
    '''
    res = []
    for _ in range(N):
        a = random.randint(0, 1)
        res.append(a)
    return res


def transforme_symbole(vect_bits, temp_symbole=0.2):
    '''
    Transforme un vecteur de N bits en symbole.
    Ici un modele simpliste de symbole est utilise:
           0 -> -1 et 1 -> 1
    On aurai pu faire:
           00 -> -2, 01 -> -1, 11 -> 1, 10 -> 2
    Renvoie aussi le vecteur temps du signal discret 
    en utilisant la duree d'un symbole.
    '''
    vect_symbole = []
    vect_temps_symbole = []
    for i in range(len(vect_bits)):
        s = 2*vect_bits[i] - 1
        vect_symbole.append(s)
        vect_temps_symbole.append(temp_symbole*i)
    return vect_symbole, vect_temps_symbole


def convertit_vers_analogique(vect_symbole, F=16, temp_symbole=0.2):
    '''
    Le signal doit etre transformer en analogique avant d'etre emis.
    On simule cela par un facteur de surechatillonage F.
    On ajoute F zero entre chaque symbole.

    Renvoie le vecteur temps du signal convertit aussi
    '''
    analogic_signal = []
    aux = [0 for _ in range(F)]

    for elem in vect_symbole:
        analogic_signal.append(elem)
        analogic_signal += aux

    vect_temps_symbole_analogique = np.arange(
        0, len(vect_symbole)*temp_symbole, temp_symbole/(F+1))

    return analogic_signal, vect_temps_symbole_analogique


def applique_filtre_emission(analogic_signal, he, F=16, temp_symbole=1):
    '''
    Applique la reponse impulsionnelle du filtre d'emission
    he a vect_symbole.
    Retourne le vecteur temps correspondant.
    '''
    rep_imp = []
    for i in range(len(analogic_signal)):
        rep_imp.append(he(i))
    result = signal.convolve(rep_imp, analogic_signal)

    vect_temps_signal_emis = np.arange(
        0, len(result)*temp_symbole/F, temp_symbole/(F))

    return result, vect_temps_signal_emis


if __name__ == "__main__":
    N = 20
    F = 128
    temp_symbole = 100
    vect_bits = genere_information(N)
    vect_symbole, vect_temps_symbole = transforme_symbole(
        vect_bits, temp_symbole)
    analogic_signal, vect_temps_symbole_analogique = convertit_vers_analogique(
        vect_symbole, F, temp_symbole)

    to_use_srrc = functools.partial(
        filtre.srrc, F=F, temp_symbole=temp_symbole)

    signal_emis, vect_temps = applique_filtre_emission(
        analogic_signal, to_use_srrc, F=F, temp_symbole=temp_symbole)

    # plt.plot(vect_temps_symbole_analogique, analogic_signal)
    plt.plot(vect_temps, signal_emis)
    plt.show()
