# Check for vaccinated cats.py

**Database Query and Print Analysis**

This Python script uses the SQLite database library to connect to a database file named 'sweigartcats.db'. It then executes two SQL queries to find specific information in the database and prints the results.

### First Query: Cats with No Vaccines

The first query is as follows:

```sql
SELECT cats.rowid, cats.name
FROM cats
LEFT JOIN vaccinations ON cats.rowid = vaccinations.cat_id
WHERE vaccinations.cat_id IS NULL
```

This query returns the row IDs and names of cats in the database that do not have any vaccine records. Here's how it works:

1. The `LEFT JOIN` combines rows from the `cats` and `vaccinations` tables where the `cat_id` column from `vaccinations` is equal to the `rowid` column from `cats`.
2. The `WHERE` clause filters the results to only include rows where there is no match in the `vaccinations`