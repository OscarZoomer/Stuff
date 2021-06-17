from colorama import Fore, init, Style
from mnemonic import Mnemonic
import os
import time
init(convert=True)

bblue = Fore.CYAN + Style.BRIGHT
bwhite = Fore.WHITE + Style.BRIGHT

mnemo = Mnemonic("english")

def Clear():
    os.system('cls')
Clear()    

def Main():
    print(f"""{bblue}
                                      ════════════════════════════════════════
{bblue}                                                  ╔╗ ╦╔╦╗╔═╗╔═╗╔╗╔
{bblue}                                                  ╠╩╗║ ║ ║ ╦╠╣ ║║║
{bblue}                                                  ╚═╝╩ ╩ ╚═╝╚═╝╝╚╝   
                                      {bblue}════════════════════════════════════════""")
    print(f"""
                                              {bwhite}Developed By: {bblue}razu#0001  

                                      {bblue}════════════════════════════════════════        
                                                {bwhite}[{bblue}1{bwhite}] {bblue}Generate Wordlist 
                                         {bwhite}[{bblue}2{bwhite}] {bblue}Generate Wordlist Into A File
                                 """)
    choice = input(" > ")

    if choice == "1":
        words = mnemo.generate(strength=128)
        print(f"{bwhite}\n  {words}\n{bblue}  How To Redeem:\n  {bblue}1) {bwhite}Head to https://login.blockchain.com/#/recover\n  {bblue}2) {bwhite}Paste Your Wordlist.\n  {bblue}3) {bwhite}Head to https://temp-mail.org/\n  {bblue}4) {bwhite}Enter the temp email and enter a random password!\n  {bblue}5) {bwhite}Enjoy Free BTC!")
        os.system('pause')
        Clear()
        Main()
    elif choice == "2":
        print(f"{bblue}How many do you want to generate?")
        amount = int(input(" > "))

        for i in range(amount):
            words = mnemo.generate(strength=128)
            with open('Wordlists.txt', 'a+') as f:
                f.write(f"""===================\nWordlist: {words}\n===================""")
                print(f"{bblue}[{bwhite}!{bblue}] Generated {i} Wordlists!")     

        print(f"{Fore.RED + Style.BRIGHT}[{bwhite}!{Fore.RED + Style.BRIGHT}] Finished Generating {amount} Wordlists!")                           
        os.system('pause')
        Clear()
        Main()

    else:
        print(f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}] Error! Please select the option of 1 and 2!")
        time.sleep(2)
        Clear()
        Main()

if __name__ == "__main__":
    Main()