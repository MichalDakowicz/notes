lista=[]
with open("informatyka/dane/74/hasla.txt") as plik:
    for linia in plik:
        lista.append(linia.strip())
print(lista)
ile=0
for haslo in lista:
    if haslo.isdecimal():
        ile+=1
print(ile)

slownik={}
for haslo in lista:
    if haslo in slownik:
        slownik[haslo]+=1
    else:
        slownik[haslo]=1
for k,v in slownik.items():
    if v>1:
        print(k)

ile_hasel = 0
for haslo in lista:
    CY = ML = DL = False
    for znak in haslo:
        if "0" <= znak <= "9":
            CY = True
        elif "a" <= znak <= "z":
            ML = True
        elif "A" <= znak <= "Z":
            DL = True
    if CY and ML and DL:
        ile_hasel += 1
print(ile_hasel)
