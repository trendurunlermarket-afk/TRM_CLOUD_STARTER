TRM_CLOUD_STARTER (Fahri & Derya)

Bu paket, Telegram botunu bulutta (Render gibi bir platformda) calistirmak icin hazirlanmis basit bir isci (worker) servisidir.

Dosyalar:
- main.py           -> Telegram'a periyodik mesaj atan basit bot
- requirements.txt  -> Gerekli Python paketleri
- render.yaml       -> Render.com icin ornek servis ayari

Kullanmak icin:
1) Bu klasoru bir GitHub reposu olarak yukle.
2) Render.com'da New > Blueprint seckesinden bu repoyu sec.
3) Ortam degiskenlerini ayarla:
   - BOT_TOKEN  -> BotFather'dan aldigin token
   - CHAT_ID    -> @userinfobot veya getUpdates ile buldugun chat id
   - SLEEP_SECONDS -> Kac saniyede bir mesaj atsin (ornegin 3600)

Bu sadece bulut alt yapisini test etmek icin bir "starter"dir.
Sonraki adimda TRM_AUTO_FINAL ile ayni mantikta video/link gonderimi eklenebilir.
