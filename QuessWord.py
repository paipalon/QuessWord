import random

def main():
    
    sanat = ["Tampere","Ylöjärvi","Orivesi","Helsinki","Hämeenlinna","Hyvinkää","Uusikaupumki","Rovaniemi","Valkeakoski","Ikaalinen"]
    listapituus = len(sanat)
    enintaan = 15 # voi arvata vääriä kirjaimia ennen kuin oikea ilmoitetaan
    jatko = "k"
    
    while jatko == "k" or jatko == "K":
        jatko = input("Haluatko arvata sanan? k/e   ")
        if jatko == "k" or jatko == "K":
            arvaukset = 0
            luku = random.randrange(0,listapituus-1)
            sana = sanat[luku] #arvattava sana
            print("Arvottiin sana.")
            slista = list(sana)
            spituus = len(slista)
            printti = "" # kerätään käyttäjälle näytettävää merkkijonoa 
            tulostus = "" # sama kuin printti ilman välejä
            tulostus = list(tulostus)
            vaarat = ""
    
            print("Arvaa sana")
            for i in range(0,spituus):
                printti += "_ " #alussa sanan pituuden verran alaviivoja ja välejä
                tulostus += "_" #alussa pelkkiä alaviivoja
            print(printti)
            print("")
    
    
            oikeat = 0
            while oikeat<spituus and arvaukset<enintaan:
                arvaukset +=1
                print("Arvaus numero ", arvaukset)
                kirjain = input("Syötä kirjain: ")
                sanassa = tarkasta(kirjain,slista,spituus,tulostus)
                if sanassa<1:
                    print("Kirjain "+kirjain+" ei kuulu sanaan.")
                    vaarat += (kirjain+" ")
                    print("Väärät kirjaimet: "+vaarat)
                    print(" ")
                elif sanassa == 1000:
                    print("Olet jo arvannut tämän kirjaimen.")
                elif sanassa == 500:
                    print("Et syöttänyt kirjainta.")
                else:
                    print("Kirjain "+kirjain+" kuuluu sanaan.")
                    oikeat += sanassa
                    print("Sinulla on oikeita kirjaimia",oikeat)
                    printti = " "
                    for i in range(0,spituus): #muodostetaan käyttäjälle näytettävä tulostus
                        printti += tulostus[i]+" "
                    printti = str(printti)
                    print(printti)
                    print(" ")
                    if len (vaarat)>0 and oikeat<spituus:
                        print("Väärät kirjaimet: "+vaarat)
                        print(" ")
            if oikeat==spituus:
                print("Onnittelut! Arvasit sanan.")
            else:
                print("Sana on "+sana)

def tarkasta(kir, sl, sp, tul): #montako kertaa kirjain on sanassa
    km = 0
    if kir.isalpha():
        for i in range(0,sp):
            if sl[i] == kir or sl[i] == kir.upper():
                if tul[i] =="_":
                    km += 1
                    tul[i] = sl[i]
                else:
                    km = 1000
    else:
        km = 500
    return km

main()   
