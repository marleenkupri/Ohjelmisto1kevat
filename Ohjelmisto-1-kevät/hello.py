print('Hello world')
print("hyvää\n\thuomenta")
käyttäjä = input("Anna nimesi:   ")
ikä = input("Anna ikäsi:   ")
print(f'"Hei", sanoi:\n\t{käyttäjä}, ikä: {ikä}')

luku1 = float(input("Anna luku:  "))
luku2 = float(input("Anna luku:  "))
tulo = luku1 * luku2
print(f"Lukujen {luku1} ja {luku2} tulo on {tulo}")

pisteet = 50 # Muuttujan pisteet arvo on nyt 50
print(pisteet) # Tulostaa: 50

pisteet = 120 # Nyt muuttujan pisteet arvo on 120
print(pisteet) # Tulostaa: 120

muuttuja = "tekstiä" # merkkijono eli string
print(muuttuja)

luku = 123 # kokonaisluku eli int
print(luku)

liukuluku = 3.2 # liukuluku eli float
print(liukuluku)

totuusarvo = True # totuusarvo eli boolean
print(totuusarvo)

eka = -9
toka = 12_343_678
kolmas = 4.55
neljäs = -4 + 2j

print(eka)
print(toka)
print(kolmas)
print(neljäs.real)
print(neljäs.imag)

hymiömerkkijono = "😊❤️"
print(hymiömerkkijono)

print(8 + 3)
print(8 - 3)
print(8 * 3)
print(8 / 3)
print(8 // 3) # pelkän kokonaisosan palauttava jakolasku
print(8 ** 3) # 8^3
print(8 % 3) # 8 - 3 - 3 = 2

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5 / 9
print("Lämpötila Celsius-asteina: " + str(celsius))
print(f"Lämpötila Celsius-asteina: {celsius:.3f}")

import math

print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")