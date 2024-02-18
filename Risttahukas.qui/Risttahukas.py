import math
from random import randint

class Risttahukas:
    def __init__(self, pikkus, laius, korgus):
        self.__pikkus = pikkus
        self.__laius = laius
        self.__korgus = korgus
        self.__diagonaal = 0
        self.__ruumala = 0
        self.arvuta_andmed()

    @property
    def diagonaal(self):
        return self.__diagonaal

    @property
    def ruumala(self):
        return self.__ruumala

    @property
    def tais_pindala(self):
        return 2 * (self.__pikkus * self.__laius + self.__laius * self.__korgus + self.__pikkus * self.__korgus)

    def arvuta_andmed(self):
        self.__diagonaal = math.sqrt(self.__pikkus ** 2 + self.__laius ** 2 + self.__korgus ** 2)
        self.__ruumala = self.__pikkus * self.__laius * self.__korgus