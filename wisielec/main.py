import random
from slowa import slowa

#dict
wisielec_grafika = {
    0:(
        "     ",
        "     ",
        "     ",
        "     "),
    1:(
        "  o  ",
        "     ",
        "     ",
        "     "),
    2:(
        "  o  ",
        "  |  ",
        "     ",
        "     "),
    3:(
        "  o  ",
        "  |\\",
        "     ",
        "     "),
    4:(
        "  o  ",
        " /|\\",
        "     ",
        "     "),
    5:(
        "  o  ",
        " /|\\",
        "   \\",
        "     "),
    6:(
        "  o  ",
        " /|\\",
        " / \\",
        "     "),
}

def wyswietl_ludzika(zleTrafienia):
    print("-------------------")
    for x in wisielec_grafika[zleTrafienia]:
        print(x)
    print("-------------------")
def wyswietl_podpowiedzi(podpowiedz):
    print(" | ".join(podpowiedz))
def wyswietl_odpowiedz(odpowiedz):
    print(" ".join(odpowiedz))
def main():
    odpowiedz = random.choice(slowa)
    podpowiedz = ["_"] * len(odpowiedz)
    zleTrafienia = 0
    zgadnieteLitery = set()
    dziala = True


    while dziala:
        wyswietl_ludzika(zleTrafienia)
        wyswietl_podpowiedzi(podpowiedz)
        proba = input("Wpisz literę: ").lower()

        if len(proba) != 1 or not proba.isalpha():
            print("Jedna litera!")
            continue

        if proba in zgadnieteLitery:
            print(f"Już spróbowałeś litery {proba}!")
            continue

        zgadnieteLitery.add(proba)

        if proba in odpowiedz:
            for y in range(0, len(odpowiedz)):
                if odpowiedz[y] == proba:
                    podpowiedz[y] = proba
        else:
            zleTrafienia += 1
            print("źle!")


        if zleTrafienia == 6:
          wyswietl_ludzika(zleTrafienia)
          wyswietl_odpowiedz(odpowiedz)
          print("Przegrałeś!")
          dziala = False
        elif "_" not in podpowiedz:
          wyswietl_ludzika(zleTrafienia)
          print("Wygrałeś!")
          dziala = False

if __name__ == "__main__":
    main()