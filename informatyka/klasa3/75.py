with open("informatyka/dane/75/tekst.txt", "r") as plik:
    slowa = plik.read().split()

with open("informatyka/dane/75/probka.txt", "r") as plik:
    probki = [linia.split() for linia in plik.readlines()]

for slowo in slowa:
    if len(slowo) > 1 and slowo[0]=='d' and slowo[-1]=='d':
        print(slowo)

A,B=5,2
for slowo in slowa:
    if len(slowo)>=10:
        zaszyfrowane="".join(chr(((ord(znak)-ord('a'))*A+B)%26+ord('a')) for znak in slowo)
        print(zaszyfrowane)

for indeks, (jawne, zaszyfrowane) in enumerate(probki, start=1):
    for A in range(1, 26, 2):  
        for B in range(26):
            test_enc="".join(chr(((ord(znak) - ord('a'))*A+B)%26+ord('a')) for znak in jawne)
            if test_enc==zaszyfrowane:
                print(f"Klucz szyfrujący numer {indeks}: ({A},{B})")
                for A_odw in range(1,26,2):
                    if (A*A_odw)%26==1:
                        B_odw=(-A_odw*B)%26
                        print(f"Klucz deszyfrujący numer {indeks}: ({A_odw},{B_odw})")
                        break
                break