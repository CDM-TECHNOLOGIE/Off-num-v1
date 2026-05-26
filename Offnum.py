
import subprocess
import time
import random
import os
from threading import Thread
import sys

CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f"""
{CYAN}╔══════════════════════════════════════════════════════╗
║{GREEN}   WELCOM TO THE HELL CIBLE
║{GREEN}                        TON
║{GREEN}                      HEURE   
║{GREEN}                           À                 
║{GREEN}                      SONNÉ
║{GREEN}  WESH LA LEGENDE DIT VRAIE
║
║{CYAN}                                                      
║{YELLOW}{BOLD}      ⚡ CDM TECH - PAR A-FBI  ⚡{CYAN}      
║{BLUE}{BOLD}               CDM 503                 {CYAN}      
╚══════════════════════════════════════════════════════╝{RESET}
""")

def typewriter(texte, couleur=CYAN, delai=0.03):
    texte_colore = f"{couleur}{texte}{RESET}"
    for char in texte_colore:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delai)
    print()

def charger_messages_spam(fichier="spam.txt","spam.txt2","spam.txt3")Android Download 👉: https://st.simpledesign.ltd/fqy2M3

iOS Download 👉: https://apps.apple.com/app/id1636254820):
    if not os.path.exists(fichier):
        messages_defaut = [
            "SALUT",
            "HELLO",
            "HOLLA",
            "WESH",
            "COUCOU"
        ]
        with open(fichier, 'w', encoding='utf-8') as f:
            f.write('\n'.join(messages_defaut))
    
    with open(fichier, 'r', encoding='utf-8') as f:
        messages = [ligne.strip() for ligne in f.readlines() if ligne.strip()]
    return messages

def ouvrir_lien_whatsapp(numero_telephone, message):
    numero_propre = ''.join(filter(str.isdigit, numero_telephone))
    message_encode = message.replace(' ', '%20').replace('\n', '%0A')
    lien = f"https://api.whatsapp.com/send?phone={numero_propre}&text={message_encode}"
    
    try:
        subprocess.Popen(['xdg-open', lien])
    except:
        try:
            subprocess.Popen(['open', lien])
        except:
            subprocess.Popen(['start', lien], shell=True)

def envoyer_message(numero_telephone, message):
    """Fonction pour envoyer un seul message - encapsulée pour la logique de reconnexion"""
    ouvrir_lien_whatsapp(numero_telephone, message)
    return True

def travailleur_spam(numero_telephone, messages, nombre_spam, intervalle_delai):
    for i in range(nombre_spam):
        try:
            msg = random.choice(messages)
            envoyer_message(numero_telephone, msg)
            delai = random.uniform(*intervalle_delai)
            time.sleep(delai)
        except Exception as e:
            print(f"{RED}[!] Erreur lors de l'envoi du message : {e}{RESET}")
            # Logique de reconnexion avec réessai
            nombre_tentatives = 0
            tentatives_max = 3
            while nombre_tentatives < tentatives_max:
                try:
                    typewriter(f"[*] Tentative de reconnexion... ({nombre_tentatives + 1}/{tentatives_max})", YELLOW, 0.02)
                    time.sleep(2)  # Attendre avant de se reconnecter
                    msg = random.choice(messages)
                    envoyer_message(numero_telephone, msg)
                    typewriter("[+] Reconnecté avec succès !", GREEN, 0.02)
                    delai = random.uniform(*intervalle_delai)
                    time.sleep(delai)
                    break  # Succès, sortir de la boucle de réessai
                except Exception as erreur_reconnexion:
                    nombre_tentatives += 1
                    print(f"{RED}[!] Tentative de reconnexion {nombre_tentatives} échouée : {erreur_reconnexion}{RESET}")
                    if nombre_tentatives == tentatives_max:
                        typewriter("[!] Nombre maximal de tentatives atteint. Message ignoré...", RED, 0.02)
                        time.sleep(intervalle_delai[1])  # Attendre avant de continuer
                        continue

def main():
    print_banner()
    typewriter("INITIALISATION DU SYSTÈME CDM TECH...", GREEN, 0.02)
    typewriter(f"{BOLD}DÉVELOPPEUR: ANTI FBI{RESET}", PURPLE, 0.03)
    time.sleep(1)
    
    typewriter("ACQUISITION DE LA CIBLE:", BLUE)
    numero_cible = input(f"{PURPLE}╠══[CDM503]> {RED}TÉLÉPHONE: {RESET}").strip()
    
    typewriter("INTENSITÉ DE L'INONDATION:", BLUE)
    nombre_spam = int(input(f"{PURPLE}╠══[CDM503]> {RED}NOMBRE: {RESET}"))
    
    typewriter("CALIBRAGE TEMPOREL:", BLUE)
    delai_min = float(input(f"{PURPLE}╠══[CDM503]> {RED}MIN(s): {RESET}"))
    delai_max = float(input(f"{PURPLE}╠══[CDM503]> {RED}MAX(s): {RESET}"))
    
    messages = charger_messages_spam()
    typewriter(f"CHARGEMENT DES PAYLOADS : {len(messages)}", YELLOW)
    
    clear_screen()
    print_banner()
    typewriter("PRÊT À DÉPLOYER ?", RED)
    confirmation = input(f"{PURPLE}╠══[CDM503]> {RED}LANCER (O/N): {RESET}").lower()
    
    if confirmation == 'Y':
        typewriter("WESH", GREEN)
        typewriter("SALUT", YELLOW)
        typewriter(f"{BOLD}PAR ANTI FBI{RESET}", CYAN)
        
        thread_spam = Thread(target=travailleur_spam, args=(numero_cible, messages, nombre_spam, (delai_min, delai_max)))
        thread_spam.daemon = True
        thread_spam.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            typewriter("\nSYSTÈME CDM TECH DÉCONNECTÉ", RED)
            typewriter("ANTI FBI- DÉCONNEXION", PURPLE)
    else:
        typewriter("OPÉRATION ANNULÉE", RED)

if __name__ == "__main__":
    main()
#MODZ BY ANTI FBI
