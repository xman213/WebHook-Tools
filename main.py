import requests
from random import choice
import threading
import colorama
from colorama import Fore
from colorama import init, Fore, Back, Style
from pystyle import *
import json
import os 
import time
count = 0
send = 0
os.system('title webhook tools')
def spam():
      with open("proxies.txt", "r") as f:
                            proxy1 = choice(f.readlines()).strip()
                            proxies = {'https': f'http://{proxy1}'}
      global time
      global count
      global send
      while True:
        data = {
            
            "username" : "xman",
            "avatar_url": "https://cdn.discordapp.com/attachments/864586608149790770/1004117958215356486/4.jpg"
        }


        data["embeds"] = [
            {
                "description" : embedtext,
                "title" : f"{emebdtitle}",
                "footer": {
                            "text": f"https://github.com/xman213"
                            }
            }
        ]
        try:
         r = requests.post(webhook, json = data, proxies=proxies)
         
         send += 1 
         
         os.system(
                f"title Webook Spammer made by xman │ Requests Sent: {send} │ Messages Sent: {count}" 
            )
        except Exception:
            pass
        try:
            if 204 == r.status_code:
                count += 1
                print(str(f'{colorama.Fore.GREEN} Sent To WebHook | {colorama.Fore.WHITE}{count}'))
            if "blocked" in r.text:
                print(f"{colorama.Fore.RED} Ratelimited on | {colorama.Fore.WHITE}{proxy1}")
            else:
             pass
        except Exception:
            pass

         

threads = 1000



print(f'{Fore.RED}[1] Webhook Spammer [2] Webhook Deleter')
choicee = int(input('Choice: '))
if choicee == 1:

    webhook = input('Enter webhook: ')
    embedtext = input('Enter text in embed: ')
    emebdtitle = input('Enter Embed Title: ')
    os.system('cls')
    while True:
     if threading.active_count() < int(threads):
                threading.Thread(target=spam).start()
else:
    webhook = input('Enter webhook: ')
    r = requests.delete(webhook)
    if r.status_code == 204:
        print(f'{Fore.GREEN} Webhook Was Deleted!')
        time.sleep(30)



