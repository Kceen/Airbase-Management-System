import Avion

def loginMehanicar(username,password):
    for mehanicar in mehanicari:
        if mehanicar["username"]==username and mehanicar["password"]== password:
            return True
    return False


def loadMehanicari():
    for line in open("mehanicari.txt", "r").readlines():
        if(len(line) > 1):
            mehanicari.append(str2pilot(line))
    


def str2pilot(line):
    if(line[-1] == "\n"):
        line = line[:-1]
    
    id, ime, prezime, username, password = line.split(",")
    
    mehanicar = {
            "id" : id,
            "ime" : ime,
            "prezime" : prezime,
            "username" : username,
            "password" : password
            }
    
    return mehanicar


def popravi(idAviona, username1):
    for avion in Avion.avioni:
        if(avion["id"] == idAviona and avion["operacionoSposoban"] == "NE"):
            print()
            print("AVION = " + avion["konstruktor"] + " " + avion["model"] + " JE PONOVO OPERACIONO SPOSOBAN")
            print()
            
            avion["operacionoSposoban"] = "DA"
            Avion.sacuvajFajl()
            zapisiULogPopravka(username1, idAviona)
            return
    
    print("-----------------------------------------------------------------------------------------------------------------")
    print()
    print("AVION SA ID = " + idAviona + " NE POSTOJI ILI JE VEC POPRAVLJEN")
    print()
    print("-----------------------------------------------------------------------------------------------------------------")
   


def dodajGorivo(idAviona, kolicina, username1):
    for avion in Avion.avioni:
        if(avion["id"] == idAviona and avion["trenGorivo"] + int(kolicina) < avion["maxGorivo"]):
            avion["trenGorivo"] = avion["trenGorivo"] + int(kolicina)
            
            print()
            print("U AVION = " + avion["konstruktor"] + " " + avion["model"] + " JE DODATO " + kolicina + " KG GORIVA I SADA IMA " + str(avion["trenGorivo"]) + " KG GORIVA")
            print()
            
            Avion.sacuvajFajl()
            zapisiULogGorivo(username1, idAviona, kolicina)
            return
    
    print("-----------------------------------------------------------------------------------------------------------------")
    print()
    print("AVION SA ID = " + idAviona + " NE POSTOJI ILI MU SE NE MOZE DODATI DATA KOLICINA GORIVA")
    print()
    print("-----------------------------------------------------------------------------------------------------------------")


def zapisiULogPopravka(username, idAviona):
    for mehanicar in mehanicari:
        if(username == mehanicar["username"]):
            imeIPrezime = mehanicar["ime"] + " " + mehanicar["prezime"]
    
    for avion in Avion.avioni:
        if(avion["id"] == idAviona):
            tajAvion = avion["konstruktor"] + " " + avion["model"]
            file = open("logMehanicari.txt", "a")
            file.write(imeIPrezime + " je popravio avion = " + tajAvion + " sa ID = " + idAviona + "\n")
            file.close()
    
    
    
    
def zapisiULogGorivo(username, idAviona, kolicina):
    for mehanicar in mehanicari:
        if(username == mehanicar["username"]):
            imeIPrezime = mehanicar["ime"] + " " + mehanicar["prezime"]
    
    for avion in Avion.avioni:
        if(avion["id"] == idAviona):
            tajAvion = avion["konstruktor"] + " " + avion["model"]
        
    
    file = open("logMehanicari.txt", "a")
    file.write(imeIPrezime + " je dodao " + kolicina + " kg goriva u " + tajAvion + " sa ID = " + idAviona + "\n")
    file.close()


mehanicari = []
loadMehanicari()
