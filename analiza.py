log = open("stevke.txt", "r")
stevke = log.read()
log.close()

seznam_stevk = stevke.split(" ")
skupno_stevk = len(seznam_stevk)

#Seznam napak je bil skopiran iz notepada, ki jih je zapisoval

napake = "sex. hate. sex. gyro. gyro. sex. hate. shakes. find. gyro. Jared. gyro. pho. hate. side. pho. hate. sex. hate. hate. sex. hi. sex. shakes. sex. hi. hate. sex. hate. pho. pho. hate. hate. hate. sex. hole. hi. sex. hate. gyro. shakes. hi. hate. pho. pho. gyro. hate. pho. full. hate. hate. sex. gyro. sex. sex. gyro. so. hate. Jared. pho. hi. hi. gyro. gyro. gyro. shakes. gyro. sex. sex. hate. gyro. hate. so. hate. shakes. soul. hate. hate. shakes. hate. Jared. sex. hate. Jared. full. hate. gyro. gyro. full. hate. hate. sex. Jared. sex. shakes. dude. full."
seznam_napak = napake.split(". ")

skupno_napak = len(seznam_napak)
bes_napak = list(set(seznam_napak))

#['sex', 'pho', 'then.', 'hi', 'shakes', 'Jared', 'soul', 'full', 'dude', 'side', 'find', 'hate', 'so', 'gyro', 'hole']

"""
0 = 'gyro'
2 = 'dude'
4 = 'pho', 'full', 'soul', 'find'
6 = 'sex', 'shakes', 'side', 'so'
7 = 'jared', 
8 = 'hate', 'hole', 
9 = 'hi', 
"""

analiza = open("analiza.txt", "a")
zapis = "Skupno stevilo poslusanih besed: " + str(skupno_stevk) + "\n"
analiza.write(zapis)
zapis = "Skupno stevilo napak: " + str(skupno_napak) + "\n"
analiza.write(zapis)

for i in range(10):
    zapis = "Stevilo " + str(i) + " se je ponovilo " + str(seznam_stevk.count(str(i))) + "-krat, kar predstavlja " + str(round(seznam_stevk.count(str(i)) /skupno_stevk, 2) * 100) + "%\n"
    analiza.write(zapis)
for i in bes_napak:
    zapis = "Napaka " + str(i) + " se je ponovila " + str(seznam_napak.count(str(i))) + "-krat, kar predstavlja " + str(round(seznam_napak.count(str(i)) /skupno_napak, 2) * 100) + "%\n"
    analiza.write(zapis)


zapis = "Delez napak pri strojni izgovorjavi je " + str(round(skupno_napak / skupno_stevk, 2) * 100) + "%\n"
analiza.write(zapis)
for i in range(10):
    zapis = "Stevilo " + str(i) + " je napacno prebrano -krat, kar predstavlja % napako.\n"
    analiza.write(zapis)
analiza.close()

