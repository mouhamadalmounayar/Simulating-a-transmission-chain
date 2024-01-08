import numpy as np
import matplotlib.pyplot as plt


def nrz(t, larg=10):
    if 0 <= t < larg:
        return 1
    return 0


def srrc(t, F=16, alpha=0.5, temp_symbole=1, L=8):
    t = t-temp_symbole*L/2
    if t == 0:
        return 1/F*(1-alpha+4*alpha/np.pi)
    if abs(t) == temp_symbole/(4*alpha):
        f = alpha/np.sqrt(2)
        p1 = (1+2/np.pi)*np.sin(np.pi/(4*alpha))
        p2 = (1-2/np.pi)*np.cos(np.pi/(4*alpha))
        return 1/F*(f*(p1+p2))
    p1 = np.sin(np.pi * t/temp_symbole * (1-alpha))
    p2 = 4*alpha*t/temp_symbole*np.cos(np.pi*t/temp_symbole*(1+alpha))
    de = np.pi*t/temp_symbole*(1-(4*alpha*t/temp_symbole)**2)
    return (p1+p2)/(F*de)


def srrc_herm(t, F=16, alpha=0.5, temp_symbole=1, L=8):
    t = t-temp_symbole*L/2
    t = -t
    if t == 0:
        return 1/F*(1-alpha+4*alpha/np.pi)
    if abs(t) == temp_symbole/(4*alpha):
        f = alpha/np.sqrt(2)
        p1 = (1+2/np.pi)*np.sin(np.pi/(4*alpha))
        p2 = (1-2/np.pi)*np.cos(np.pi/(4*alpha))
        return 1/F*(f*(p1+p2))
    p1 = np.sin(np.pi * t/temp_symbole * (1-alpha))
    p2 = 4*alpha*t/temp_symbole*np.cos(np.pi*t/temp_symbole*(1+alpha))
    de = np.pi*t/temp_symbole*(1-(4*alpha*t/temp_symbole)**2)
    return (p1+p2)/(F*de)


if __name__ == "__main__":
    t = np.linspace(0, 8, num=500)
    srrc_vect = [srrc(e) for e in t]
    plt.plot(t, srrc_vect)
    plt.show()
