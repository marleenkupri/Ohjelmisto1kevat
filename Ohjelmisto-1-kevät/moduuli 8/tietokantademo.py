import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='marleenk',
         password='salasana',
         autocommit=True,
         collation='utf8mb4_unicode_ci'
         )

def hae_data():
    sql = "SELECT name, ident, latitude_deg FROM airport LIMIT 10"
    spl2 = "SELECT country. FROM country"

    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()

    print(tulos)
    print(tulos[0])
    print(tulos[0][0])

    for rivi in tulos:
        print(rivi)

hae_data()

def lisää_uusi_kenttä(ident,name):
    sql = "SELECT id, name, municipality FROM airport WHERE id = 10000 BY id LIMIT 5"

    kursori = yhteys.cursor()
    kursori.execute(sql)