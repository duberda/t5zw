import requests
import os
from time import sleep
print("#Coded BY : @ccXco")
sleep(0.0)

print("\033[0;31m《1》Update Tools & lib \n《2》Open Tool")
lib = input("\n《·》Please Choice《1 or 2》> ")
if lib == "1":
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install python')
    os.system('pkg install python')
    os.system('pip1 install python')
    os.system('pip install wheel')
    os.system('pip1 install wheel')
    os.system('pkg install wheel')
    os.system('pip install colorama')
    os.system('pip2 install colorama')
    os.system('pkg install colorama')
    os.system("pip install colorama")
    os.system("pip install colored")
    os.system("pip install instabot")
    os.system("pip install youtube_dl")
    os.system("pip install pyfiglet")
    os.system("pip install pafy")
    os.system("pip install tqdm")
    os.system("pip install requests_toolbelt")
    os.system("pip install urllib")
    os.system("pip install secrets")
    os.system("pip install uuid")
    os.system("pip install bs4")
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

import requests
import random
import secrets
from time import sleep
from user_agent import generate_user_agent
from queue import Queue
from colorama import *
import time
import colorama
import requests

print("\033[0;35m#Coded BY : @ccXco")
print("")
print(Fore.RED + """
  _____                       _   
 |  __ \                     | |  
 | |__) |___ _ __   ___  _ __| |_ 
 |  _  // _ \ '_ \ / _ \| '__| __|
 | | \ \  __/ |_) | (_) | |  | |_ 
 |_|  \_\___| .__/ \___/|_|   \__|
            | |                   
            |_|                                            
    
    """, Fore.GREEN + "Credit @ccXco - RoBiNiQ")
print(Fore.GREEN + "Instagram Reporter,", Fore.RED+"Free And Not For Sell")
username = input(Fore.CYAN + "[•] Username : ") 
password = input(Fore.YELLOW + "[•] Password : ")


def login1():
    import os
    import requests
    import time
    import re
    from json import loads
    r1 = requests.session()
    global ig_did, csrftoken, sessionid

    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
        'x-instagram-ajax': '0c15f4d7d44a',
        'x-requested-with': 'XMLHttpRequest'  
    }
    login_data = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    login = r1.post(login_url, data=login_data, headers=login_headers)
    if ('{"user": false, "authenticated": false, "status": "ok"}') in login:
        print(Fore.RED + "[!] Check Your Username And Try Again")

    if ('{"user": true, "authenticated": false, "status": "ok"}') in login.text:
        print(Fore.RED + "[!] Check Yo Password And Try Again")

    if ('{"message": "checkpoint_required"') in login.text:
        print(Fore.RED + "[!] Checkpoint")

    if 'userId' in login.text:
        print('')  
    else:
        print(Fore.RED + "[!] Check Your Acc And Try Again")

    ig_did = login.cookies['ds_user_id']
    csrftoken = login.cookies['csrftoken']
    sessionid = login.cookies['sessionid']
    u = r1.get(f"https://www.instagram.com/{username}/?__a=1")
    idq = str(u.json()["graphql"]["user"]["id"])
    print(f"[+] Login Done > {idq}")
    hed = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '31',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'ig_did={ig_did}; mid=X1ej8wALAAH-iuqPdbS2k838raMR; datr=WVVnXzp0tD7mIRdZ-0jb9JKJ; ig_nrcb=1; shbid=14759; shbts=1612285444.666352; rur=ATN; csrftoken={csrftoken}; ds_user_id={idq}; sessionid={sessionid}',
        'origin': 'https://www.instagram.com',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',  
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'x-csrftoken': csrftoken,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0HH5O9Hioplekd3BZjVgr-KFLmmXjkRtIbTd68b-Ay4U_g',
        'x-instagram-ajax': 'b50ae05deb9f',
        'x-requested-with': 'XMLHttpRequest'
    }

    Target = input(Fore.YELLOW + '[•] Target : ')
    uss = r1.get(f"https://www.instagram.com/{Target}/?__a=1")
    idd = str(uss.json()["graphql"]["user"]["id"])
    print(f'[•] {Target} > {idd}')
    print("""
       chose Report <:>
       [1] - spam
       [2] - violence
       [3] - Impersonation
       [4] - Sexual activity
       [5] - harassment
       [6] - Self-harm
       [7] - Hate on

           """)  
    xx = int(input(Fore.CYAN + "[•] Enter the report number > "))
    print("")
    nu = 0
    n = 0
    rs = requests.session()
    if xx == 1:
        P1 = int(input(Fore.GREEN + "[•] How many reports > "))
        tu = int(input("[•] time wait > "))

        for i_1 in range(P1):
            url_1 = f'https://www.instagram.com/users/{idd}/report/'
            data_1 = {
                'source_name': 'profile', 
                'reason_id': '1'
            }
            report_1 = rs.post(url_1, data=data_1, headers=hed).status_code
            if report_1 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")
            time.sleep(tu)

    elif xx == 2:
        P2 = int(input("How many reports > "))  
        tu = int(input("time wait > "))
        for i_2 in range(P2):
            url_2 = f'https://www.instagram.com/users/{idd}/report/'
            data_2 = {
                'source_name': 'profile',
                'reason_id': '5'
            }
            report_2 = rs.post(url_2, data=data_2, headers=hed).status_code
            if report_2 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")  
            time.sleep(tu)
    elif xx == 3:
        P3 = int(input("How many reports > "))
        tu = int(input("time wait > "))

        for i_3 in range(P3):
            url_3 = f'https://www.instagram.com/users/{idd}/report/'
            data_3 = {
                'source_name': 'profile',
                'reason_id': '8'
            }
            report_3 = rs.post(url_3, data=data_3, headers=hed).status_code
            if report_3 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")
            time.sleep(tu)
    elif xx == 4:
        P4 = int(input("How many reports > "))
        tu = int(input("time wait > "))

        for i_4 in range(P4):
            url_4 = f'https://www.instagram.com/users/{idd}/report/'
            data_4 = {
                'source_name': 'profile',
                'reason_id': '4'
            }
            report_4 = rs.post(url_4, data=data_4, headers=hed).status_code
            if report_4 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")
            time.sleep(tu)
    elif xx == 5:
        P5 = int(input("How many reports > "))
        tu = int(input("time wait > "))
        print('-' * 30)
        for i_5 in range(P5):
            url_5 = f'https://www.instagram.com/users/{idd}/report/'
            data_5 = {
                'source_name': 'profile',
                'reason_id': '7'
            }
            report_5 = rs.post(url_5, data=data_5, headers=hed).status_code
            if report_5 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")
            time.sleep(tu)
    elif xx == 6:
        P6 = int(input("How many reports > "))
        tu = int(input("time wait > "))

        for i_6 in range(P6):
            url_6 = f'https://www.instagram.com/users/{idd}/report/'
            data_6 = {
                'source_name': 'profile',
                'reason_id': '2'
            }
            report_6 = rs.post(url_6, data=data_6, headers=hed).status_code
            if report_6 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")
            time.sleep(tu)
    elif xx == 7:
        P7 = int(input("How many reports > "))
        tu = int(input("time wait > "))
        print('-' * 30)
        for i_7 in range(P7):
            url_7 = f'https://www.instagram.com/users/{idd}/report/'
            data_7 = {
                'source_name': 'profile',
                'reason_id': '6'
            }
            report_7 = rs.post(url_7, data=data_7, headers=hed).status_code
            if report_7 == 200:
                nu += 1
            else:
                n += 1
            print(f"\rSent = {nu}  Error = {n}", end="")
            time.sleep(tu)


login1()

#Coded BY : @ccXco