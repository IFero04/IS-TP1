import psycopg2
from datetime import datetime


class PostgresDB:
    def __init__(self):
        self.curr = None
        self.conn = None
        self.create_connection()

    def create_connection(self):
        self.conn = psycopg2.connect(
            dbname='is',
            user='is',
            password='is',
            host='is-db',
            port='5432'
        )
        self.curr = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.curr.close()
            self.conn.close()

    def store_xml(self, xml, file_name):
        try:
            self.curr.execute('''
                INSERT INTO imported_xml(xml, file_name) 
                VALUES (%s, %s)
                ON CONFLICT (file_name) DO UPDATE 
                SET xml = EXCLUDED.xml, updated_on = CURRENT_TIMESTAMP
                RETURNING created_on, updated_on
            ''', (xml, file_name))

            result = self.curr.fetchone()

            self.conn.commit()

            if result:
                created_on, updated_on = result

                if created_on == updated_on:
                    return "salvo"
                else:
                    return "atualizado"

        except psycopg2.DatabaseError as exception:
            self.conn.rollback()
            self.close_connection()
            raise Exception(exception)

    def execute_query(self, query, parameters=None):
        try:
            if parameters:
                self.curr.execute(query, parameters)
            else:
                self.curr.execute(query)

            result = self.curr.fetchall()
            self.conn.commit()
            return result

        except psycopg2.DatabaseError as exception:
            self.conn.rollback()
            self.close_connection()
            raise Exception(exception)

