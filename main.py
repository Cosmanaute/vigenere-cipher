
def run():
    tekst = input("Streng: ").replace(' ', '')
    nøkkel = input("Nøkkel: ").replace(' ', '')
    kryptertTekst = vigenere_cipher(tekst, nøkkel)
    print(kryptertTekst)

def finnePosisjon(bokstav):    
    alfabet = "abcdefghijklmnopqrstuvwxyz" 
    plassering = alfabet.index(bokstav.lower()) #finner laveste index
    return plassering

def flyttePosisjon(bokstav, flytting): 
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    plassering = (finnePosisjon(bokstav) + flytting) % 26 
    nyBokstav = alfabet[plassering]
    return nyBokstav

def vigenere_cipher(tekst, nøkkel):
    kryptertTekst = ""
    counter = 0
    for bokstav in tekst:
        if bokstav in "abcdefghijklmnopqrstuvwxyz":
            flytting = finnePosisjon(nøkkel[counter % len(nøkkel)])
            nyBokstav = flyttePosisjon(bokstav, flytting)
            kryptertTekst +=nyBokstav 
            counter += 1
        else:
            kryptertTekst +=bokstav
            
    return kryptertTekst


if __name__ == '__main__':
    run()
