from test import enlapsed
from requests import request
from itertools import starmap
import time 
import requests




def get_urls_from_user():
    urls: list[str] =[]
    while True:
        site=input("site gir(bitirmek için boş bırak)")
        if site == "":
            break
        # kullanıcı "google" gibi noktasız yazdıysa .com ekleyelim
        if "." not in site: 
            site = site + ".com"
 
        if not site.startswith(("http://", "https://")):
            site="https://" +site
        urls.append(site)
    return urls



def check_url(url:str, timeout: int = 5):

    start = time.time ()
    try:
        response = requests.get(url, timeout=timeout,headers ={"user-agent":"status-checker/1.0"})
        end = time.time()
        enlapsed_ms = int ((end - start)*1000)
        return response.status_code,enlapsed_ms,""
    except Exception as e : 
        end = time.time()
        enlapsed_ms = int ((end - start)*1000)
        return None,enlapsed_ms, type (e).__name__


def main ():
    urls=get_urls_from_user()



    if not urls:
        print("Hiç site girmedin. Program bitti")
        return


    print("\n---Sonuçlar---")

    for url in urls:
        status,ms,err=check_url(url)
        if status is None:
            print(f"{url} -> FAILED ({ms}ms)|{err}")
            continue
        slow_flag = " ⚠ SLOW" if ms > 500 else ""
        print(url, status, ms, "ms", slow_flag)



if __name__ == "__main__":
    main()



    
