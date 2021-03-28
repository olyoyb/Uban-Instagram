#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#0737
#

try:
    import requests
    import os
    from os import system, path
    import threading
    import random

    system("title " + "Soud Was Here - @8Y - Soud#0737")
    import colorama
    from colorama import Fore

    colorama.init(autoreset=True)
except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
if path.exists("proxy.txt"):
    proxyfile = open("proxy.txt", 'r').read().splitlines()
else:
    print("Pls Make proxy.txt file\n")
    input()
    exit()
sent, spam, banned = 0, 0, 0
logo = """
         _______   __
   ____ |  _  \ \ / /
  / __ \ \ V / \ V / 
 / / _` |/ _ \  \ /  
| | (_| | |_| | | |  
 \ \__,_\_____/ \_/  
  \____/             
"""
print(f"{Fore.CYAN}{logo}")
print(
    f"{Fore.GREEN}\n\tInstagram: @8Y\n\tGithub: @Soud69\n\tDiscord: Soud#0737\n\tTelegram: @Soud69{Fore.RED}\n\t[Dont Try To Sell It]\n")
account_username = input("Username: ")
account_full_name = input("Account Name: ")
account_email = input("Email: ")
account_phone = int(input("Phone Number: "))
message_contact = input("Contact Message (Leave It Empty To Use Default Message): ")

if message_contact == "":
    message_contact = "Hello Instagram Support, my account have been disabled by mistake, pls reactive it"
threads_number = int(input("Threads: "))


def unban():
    global spam, sent, banned, account_full_name, account_email, account_username, account_phone, message_contact
    while 1:
        proxy_dict = []
        for proxy in proxyfile:
            proxy_dict.append(proxy)
            rnd = str(random.choice(proxy_dict))
        try:
            proxyfinal = {
                "http": f"http://{rnd}",
                "https": f"https://{rnd}"
            }
            url = "https://help.instagram.com/ajax/help/contact/submit/page"
            data = {
                "jazoest": 2890,
                "lsd": "AVr_Dx9PS9A",
                "name": account_full_name,
                "instagram_username": account_username,
                "email": account_email,
                "mobile_number": account_phone,
                "appeal_reason": message_contact,
                "support_form_id": 606967319425038,
                "support_form_hidden_fields": "{}",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
                "__csr": "",
                "__req": "h",
                "__beoa": 0,
                "__pc": "PHASED:DEFAULT",
                "__bhv": 2,
                "dpr": 3,
                "__ccg": "EXCELLENT",
                "__rev": 1003521343,
                "__s": "8x0mgw:dal0sr:s5g412",
                "__hsi": "6943937313156005653-0",
                "__comet_req": 0,
                "__spin_r": 1003521343,
                "__spin_b": "trunk",
                "__spin_t": 1616761394
            }
            head = {
                "Host": "help.instagram.com",
                "Accept": "*/*",
                "X-FB-LSD": "AVr_Dx9PS9A",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-us",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://help.instagram.com",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                "Connection": "keep-alive",
                "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content"
            }
            req = requests.post(url, data=data, headers=head, proxies=proxyfinal, timeout=3)
            if ">Form submitted successfully" in req.text:
                sent += 1
                print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")
            elif "You may want to slow down or stop to avoid a restriction on your account" in req.text:
                spam += 1
                print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")
            elif "The username or short-link you provided does not belong to an inactive Instagram Account." in req.text:
                sent += 1
                print("\nUnbanned !")
                print(f"\n\rSent : {sent} | Spam : {spam} | Error: {banned}\n\n")
                print(f"{Fore.CYAN}{logo}")
                print(
                    f"{Fore.GREEN}\n\tInstagram: @8Y\n\tGithub: @Soud69\n\tDiscord: Soud#0737\n\tTelegram: @Soud69{Fore.RED}\n\t[Dont Try To Sell It]\n")
                input("Click Enter To Exit...")
                exit()
            else:
                banned += 1
                print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")
        except:
            banned += 1
            print(f"\rSent : {sent} | Spam : {spam} | Error: {banned}", end="")


threads = []
for i in range(threads_number + 1):
    t = threading.Thread(target=unban)
    t.start()
    threads.append(t)
for i in threads:
    i.join()
