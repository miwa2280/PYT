import psycopg2
import config

print(13381338133)

with psycopg2.connect(
    dbname=config.PGDATABASE,
    user=config.PGUSER,
    password=config.PGPASSWORD,
    host=config.PGHOST,
    port=5432,
) as connection:
    with connection.cursor() as cursor:
        sql_query_table_brand = """
        CREATE TABLE IF NOT EXISTS brand (
            id SERIAL PRIMARY KEY,
            name VARCHAR(75) NOT NULL UNIQUE
        )
        """
        cursor.execute(sql_query_table_brand)

        sql_query_tables_customer_car = """
        CREATE TABLE IF NOT EXISTS customer (
            id SERIAL PRIMARY KEY,
            name VARCHAR(25) NOT NULL,
            tin VARCHAR(10)
        );

        CREATE TABLE IF NOT EXISTS car (
            id SERIAL PRIMARY KEY,
            model VARCHAR(20) NOT NULL,
            cost INTEGER,
            brand_id INTEGER REFERENCES brand(id),
            customer_id INTEGER REFERENCES customer(id)
        );
        """
        cursor.execute(sql_query_tables_customer_car)

        query_insert = "INSERT INTO brand (name) VALUES (%s)"
        cursor.execute(query_insert, ('BMW',))