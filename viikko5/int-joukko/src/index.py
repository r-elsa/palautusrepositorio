import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    print(joukko.kuuluu(2))
    print(joukko.kuuluu(4))
    print(joukko.to_int_list())
    joukko.lisaa(4)

    print(joukko.to_int_list())
    print(joukko.__str__())


if __name__ == "__main__":
    main()
