"""Chercher les nombres premiers."""

from math import sqrt
from math import floor

def isprime(p):
    """Vérifier si les nombres sont premiers."""

    if p==1:
        return False
    for i in range (2, floor(sqrt(p))+1):
        if p%i == 0:
            return False
    return True

#### Fonction principale


def main():
    """Affichier les nombres premiers entre 2 et 99."""
    for n in range(2,100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
