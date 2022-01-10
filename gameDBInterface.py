import sqlite3
from sqlite3 import Error

class gameDBInterface:

    sql_delete = "DELETE FROM games;"

    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)



    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
    
    def insert_game_object(self, game):
        import pdb; pdb.set_trace()
        name = game.get_title()
        rank = game.get_rank()

        self.create_game_row(name, rank)

    def get_user_game_queue(self):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        import pdb; pdb.set_trace()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM games")

        rows = cur.fetchall()

        return list(rows)


    def create_game_row(self, name, rank):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        import pdb; pdb.set_trace()
        sql = ''' INSERT INTO games(name,rank)
                VALUES(?,?) '''
        
        cur = self.conn.cursor()
        
        game_values = (name, rank)
        
        cur.execute(sql, game_values)
        
        self.conn.commit()
        
        return cur.lastrowid

    def close_connection(self):
        self.conn.close()