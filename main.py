import os
import time
import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="[TRM_CLOUD] %(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("CHAT_ID", "").strip()
SLEEP_SECONDS = int(os.getenv("SLEEP_SECONDS", "3600"))  # default: 1 saat

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_text(text: str) -> None:
    if not BOT_TOKEN or not CHAT_ID:
        logger.error("BOT_TOKEN veya CHAT_ID tanimli degil.")
        return
    try:
        resp = requests.post(
            API_URL,
            data={"chat_id": CHAT_ID, "text": text},
            timeout=30,
        )
        if resp.status_code != 200:
            logger.error("Telegram hata kodu: %s, cevap: %s", resp.status_code, resp.text)
        else:
            j = resp.json()
            if not j.get("ok"):
                logger.error("Telegram OK degil: %s", j)
            else:
                logger.info("Mesaj gonderildi.")
    except Exception as e:
        logger.error("Mesaj gonderim hatasi: %s", e)

def main_loop():
    logger.info("TRM_CLOUD bot basladi. Dongu suresi: %s sn", SLEEP_SECONDS)
    send_text("TRM_CLOUD bot bulutta calismaya basladi 💙")
    while True:
        logger.info("Periyodik mesaj gonderiliyor...")
        send_text("TRM_CLOUD periyodik mesaj testidir.")
        time.sleep(SLEEP_SECONDS)

if __name__ == "__main__":
    main_loop()
