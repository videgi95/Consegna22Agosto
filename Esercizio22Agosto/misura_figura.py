figura = " "
while figura != "stop":
    figura = input("Scegli la figura di cui calcolare il perimetro\nPuoi scegliere quadrato,cerchio o rettangolo\nScrivi stop per uscire: \n")
    if figura.lower() == "quadrato":
        lato = int(input("Inserisci la misura del lato del quadrato: \n"))
        perimetro = lato*4
        print(f"Il perimetro e': {perimetro}")
    elif figura.lower() == "cerchio":
        raggio = int(input("Inserisci la misura del raggio: \n"))
        circonferenza=2*3.14*raggio
        print(f"La misura della circonferenza e'{circonferenza}")
    elif figura.lower() == "rettangolo":
        base = int(input("Inserisci la misura della base: \n"))
        altezza = int(input("Inserisci la misura dell'altezza: \n"))
        p_rettangolo = 2*base + 2*altezza
        print(f"La misura del perimetro del rettangolo e': {p_rettangolo}")
    elif figura.lower() == "stop":
        break
    else:
        print("Selezione non valida,scegli tra le figure proposte")
        