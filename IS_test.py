import time
import random

try:
    from gtts import gTTS
except:
    raise ModuleNotFoundError("gTTS ni bil najden")
try:
    import vlc
except:
    raise ModuleNotFoundError("vlc ni bil najden")

#konstante

besedilo = ""
jezik = "en"
stevilo_poskusov = 500
seznam_stevil = [x for x in range(10)]

#vpisi svojo pot tukaj
pot = r'C:\Users\Jure\Desktop\test.mp3'

"""
Spodnji funkciji testirata govorjenje števil od 1 do 9 (funkcija zacetno_branje_stevil)
in 9 do 1 (drugo_branje_stevil).
"""

def zacetno_branje_stevil():
    for i in seznam_stevil:
        besedilo = str(i)
        brano_besedilo = gTTS(text = besedilo, lang = jezik, slow = False)
        brano_besedilo.save("test.mp3")
        bralnik = vlc.MediaPlayer(pot)
        bralnik.play()

def drugo_branje_stevil():
    for i in list(reversed(seznam_stevil)):
        besedilo = str(i)
        brano_besedilo = gTTS(text = besedilo, lang = jezik, slow = False)
        brano_besedilo.save("test.mp3")
        bralnik = vlc.MediaPlayer(pot)
        bralnik.play()
        
"""
Spodnja funkcija generira nakljucno stevilo, ga zapise, prebere, shrani posnetek
in predvaja. Konstante definiramo zgoraj.
"""

def generiraj_tekst():
    n = 0
    while n < stevilo_poskusov:
        stevilo = str(random.choice(seznam_stevil))
        brano_besedilo = gTTS(text = stevilo, lang = jezik, slow = False)
        brano_besedilo.save("test.mp3")
        bralnik = vlc.MediaPlayer(pot)
        bralnik.play()
        stevilo += " "
        print("testiram ",stevilo, " testirati moram se ", stevilo_poskusov - n, " stevil.")
        with open("stevke.txt", "a") as log:
            log.write(stevilo)
        n += 1
        time.sleep(3)

generiraj_tekst()
