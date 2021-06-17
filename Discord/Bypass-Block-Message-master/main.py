import os
from requests import Session
from colorama import Fore, init
init(convert=True)

class Client:
    def __init__(self, token):
        self.token = token
        self.session = Session()
        self.api = "https://discord.com/api/v6/"
        self.user_id = ""
        self.channel_id = ""
    
    def getHeaders(self):
        return { "Content-Type": "application/json", "Authorization": self.token , "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    def main(self):
        os.system("cls")
        print(f'= Dm Blocker Bypass =  ~ Fweak\n\n')

    def askUserId(self):
        print(f'\n[{Fore.CYAN};;{Fore.RESET}] User Id: ', end="")
        self.user_id = str(input("")).rstrip()
    
    def createDmChannel(self):
        _response = self.session.post(f"{self.api}users/@me/channels", json={ 'recipient_id': self.user_id}, headers=self.getHeaders())
        if _response.status_code < 400:
            self.channel_id = _response.json()['id']
    
    def sendMessage(self):
        print(f"\n[{Fore.CYAN}!!{Fore.RESET}] Message Content: ", end="")
        content = str(input(""))
        _data = self.session.post(f"{self.api}/channels/{self.channel_id}/messages", json={"content": content}, headers=self.getHeaders())
        if _data.status_code < 400:
            print(f"[{Fore.GREEN}!!{Fore.RESET}] Sent message!")
        else:
            print(f"[${Fore.RED}!!{Fore.RESET}] Error sending message")
        self.sendMessage()
        
if __name__ == "__main__":
    print(f"[{Fore.CYAN}!!{Fore.RESET}] Your token: ", end="")
    bypasss = Client(str(input("")))
    bypasss.main()
    bypasss.askUserId()
    bypasss.createDmChannel()
    bypasss.sendMessage()

