import requests 
import random 
import os

while True:
    renk = random.randint(1,5)
    try :
        if renk == 1 :
            renk = "color a" 
        elif renk == 2 :
            renk = "color b"
        elif renk == 3 :
            renk = "color c"
        elif renk == 4 :
            renk = "color d"
        elif renk == 5 :
            renk = "color e"
        os.system(renk)
        linke = "https://www.google.com"
        req = requests.get(linke , headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"})
        bilgi2 = str(req.status_code)
        bilgi1 = str(req.elapsed)
        print("[+] Link  "+linke+"    |   Geçen Süre  "+bilgi1+"       |    Durum Kodu  "+bilgi2+"     [+] \n")
    except Exception:
        print("[+] Bilinmeyen Hata [+]")