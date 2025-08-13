from random import randint as ri
# DESCRIZIONE
def descrizione():
    return "Questo è un gioco in cui bisogna indovinare il numero generato in base al livello scelto\n"

partite_giocate = 0
partite_vinte = 0
partite_perse = 0
numeri_indovinati = []

# SCELTA DEL LIVELLO
def scelta_livello():
    livelli = (1, 2, 3)
    t = {1: 3, 2: 5, 3: 6}
    while True:
        try:
            livello = int(input(f"Livello {livelli}: "))
            if livello not in livelli: 
                print("Livello non valido!\n")
                continue
            break
        except ValueError: print("Inserire numero intero\n")
    limite = livello * 10
    tent = t[livello]
    return (limite, tent)
    
    
# NUMERO CASUALE
def genera_casuale(limite):
    casuale = ri(1, limite)
    return casuale
 
 
# GIOCO
def gioca(limite, tent, casuale):
    global partite_giocate, partite_vinte, partite_perse, numeri_indovinati
    
    while tent > 0:
        print(f"\nTentativi: {tent}\n")
        try:
            num=int(input(f"Inserisci un numero intero positivo tra 1 e {limite}: "))
            if num < 0: 
                print("Inserire un numero positivo\n")
                continue
            elif not 1 <= num <= limite:
                print(f"Inserire un numero compreso tra 1 e {limite}\n")
                continue
                
            else:
                if num == casuale:
                    print("Hai indovinato!\n")
                    partite_vinte += 1
                    numeri_indovinati.append(casuale)
                    break
                    
                    
                else:
                    tent -= 1
                    print("Non hai indovinato!\n")
                    if tent != 0:
                        if casuale > num: print("(suggerimento: il numero é più alto)")
                        elif casuale < num:
                            print("(suggerimento: il numero é più basso)")
                        
                    if tent == 0:
                        print(f"Hai perso... Il numero era {casuale}\n")
                        partite_perse += 1
                        continue
        except ValueError: print("Inserire un numero\n")
    partite_giocate += 1
 
    
# OUTPUT   
def main():
    print(descrizione())
    while True:
        (_limite, _tent) = scelta_livello()
        _casuale = genera_casuale(_limite)
        gioca(_limite, _tent, _casuale)
        
        while True:
            rigiocare = input("Giocare di nuovo (s/n): ").lower().strip()
            if rigiocare == "s" or rigiocare == "n": break
        if rigiocare == "n": 
            print(f"\n\n\nGiocate: {partite_giocate}\nVinte: {partite_vinte}\nPerse: {partite_perse}\n")
            print(f"\nNumeri indovinati: {numeri_indovinati}")
            break
        

if __name__ == "__main__":
    main()