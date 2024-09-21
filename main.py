import hashlib
import time
import itertools
import string

def brute_force(mdpprovided):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    attempts = 0
    start_time = time.time()

    for length in range(1, 9):  # Limite jusqu'à 8 caractères
        for attempt in itertools.product(chars, repeat=length):
            attempts += 1
            attempt_password = ''.join(attempt)
            if attempt_password == mdpprovided:
                end_time = time.time()
                duration = end_time - start_time
                print("------------------------------------")
                print(f"Mot de passe trouvé : {attempt_password}")
                print(f"Temps écoulé : {duration:.2f} secondes")
                print(f"Nombre de tentatives : {attempts}")
                print("------------------------------------")
                return
            
            # Vérifier le temps écoulé
            if time.time() - start_time > 120:
                print("------------------------------------")
                print(f"Temps écoulé de 120 secondes dépassé.")
                print(f"Nombre de tentatives effectuées : {attempts}")
                print("------------------------------------")
                return

    print("Mot de passe non trouvé dans la limite de caractères spécifiée.")

def cryptage_mdp(mdpprovided):
    hash_methods = {
        "MD5": hashlib.md5,
        "SHA-1": hashlib.sha1,
        "SHA-256": hashlib.sha256,
        "SHA-384": hashlib.sha384,
        "SHA-512": hashlib.sha512,
        "SHA-224": hashlib.sha224,
        "BLAKE2b": hashlib.blake2b,
        "BLAKE2s": hashlib.blake2s,
        "SHA3-224": hashlib.sha3_224,
        "SHA3-256": hashlib.sha3_256,
    }

    print("------------------------------------")
    print("Hachages pour le mot de passe fourni :")
    for name, method in hash_methods.items():
        hashed_password = method(mdpprovided.encode()).hexdigest()
        print(f"{name}: {hashed_password}")
    print("------------------------------------")

def decryptage_hash(hachage, dictionnaire):
    hash_methods = {
        "MD5": hashlib.md5,
        "SHA-1": hashlib.sha1,
        "SHA-256": hashlib.sha256,
        "SHA-384": hashlib.sha384,
        "SHA-512": hashlib.sha512,
        "SHA-224": hashlib.sha224,
        "BLAKE2b": hashlib.blake2b,
        "BLAKE2s": hashlib.blake2s,
        "SHA3-224": hashlib.sha3_224,
        "SHA3-256": hashlib.sha3_256,
    }

    print("------------------------------------")
    print("Recherche dans le dictionnaire...")
    
    attempts = 0
    found = False
    start_time = time.time()  # Ajouté pour le timing

    # Ouvrir le fichier de dictionnaire
    with open(dictionnaire, 'r') as file:
        for line in file:
            attempt_password = line.strip()  # Enlever les espaces et les sauts de ligne
            attempts += 1
            
            # Tester chaque méthode de hachage
            for name, method in hash_methods.items():
                if method(attempt_password.encode()).hexdigest() == hachage:
                    end_time = time.time()
                    duration = end_time - start_time
                    print("------------------------------------")
                    print(f"Mot de passe trouvé : {attempt_password} avec {name}")
                    print(f"Temps écoulé : {duration:.2f} secondes")
                    print(f"Nombre de tentatives : {attempts}")
                    print("------------------------------------")
                    found = True
                    break  # Sortir de la boucle de méthodes de hachage
            
            if found:
                break  # Sortir de la boucle de mots de passe

    if not found:
        print("Aucun mot de passe correspondant trouvé.")
    print(f"Nombre total de tentatives : {attempts}")
    print("------------------------------------")

def afficher_menu():
    print("------------------------------------")
    print("1) Test de brute force mdp")
    print("2) Cryptage de mdp via 10 méthodes")
    print("3) Décryptage de hachage via 10 méthodes")
    print("4) Soon . . .")
    print("")
    print("x) Quitter")
    print("------------------------------------")

def main():
    while True:
        afficher_menu()
        choix = input("Que voulez-vous faire ? ").strip().lower()

        if choix == '1':
            mdp = input("Entrez le mot de passe à tester : ")
            brute_force(mdp)
        elif choix == '2':
            mdp = input("Entrez le mot de passe à crypter : ")
            cryptage_mdp(mdp)
        elif choix == '3':
            hachage = input("Entrez le hachage à décrypter : ")
            decryptage_hash(hachage, "dictionnaire.txt")  
        elif choix == 'x':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
