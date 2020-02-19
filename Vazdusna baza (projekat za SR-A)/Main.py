import Avion
import Pilot
import Mehanicar

def main(): 
    print("1 - SISTEM ZA PILOTE")
    print("2 - SISTEM ZA MEHANICARE")
    
    print()
    
    userInput = input("PRITISNITE 1 ZA SISTEM ZA PILOTE ILI 2 ZA SISTEM ZA MEHANICARE = ")
    print()
    
    if(userInput == "1"):
        print("IZABRALI STE SISTEM ZA PILOTE")
        print("MOLIM VAS ULOGUJTE SE")
        print()
        
        username = input("MOLIM VAS UNESITE VAS USERNAME = ")
        password = input("MOLIM VAS UNESITE VAS PASSWORD = ")
        
        if(Pilot.loginPilot(username,password)):
            print()
            print("LOGIN SUCCESS")
            print()
            
            menuInput = "0";
            
            while(menuInput != "X" and menuInput != "x"):
                printMenuP()
                print()
                menuInput = input("IZABERITE ODGOVARAJUCU OPCIJU = ")
                print()
                
                if(menuInput == "1"):
                    Avion.header()
                    Avion.ispisSvihAviona()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput == "2"):
                    Avion.header()
                    Avion.ispisSposobnihAviona()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput == "3"):
                    Avion.header()
                    Avion.ispisAvionaNaPopravci()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput == "4"):
                    Avion.header()
                    Avion.ispisSlobodnihAviona()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput == "5"):
                    Avion.header()
                    Avion.ispisSlobodnihIOperacionoSposobnihAviona()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                    
                    izbor = input("IZABERITE AVION POMOCU ID-JA = ")
                    Avion.poleti(izbor, username)
                    
                elif(menuInput == "6"):
                    Avion.header()
                    Avion.ispisZauzetihAviona()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                    
                    izbor = input("IZABERITE AVION POMOCU ID-JA = ")
                    Avion.sleti(izbor)
                elif(menuInput == "7"):
                    konstruktor = input("UNESI KONSTRUKTORA AVIONA = ")
                    model = input("UNESI MODEL AVIONA = ") 
                    Avion.header()
                    Avion.nadjiAvion(konstruktor, model)
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput == "8"):
                    key = input("UNESI PO CEMU ZELIS DA SORTIRAS AVIONE = ")
                    if(Avion.kljucUAvionu(key)):
                        Avion.sort(key)
                        Avion.header()
                        Avion.ispisSvihAviona()
                        print()
                        print("-----------------------------------------------------------------------------------------------------------------")
                        print()
                    else:
                        print("-----------------------------------------------------------------------------------------------------------------")
                        print()
                        print("DATI PARAMETAR NE POSTOJI")
                        print()
                        print("-----------------------------------------------------------------------------------------------------------------")
             
                else:
                    if(menuInput == "x" or menuInput == "X"):
                        print("KRAJ PROGRAMA")
                    else:
                        print("UNELI STE POGRESNU OPCIJU")
                        print()
                        print("------------------------------------------------------------------------------------------------------------------")
                        print()
                
            
        
        
        else:
            print("POGRESNI PODACI ZA LOGIN")
    elif(userInput == "2"):
        print("IZABRALI STE SISTEM ZA MEHANICARE")
        print("MOLIM VAS ULOGUJTE SE")
        print()
        
        username1 = input("MOLIM VAS UNESITE VAS USERNAME = ")
        password1 = input("MOLIM VAS UNESITE VAS PASSWORD = ")
        
        if(Mehanicar.loginMehanicar(username1,password1)):
            print()
            print("LOGIN SUCCESS")
            print()
            
            menuInput1 = "0";
            
            while(menuInput1 != "X" and menuInput1 != "x"):
                printMenuM()
                print()
                menuInput1 = input("IZABERITE ODGOVARAJUCU OPCIJU = ")
                print()
                
                if(menuInput1 == "1"):
                    Avion.header()
                    Avion.ispisSvihAviona()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput1 == "2"):
                    Avion.header()
                    Avion.ispisAvionaNaPopravci()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                elif(menuInput1 == "3"):
                    Avion.header()
                    Avion.ispisAvionaNaPopravci()
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                    
                    idDaSePopravlja = input("IZABERITE AVION KOJI TREBA DA SE POPRAVLJA POMOCU ID-JA = ")
                
                    Mehanicar.popravi(idDaSePopravlja, username1)
                    
                    
                elif(menuInput1 == "4"):
                    Avion.header()
                    Avion.ispisSvihAviona()
                    
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                    
                    idDaSeDodaGorivo = input("IZABERITE AVION U KOJI SE DODAJE GORIVO POMOCU ID-JA = ")
                    kolicinaGoriva = input("UNESITE KOLICINU GORIVA KOJE DODAJETE U KG = ")
                    
                    Mehanicar.dodajGorivo(idDaSeDodaGorivo, kolicinaGoriva, username1)
                
                elif(menuInput1 == "5"):
                    print("UNESI POTREBNE PODATKE ZA NOVI AVION")
                    print()
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print()
                    
                    Avion.dodajNoviAvion()
                    
                    Avion.sacuvajFajl()
                
                else:
                    if(menuInput1 == "x" or menuInput1 == "X"):
                        print("KRAJ PROGRAMA")
                    else:
                        print("UNELI STE POGRESNU OPCIJU")
                        print()
                        print("------------------------------------------------------------------------------------------------------------------")
                        print()
        else:
            print("POGRESNI PODACI ZA LOGIN")
    else:
        print("GRESKA, IZABRALI STE POGRESNU OPCIJU")
    
    
    
def printMenuP():
    print("1 - IZLISTAJ SVE AVIONE U BAZI")
    print("2 - IZLISTAJ SVE OPERACIONO SPOSOBNE AVIONE NA BAZI")
    print("3 - IZLISTAJ SVE AVIONE NA POPRAVCI")
    print("4 - IZLISTAJ SVE DOSTUPNE AVIONE")
    print("5 - IZABERI AVION ZA LETENJE")
    print("6 - ZAVRSI LET I PREDAJ AVION")
    print("7 - NADJI AVION PO MODELU")
    print("8 - SORTIRAJ AVIONE")
    print("X - IZADJI IZ PROGRAMA")
    
def printMenuM():
    print("1 - IZLISTAJ SVE AVIONE U BAZI")
    print("2 - IZLISTAJ SVE AVIONE KOJI SE MORAJU POPRAVITI")
    print("3 - POPRAVI AVION")
    print("4 - DODAJ GORIVO U AVION")
    print("5 - DODAJ NOVI AVION U BAZU")
    print("X - IZADJI IZ PROGRAMA")
    
main()