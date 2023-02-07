import requests,json
import os
import time 
import threading 
from requests import get
from re import search
from requests import Session
from threading import Thread
os.system("clear")
print()
print("โครงศึกษา BY : FLY SHOP DISCOR : https://discord.com/invite/YknWyFmCGc ")
print()
phone = input("PHONE : ")
print()
num = int(input("NUM : "))
print()

def api1():
    requests.post("api") #ซื้อได้จากร้าน FLY SHOP DISCORD : https://discord.com/invite/YknWyFmCGc
    print("ATTACK")
    
for i in range(num):
    threading.Thread(target=api1).start()