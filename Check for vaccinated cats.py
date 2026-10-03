import sqlite3

conn = sqlite3.connect('sweigartcats.db')

# Find cats with no vaccines
query_no_vaccines = """
SELECT cats.rowid, cats.name
FROM cats
LEFT JOIN vaccinations ON cats.rowid = vaccinations.cat_id
WHERE vaccinations.cat_id IS NULL
"""
print("Cats with no vaccines:")
for row in conn.execute(query_no_vaccines):
    print(f"ID: {row[0]}, Name: {row[1]}")

# Find vaccines administered before cat's birthday
query_vaccine_error = """
SELECT cats.name, vaccinations.vaccine, vaccinations.date_administered, cats.birthdate
FROM vaccinations
JOIN cats ON cats.rowid = vaccinations.cat_id
WHERE date(vaccinations.date_administered) < date(cats.birthdate)
"""
print("\nVaccines administered before cat's birthday:")
for row in conn.execute(query_vaccine_error):
    print(f"Cat: {row[0]}, Vaccine: {row[1]}, Date: {row[2]}, Birthdate: {row[3]}")

conn.close()