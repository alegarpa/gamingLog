from game import Game
from gameDBInterface import gameDBInterface
import sqlite3
from sqlite3 import Error

def main():
    database_file = r"C:\sqlite\db\rankedlist.db"

    data = {"Xenogears": 1 ,"SMT 4A": 2, "Dark Holes": 3, "FF 5": 3,"FE SoV": 4, "Danganronpa 2": 5,
            "SMT DDS 1": 6, "SMT DDS 2": 7 ,"SMT Raidou": 8, "Dragon Quest 9": 9}

    game_list =[]
    for key, value in data.items():
        game_list.append(Game(key, value))
    
    game_db_conn = gameDBInterface(database_file)

    """for game in game_list:
        import pdb; pdb.set_trace()
        game_db_conn.insert_game_object(game)"""
    
    import pdb; pdb.set_trace()
    print(game_db_conn.get_user_game_queue())

    game_db_conn.close_connection()





if __name__ == '__main__':
    main()

    