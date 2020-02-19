import Pilot

def loadAvioni():
    for line in open("avioni.txt", "r").readlines():
        if(len(line) > 1):
            avion = str2avion(line)
            avioni.append(avion)
    


def str2avion(line):
    if(line[-1] == "\n"):
        line = line[:-1]
    
    id, drzavaPorekla, konstruktor, model, maxPotisak, trenGorivo, maxGorivo, operacionoSposoban, slobodan = line.split(",")
    
    avion = {
            "id" : id,
            "drzavaPorekla" : drzavaPorekla,
            "konstruktor" : konstruktor,
            "model" : model,
            "maxPotisak" : int(maxPotisak),
            "trenGorivo" : int(trenGorivo),
            "maxGorivo" : int(maxGorivo),
            "operacionoSposoban" : operacionoSposoban,
            "slobodan" : slobodan
            }
    
    return avion


def avion2str(avion):
    return ','.join([str(avion['id']),avion['drzavaPorekla'],avion['konstruktor'],avion['model'],str(avion['maxPotisak']),str(avion["trenGorivo"]),str(avion["maxGorivo"]),avion["operacionoSposoban"],avion["slobodan"]])


def dodajNoviAvion():
    idNov = input("UNESITE ID = ")
    
    for avion in avioni:
        if(idNov == avion["id"]):
            print()
            print("DATI ID VEC POSTOJI, PROBAJTE PONOVO SA DRUGIM")
            print()
            return
    
    drzavaPoreklaNov = input("UNESITE DRZAVU POREKLA = ")
    konstruktorNov = input("UNESITE KONSTRUKTORA = ")
    modelNov = input("UNESITE NAZIV MODELA = ")
    maxPotisakNov = input("UNESITE MAKSIMALNI POTISAK = ")
    trenGorivoNov = input("UNESITE TRENUTNU KOLICINU GORIVA U AVIONU = ")
    maxGorivoNov = input("UNESITE MAKSIMALNU KOLICINU GORIVA U AVIONU = ")
    operacionoSposobanNov = input("UNESITE DA LI JE AVION OPERACIONO SPOSOBAN = ")
    slobodanNov = input("UNESITE DA LI JE AVION SLOBODAN ZA LETENJE = ")

    avionString = idNov + "," + drzavaPoreklaNov + "," + konstruktorNov + "," + modelNov + "," + maxPotisakNov + "," + trenGorivoNov + "," + maxGorivoNov + "," + operacionoSposobanNov + "," + slobodanNov 
    avion1 = str2avion(avionString)
    avioni.append(avion1)
    
    print()
    print("AVION USPESNO DODAT U BAZU")
    print()
    
def sacuvajFajl():
    file = open("avioni.txt", "w")
    for avion in avioni:
        file.write(avion2str(avion) + "\n")
    file.close()
    
#def dodajNoviAvionUFajl(avionString):
#    file = open("avioni.txt", "a")
#    file.write(avionString + "\n")
#    file.close()
    
def header():
    print("ID |DRZAVA POREKLA|KONSTRUKTOR     |MODEL   |MAX POTISAK|TRENUTNO GORIVO|MAX GORIVO|OPERACIONO SPOSOBAN|SLOBODAN|\n" 
      "---*--------------*----------------*--------*-----------*---------------*----------*-------------------*--------*"
    )

def ispisSvihAviona2(avioni):
    for avion in avioni:
        ispisJedanAvion(avion)
        
        
def ispisSvihAviona():
    for avion in avioni:
        ispisJedanAvion(avion)
        
def ispisSposobnihAviona():
    for avion in avioni:
        if(avion["operacionoSposoban"] == "DA"):
            ispisJedanAvion(avion)
    
    
def ispisAvionaNaPopravci():
    for avion in avioni:
        if(avion["operacionoSposoban"] == "NE"):
            ispisJedanAvion(avion)
            
def ispisSlobodnihAviona():
    for avion in avioni:
        if(avion["slobodan"] == "DA"):
            ispisJedanAvion(avion)

def ispisZauzetihAviona():
    for avion in avioni:
        if(avion["slobodan"] == "NE"):
            ispisJedanAvion(avion)

   
def ispisSlobodnihIOperacionoSposobnihAviona():
    for avion in avioni:
        if(avion["slobodan"] == "DA" and avion["operacionoSposoban"] == "DA"):
            ispisJedanAvion(avion)
    
def ispisJedanAvion(avion):
    print("{0:3}|{1:14}|{2:16}|{3:8}|{4:11}|{5:15}|{6:10}|{7:19}|{8:8}|".format(
        avion["id"],
        avion["drzavaPorekla"],
        avion["konstruktor"],
        avion["model"],
        avion["maxPotisak"],
        avion["trenGorivo"],
        avion["maxGorivo"],
        avion["operacionoSposoban"],
        avion["slobodan"]
        ))
    
    
def poleti(avionID, username):
    for avion in avioni:
        if(avion["id"] == avionID and avion["slobodan"] == "DA" and avion["operacionoSposoban"] == "DA"):
            print()
            print("AVION USPESNO IZABRAN")
            print()
            
            if(int(avion["trenGorivo"]) < 1000):
                print("AVION IMA MANJE OD 1000 KG GORIVA I NE MOZE SE KORISTITI PRE DOPUNE")
                print()
                return
            else:
                avion["trenGorivo"] = int(avion["trenGorivo"]) - 1000
                avion["slobodan"] = "NE"
                Pilot.zapisiULog(username, avionID)
                sacuvajFajl()
                return
    
    print()
    print("AVION SA ID = " , avionID , " NIJE DOSTUPAN ILI NE POSTOJI")
    print()
      
def sleti(avionID):
    for avion in avioni:
        if(avion["id"] == avionID and avion["slobodan"] == "NE"):
            print()
            print("AVION USPESNO IZABRAN I MOZE SE PONOVO KORISTITI")
            print()
            avion["slobodan"] = "DA"
            sacuvajFajl()
            return
      
    print()
    print("AVION SA ID = " , avionID , " JE VEC DOSTUPAN ILI NE POSTOJI")
    print()
      
      
def nadjiAvion(konstruktor, model):
    for avion in avioni:
        if(konstruktor == avion["konstruktor"] and model == avion["model"]):
            ispisJedanAvion(avion)
      
def kljucUAvionu(key):
    jeste = False
    for avion in avioni:
        if(key in avion.keys()):
            jeste = True
    return jeste
      
def sort(key):
    avioni.sort(key= lambda x : x[key])
    
    
avioni = []
loadAvioni()
