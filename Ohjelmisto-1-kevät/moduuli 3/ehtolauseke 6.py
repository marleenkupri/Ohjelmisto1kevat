kahvi_on_hyvaa = True
kahvikone_kahvi_on_hyvaa = False

if kahvi_on_hyvaa == False on kahvikone_kahvi_on_hyvaa == False:
    print("Olet varmaan karamalmin kampuksella")

if kahvi_on_hyvaa == False or kahvikone_kahvi_on_hyvaa == False:
    print("Or looginen operaattori")

ika = float(input("Anna ikä: "))
nimi = input("Anna nimi: ")

if (ika > 18 or ika < 40 and nimi == "Juha"):
    print("Ikä on 18 ja 40 välillä, ei sisällä 18 eikä 40")

if not False:
    print("False ei ole tosi")