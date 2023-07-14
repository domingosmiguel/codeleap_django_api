# Run it once to create the database.

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

dataBaseConnection = None

try:
    dataBaseConnection = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
    )

    dataBaseConnection.autocommit = True

    cursorObject = dataBaseConnection.cursor()

    cursorObject.execute('CREATE DATABASE "{}"'.format(os.environ['DB_NAME'],))

    print('Database created.')

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if dataBaseConnection is not None:
        dataBaseConnection.close()
        print('Database connection closed.')
