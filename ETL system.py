import json
import psycopg2 as psycopg2
from faker import Faker
import random

class DataSource:
    # class to read the data from file or generate it in the console

    def data_source_simulation(self):
        # generate random dict
        fake = Faker('en_US')
        my_dict = {'num': random.randint(0, 100), 'name': fake.name(), 'value': float(random.randrange(155, 389))/100}

        return my_dict

    def data_source_file(self, file_name: str):
        # Opening JSON file
        f = open(file_name, )

        # returns JSON object as a dictionary
        # data = json.load(f)
        data = f.readlines()

        # Closing file
        f.close()

        return data

class DataSinkConsole(DataSource):

    def print_data_simulation_console(self, n=1):
        print("Print data generated from simulation:")
        for i in range(n):
            print(self.data_source_simulation())

    def print_data_file_console(self):
        print("Print data red from file:")
        for line in self.data_source_file("json_data.txt"):
            print(line)

class DataSinkPostgreSQL(DataSinkConsole):

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


if __name__ == '__main__':

    # Generate random data and print it to console
    data_source_sim = DataSinkConsole()
    data_source_sim.print_data_simulation_console(5)

    print()

    # Read data from file and print it to console
    ds_file = DataSinkConsole()
    ds_file.print_data_file_console()

    # To insert data in PostgreSQL
    # First create a list to store the generated data
    # And then use the list to update the database
    data_list = []
    ds_sql = DataSinkPostgreSQL()

    data_list.append(ds_sql.data_source_simulation())
    print(data_list)
    #ds_sql.open_connection()
    #ds_sql.insert_in_database(data_list)
    #ds_sql.close_connection()