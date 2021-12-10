from gtts import gTTS
import os

sonastik={} #sõnastiku loomine
riigid=linnad=[]
file=open("Text.txt", "r") #tekstifaili avamine
for line in file: #tsükkli loomine
    k, v=line.strip().split(" - ") #
    sonastik[k.strip()] = v.strip()
    riigid.append(k.strip()) #sisestame iga valitud üksuse lõppu meetodi parameetris määratud sisu ja tagastame riidu koopia
    linnad.append(v) 
file.close() #paneme faili kinni


while True: #mugavuse huvids kasutame tsükkli
    print("Euroopa riigid")
    print("1 - Tunnustame riiki või pealinna\n2 - Lisame uut riiki või pealinna\n3 - Kontrolli enda") #kasutaja teeb valiku
    v=int(input())
    if v==1:
        b=int(input("Pealinna teadmiseks - 1\nRiiki pealinnast teadmiseks - 2\n"))
        if b==1:
            riik=input("Sisestage riiki nime: ")
            print("Selle riiki pealinn on ",sonastik[riik])
        elif b==2:
            linn=input("Sisestage pealinnu nime ")
            print("Selle pealinnu riik on " , riik)
        else:
            print("1 / 2")
    elif v==2:
        a=input("Sisestage riik või pealinn mida soovite liisada, kasutage - sümboli ")
        #file=open("Text.txt" , "x") #avab kirjutamiseks, kui faili pole olemas 
        file=open("Text.txt" , "a") #liisab infot faili lõpuks
    elif v==3:
        v=input("Venemaa pealinn on... ")
        if v=="Moskva":
            print("Õige.")
        else:
           print("Vale!")
    else:
        print("Vale valik.") #kui kasutaja valis vale numbrit siis palume uuesti valida


s=gTTS(text=linnad[8],lang="et",slow=False).save("heli.mp3") #määrame helifaili väärtus
os.system("heli.mp3") #hellifaili esitamine


       