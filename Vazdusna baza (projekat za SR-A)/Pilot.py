import Avion

def loginPilot(username,password):
    for pilot in piloti:
        if pilot["username"]==username and pilot["password"]== password:
            return True
    return False


def loadPiloti():
    for line in open("piloti.txt", "r").readlines():
        if(len(line) > 1):
            piloti.append(str2pilot(line))
    


def str2pilot(line):
    if(line[-1] == "\n"):
        line = line[:-1]
    
    id, ime, prezime, username, password = line.split(",")
    
    pilot = {
            "id" : id,
            "ime" : ime,
            "prezime" : prezime,
            "username" : username,
            "password" : password
            }
    
    return pilot

def zapisiULog(username, idAviona):
    for pilot in piloti:
        if(username == pilot["username"]):
            imeIPrezime = pilot["ime"] + " " + pilot["prezime"]
    
    for avion in Avion.avioni:
        if(avion["id"] == idAviona):
            tajAvion = avion["konstruktor"] + " " + avion["model"]
        
    
    file = open("logPiloti.txt", "a")
    file.write(imeIPrezime + " je leteo u " + tajAvion + " sa ID = " + idAviona + "\n")
    file.close()


piloti = []
loadPiloti()
