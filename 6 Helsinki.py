print("\nHelsinki érettségi feladat 2017 május")
print("\n-------------------------------------------------\n")
print("2.Feladat: Beolvasás")
Helsinki_Adatok=[]
db=0
with open("helsinki.txt","r",encoding="utf-8") as helsinkiAdatok:
    for egySor in helsinkiAdatok:
        egyHelsinki=egySor.strip().split(" ")
        Helsinki_Adatok.append([int(egyHelsinki[0]), int(egyHelsinki[1]),egyHelsinki[2],egyHelsinki[3]])
        db+=1
if(db>0):
    print("\tSikeres beolvasás, beolvasott sorok száma: ",db)
else:
    print("\tSikertelen beolvasás próbálja újra")
print("\n------------------------------------------------\n")
print("3.Feladat:határozza meg a pontszerző helyezések számát")
print("\tPontszerző helyezések száma: ",len(Helsinki_Adatok))
print("\n------------------------------------------------\n")
print("4.Feladat: helyezések száma")
Aranydb=0
Ezustdb=0
Bronzdb=0
for i in range(len(Helsinki_Adatok)):
    if(Helsinki_Adatok[i][0]==1):
        Aranydb+=1
    elif(Helsinki_Adatok[i][0]==2):
        Ezustdb+=1
    elif(Helsinki_Adatok[i][0]==3):
        Bronzdb+=1
print("\tArany érmek száma: ",Aranydb)
print("\tEzüst érmek száma: ",Ezustdb)
print("\tBronz érmek száma: ",Bronzdb)
print("\tHelyezések melyek érmekket hoztak: ",Aranydb+Ezustdb+Bronzdb)
print("\n--------------------------------------------------\n")
print("5.Feladat: olimpiai pontok száma")
Egydb=0
Kettodb=0
Haromdb=0
Negydb=0
Otdb=0
Hatdb=0
for i in range(len(Helsinki_Adatok)):
    if(Helsinki_Adatok[i][0]==1):
        Egydb+=1
    elif(Helsinki_Adatok[i][0]==2):
        Kettodb+=1
    elif(Helsinki_Adatok[i][0]==3):
        Haromdb+=1
    elif(Helsinki_Adatok[i][0]==4):
        Negydb+=1
    elif(Helsinki_Adatok[i][0]==5):
        Otdb+=1
    elif(Helsinki_Adatok[i][0]==6):
        Hatdb+=1
Olimpiai_Pontok=Egydb*7+Kettodb*5+Haromdb*4+Negydb*3+Otdb*2+Hatdb*1
print("\tAz olimpiai pontok száma: ",Olimpiai_Pontok)
print("\n------------------------------------------------------------\n")
print("6.Feladat: legtöbb érem torna vagy úszás?")
Uszasdb=0
Tornadb=0
for i in range(len(Helsinki_Adatok)):
    if(Helsinki_Adatok[i][2]=="uszas"):
        Uszasdb+=1
    elif(Helsinki_Adatok[i][2]=="torna"):
        Tornadb+=1
if(Uszasdb>Tornadb):
    print("\tAz úszás volt a legsikeresebb sportág 1952-ben")
elif(Tornadb>Uszasdb):
    print("\tA torna volt a legsikeresebb sortág 1952-ben")
print("\n------------------------------------------------------------\n")
print("7.Feladat: File-ba írás:")
for i in range(len(Helsinki_Adatok)):
    szoveg = Helsinki_Adatok[i][0], Helsinki_Adatok[i][1], Helsinki_Adatok[i][2].replace('kajakkenu', 'kajak-kenu'),Helsinki_Adatok[i][3]
    print(szoveg)

print("\n------------------------------------------------------------\n")
print("8.Feladat: legtöbb sportoló")
Legtobbsportolo=0
MaxSportag="cica"
MaxHelyezes=0
MaxVersenySzam="cica"
for i in range(len(Helsinki_Adatok)):
    if(Legtobbsportolo<Helsinki_Adatok[i][1]):
        Legtobbsportolo=Helsinki_Adatok[i][1]
        MaxSportag=Helsinki_Adatok[i][2]
        MaxHelyezes=Helsinki_Adatok[i][0]
        MaxVersenySzam=Helsinki_Adatok[i][3]
print("\tHelyezes:",MaxHelyezes,"\n\tSportág: ",MaxSportag,"\n\tVeresenyszám: ",MaxVersenySzam,"\n\tSportolók száma: ",Legtobbsportolo)