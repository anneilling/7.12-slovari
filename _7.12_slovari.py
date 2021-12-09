
sonastik={}
riigid=[]
linnad=[]
file=open("Text.txt", "r")
for line in file:
    k, v=line.strip().split(" - ")
    sonastik[k.strip()] = v.strip()
    riigid.append(k)
    linnad.append(sonastik[k.strip()])
file.close()
print(sonastik)
print("Riigid: ")
print(riigid)
print("Pealinnad: ")
print(linnad)
a=input()


       