import time
import os, sys
import colorama

from telethon.sync import TelegramClient
# Defining the ANSI color codes
R = "\033[31m"  # Red
G = "\033[32m"  # Green
W = "\033[0m"   # Reset to White/Default


with open("Message.txt", "r", encoding="utf-8", errors="ignore") as f:
    msg = f.read()

count = 0
sent = 0
notSent = 0

def screen_clear():
    _ = os.system('cls')

def send(lines):
    global count, sent, notSent, client
    try:
        while sent < 1000:
            with TelegramClient(phone, api_id, api_hash) as client:
                client.start()
                for i in lines:
                    i = i.strip()
                    i = i.replace("\n", "")
                    client.send_message(int(i), str(msg))
                    sent += 1
                    os.system(f"title : [+] RMYEN TELEGRAM SENDER - GOOD : {sent}  BAD : {notSent}")
                    print(f"{G}[+] {W}{i} sent success!")
        
            if sent % 5 == 0:
                print(f"{G} Waiting 30 Minutes <3.{W}")
                time.sleep(540)
        
    
    except:   
        notSent += 1
        os.system(f"title : [+] RMYEN TELEGRAM SENDER - GOOD : {sent}  BAD : {notSent}")
        print(f"{R}[-] {W}{i} Not sent.")

api_id = ""
api_hash = ""
phone = ""

def Connect():
    with TelegramClient(phone, api_id, api_hash) as client:
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code (in your telegram app): '))

if __name__ == "__main__":
    screen_clear()
    connect()
    ids = input(f"{R}> {W}Enter Your Groups Ids List: ")
    with open(ids, "r") as f:
        lines = f.readlines()
        
    send(lines)
    
