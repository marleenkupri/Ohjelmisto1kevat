#indeksit  0      1     2         3
#lopusta   -4    -3     -2       -1
nimet = ["Juha", 123, "Matti", "Viivi"]
print(nimet)
print(nimet[1])
print(nimet[0])
print(nimet[-1])
print(nimet[-2])

#TODO: Lisää if-lauseke
#print(nimet[4])

print(nimet)
print("Nimet alkiosta 1 alkioon 3")
print(nimet[1:3])
print(nimet[:3])

uusi_lista = nimet[1:3]
print("Uuden lsitan tulostus")
lista = []
print(lista)
print(nimet)

print(len(nimet))
print(len(uusi_lista))
print(len(lista))
print(len([]))
print([1,2,3,4])

nimet = []
nimi = input("Anna nimi: ")
while nimi != "":
    nimet.append(nimi)
    nimi = input("Anna nimi: ")
    print(nimet)

numerot = [1, 2, 3, 4]
for i in  numerot:
    print(i)

numerot2 = range(1, 60000, 1000)
for i in numerot2:
    print(i)

numerot3 = range(10, 0, -2)
for i in numerot3:
    print(i)

for luku in range(6):
    print ("Moi!")
