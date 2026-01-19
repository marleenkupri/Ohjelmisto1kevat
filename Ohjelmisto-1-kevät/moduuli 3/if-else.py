ika = float(input("Anna ika: "))

ikä = int(input("Anna ikäsi: "))
if ikä >= 65:
    print("Olet eläkeiässä.")
elif ikä >= 18:
    print("Olet työiässä.")
elif ikä >= 7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")

print("Suoritus jatkuu pääohjelmassa")

if ika >= 18:
    print("Olet täysi-ikäinen")
else:
    print("Et ole täysi-ikäinen")