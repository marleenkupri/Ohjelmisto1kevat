import mysql.connector

country_code = input("Enter the country code (e.g., FI for Finland): ").upper()

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='marleenk',
    password='salasana',
    autocommit=True
)

cursor = connection.cursor()

sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type"
cursor.execute(sql, (country_code,))
airports = cursor.fetchall()

cursor.close()
connection.close()

# Tulosta tulokset
if not airports:
    print(f"No airports found for country code {country_code}.")
else:
    print(f"\nAirports in {country_code}:")
    for airport_type, count in airports:
        print(f"{count} {airport_type} airports")