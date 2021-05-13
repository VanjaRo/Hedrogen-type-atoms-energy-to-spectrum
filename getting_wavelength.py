from math import pi


def get_wave(ni, nj, red_mass, Z):
    k = 9*1e9
    e = 1.6*1e-19
    h = 6.626*1e-34
    c = 3*1e8
    c = 3*1e8
    lam = 1 / ((Z**2) * (k**2) * red_mass * (e**4) * 2 * (pi**2)*(1 / (ni**2) - 1 / (nj**2)) /
               ((h**3) * c)) * 10**9
    return lam


def get_reduce_mass_hydrogen():
    me = 9.10938356 * 10**-31
    mp = 1.67*10**-27
    return me*mp/(me+mp)


def get_reduce_mass_helium():
    me = 9.10938356 * 10**-31
    mp = 6.6465*10**-27
    return me*mp/(me+mp)


def get_reduce_mass_lithium():
    me = 9.10938356 * 10**-31
    mp = 1.15258*10**-26
    return me*mp/(me+mp)


def get_vector_wave_hydrogen(ni, nj):
    vector = []
    nj += 1
    for i in range(ni + 1, nj):
        vector.append(get_wave(ni, i, get_reduce_mass_hydrogen(), 1))
    return vector


def get_vector_wave_helium(ni, nj):
    vector = []
    nj += 1
    for i in range(ni + 1, nj):
        vector.append(get_wave(ni, i, get_reduce_mass_helium(), 2))
    return vector


def get_vector_wave_lithium(ni, nj):
    vector = []
    nj += 1
    for i in range(ni + 1, nj):
        vector.append(get_wave(ni, i, get_reduce_mass_lithium(), 3))
    return vector


if __name__ == '__main__':
    print(get_reduce_mass_hydrogen())
    print(get_reduce_mass_helium())
    print(get_reduce_mass_lithium())
