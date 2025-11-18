import requests
import time
import datetime

# ------------------------------
# TRM BULUT BAŞLATICI (STABLE)
# ------------------------------

URL = "https://www.google.com"   # İnternet kontrol linki

def internet_kontrol():
    try:
        requests.get(URL, timeout=5)
        return True
    except:
        return False

def log_yaz(metin):
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[TRM_BULUT] {zaman} - {metin}")

def calistir():
    log_yaz("Bulut starter çalışıyor...")

    if internet_kontrol():
        log_yaz("İnternet bağlantısı OK ✔")
        log_yaz("TRM otomasyon tetiklendi (örnek çalışma).")
    else:
        log_yaz("İnternet yok ❌ - Bir sonraki döngü beklenecek.")

# ------------------------------
# ANA DÖNGÜ (Her 15 dakikada 1 çalışır)
# ------------------------------

if __name__ == "__main__":
    log_yaz("Bulut servis başlatıldı ✔")

    while True:
        calistir()
        time.sleep(900)   # 15 dakika (900 saniye)
