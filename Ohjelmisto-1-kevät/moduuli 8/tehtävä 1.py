import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='marleenk',
    password='salasana',
    autocommit=True
)

cursor = connection.cursor()

icao = input("Enter the ICAO code of an airport: ").upper()

sql = """
      select name, municipality
      from airport
      where ident = %s \
      """

cursor.execute(sql, (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}")
    print(f"Location: {result[1]}")
else:
    print(f"No airport found with ICAO code {icao}")

cursor.close()
connection.close()