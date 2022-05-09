import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from random import choice

r = sr.Recognizer()
def record(ask= False):
    if ask:
        print(ask)
        speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR').lower()
        except sr.UnknownValueError:
            print('Sizi anlayamadım. Lütfen tekrar edin.')
            speak('Sizi anlayamadım. Lütfen tekrar edin.')
        except sr.RequestError:
            print('Sistem Çalışmıyor.')
            speak('Sistem Çalışmıyor.')
        return voice
def response(voice):
    if 'asistan' in voice:

        if 'nasılsın' in voice or 'ne haber' in voice:
            sohbet = ["İyiyim teşekküler seni sormalı?", "İyiyim sen nasılsın?", "İyi diyelim iyi olsun.", "Her şey yolunda.", "Sesini duydum daha iyi oldum."]
            rasgele = choice(sohbet)
            print(rasgele)
            speak(rasgele)

        elif 'nasıl gidiyor' in voice:
            sohbet = ["İdare ediyoruz.", "Geçinip gidiyoruz.", "Mükemmel gidiyor çünkü beni hatırladın.", "Her şey yolunda.", "Mükemmel gidiyor çünkü kendimi her gün geliştiriyorum."]
            rasgele = choice(sohbet)
            print(rasgele)
            speak(rasgele)

        elif 'saat kaç' in voice:
            print('Saat: ' + datetime.now().strftime("%H:%M:%S"))
            speak('Saat: ' + datetime.now().strftime("%H:%M:%S"))

        elif 'arama yap' in voice:
            search = record('Ne aramak istiyorsun?')
            url = 'https://google.com/search?q='+search
            webbrowser.get().open(url)
            print(search + ' için bulduklarım.')

        elif "youtube'da ara" in voice:
            search = record('Ne aramak istiyorsun?')
            url = 'https://www.youtube.com/results?search_query='+search
            webbrowser.get().open(url)
            print("İslenilen arama yapılmıştır.")
            speak(search+" 'için youtube'da arama yapılmıştır.")

        elif 'not defteri oluştur' in voice:
            isim = record('Not defterinizin adı ne olsun?')
            olustur = open(isim + ".txt", "w")
            print('Dosyanız başarılı bir şekilde oluştu.')
            speak('Dosyanız başarılı bir şekilde oluştu.')

        elif 'word belgesi oluştur' in voice:
            isim = record('Word dosyanızın adı ne olsun?')
            olustur = open(isim + ".docx", "w")
            print('Dosyanız başarılı bir şekilde oluştu.')
            speak('Dosyanız başarılı bir şekilde oluştu.')

        elif 'okuma metni oluştur' in voice:
            isim = record('Okuma metninizin adı ne olsun?')
            olustur = open(isim + ".pdf", "w")
            print('Dosyanız başarılı bir şekilde oluştu.')
            speak('Dosyanız başarılı bir şekilde oluştu.')

    elif 'kapat' or 'görüşürüz' or 'kendine iyi bak' in voice:
        sozluk = ["Kendine iyi bak arkadaşım.", "Beni unutma!", "Sadece işin düştüğünde değil, sohbet için de seslen :)",
                "Asistanın hep burada seni bekliyor.", "Görüşürüz sevgili arkadaşım."]
        rasgele= choice(sozluk)
        print(rasgele)
        speak(rasgele)
        exit()



def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,100000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

print('Size nasıl yardımcı olabilirim?')
speak('Size nasıl yardımcı olabilirim?')
time.sleep(1)

while 1:
    voice = record()
    if 'asistan' in voice:
        print(voice)
    response(voice)