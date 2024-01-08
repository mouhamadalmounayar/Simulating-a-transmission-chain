from emission import *
from reception import *
from bruit import *


def calcul_erreur(vect1, vect2):
    tot = 0
    for i in range(len(vect1)):
        if vect1[i] != vect2[i]:
            tot += 1
    return tot/len(vect1)


if __name__ == "__main__":
    # Nombre de bits
    N = 50

    # Facteur de surechantillonage
    F = 128

    # Rapport Signal Bruit
    snr_db = 10

    # Duree d'un symbole
    temp_symbole = 100

    # Cree les N bits
    vect_bits = genere_information(N)

    # Transforme bits en symbole
    vect_symbole, vect_temps_symbole = transforme_symbole(
        vect_bits, temp_symbole)

    # Transforme symbole en signal analogique
    analogic_signal, vect_temps_symbole_analogique = convertit_vers_analogique(
        vect_symbole, F, temp_symbole)

    # Filtrage a l'emission
    filtre_emission = functools.partial(
        filtre.srrc, F=F, temp_symbole=temp_symbole)
    filtre_emission = filtre.nrz

    signal_emis, vect_temps = applique_filtre_emission(
        analogic_signal, filtre_emission, F=F, temp_symbole=temp_symbole)

    # Ajout bruit
    signal_recu = ajout_bbag(signal_emis, snr_db)

    # Filtrage a la reception
    filtre_reception = functools.partial(
        filtre.srrc, F=F, temp_symbole=temp_symbole)
    filtre_reception = filtre.nrz

    signal_filtre_recu, vect_temps_recu_filtre = applique_filtre_reception(
        signal_recu, filtre_reception, F=F, temp_symbole=temp_symbole)

    # Decimation
    signa_decime = decimation(signal_filtre_recu, N, F, temp_symbole, 8)

    # Recuperation bits
    vect_bits_recu = redonne_bits(signa_decime)

    # Plotting
    # plt.plot(vect_temps_symbole_analogique, analogic_signal)
    # plt.plot(vect_temps, signal_emis)
    # plt.plot(vect_temps, signal_recu)
    # plt.plot(vect_temps_recu_filtre, signal_filtre_recu)
    plt.plot(signa_decime)
    plt.plot(vect_symbole)
    plt.plot(vect_bits)
    plt.show()

    s = calcul_erreur(vect_bits, vect_bits_recu)
    print("Proba d'erreur = ", s)
