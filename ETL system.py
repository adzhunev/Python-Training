import json
import psycopg2 as psycopg2
from faker import Faker
import random

class DataSource():
    # class to read the data from file or generate it in the console

    def __init__(self, data):
        self.data = data

    def data_sourse_simulation(self):
        # generate random dict
        fake = Faker('en_US')
        my_dict = {'num': random.randint(0, 100), 'name': fake.name(), 'value': float(random.randrange(155, 389))/100}
        #print(my_dict)
        return my_dict

    def data_sourse_file(self, file_name: str):
        # Opening JSON file
        f = open(file_name, )

        # returns JSON object as a dictionary
        data = json.load(f)

        #print(data)

        # Closing file
        f.close()

        return data

class DataSink:

    def __init__(self, dict):
        self.dict = dict

    def data_sink_print_console(self, dict):
        print(dict)

class DataSinkPostgreSQL(DataSink):

    def open_connection(self):
        # method to open a connection to the database

        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(host="localhost", database_name="my_database", user="username", password="password")
            cur = conn.cursor()
            cur.execute('SELECT version()')
            print('CONNECTION OPEN: PostgreSQL database version: ')
            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn = None
            cur = None

        return conn

    def close_connection(conn):
        # method to close a connection to the database
        try:
            conn.close()
            print('Closed connection to the PostgreSQL database')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def insert_in_database(self, sql_string, cur=None, conn=None):
        if cur != None:
            try:
                cur.execute(sql_string)
                conn.commit()

                print('\nfinished INSERT INTO execution')

            except (Exception) as error:
                print("\nexecute_sql() error:", error)
                conn.rollback()
