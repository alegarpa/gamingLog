class GameQueue:

    def __init__(self, entry=[]):
        self.games = entry
        self.queue_size = len(self.games)
        self.game_map = {}
    
    def add_game(self, game):
        self.games.append(game)

    def add_games(self, game_list):
        for game in game_list:
            self.add_game(game)

    def insert_game_at_pos(self, game, pos):
        self.games.insert(pos, game)

    def move_game_to_pos(self, game, pos):
        current_game_pos = self.games.index(game)
        self.games.pop(current_game_pos)
        self.games.insert(pos, game)

    def remove_game(self, game):
        self.games.index(game)
        self.games.pop(current_game_pos)



data = ["Xenogears" ,"SMT 4A", "Dark Holes", "FF 5" ,"FE SoV","Danganronpa 2",
        "SMT DDS 1" ,"SMT DDS 2" ,"SMT Raidou" ,"Dragon Quest 9"]

new_game = "Persona 1"
newer_game = "SMT Devil Survivor 2"

myQueue = GameQueue(data)

myQueue.add_game(new_game)
myQueue.insert_game_at_pos(newer_game, 3)