class Game:
    
    def __init__(self, title, rank):
        self.title = title
        self.rank = rank

    def set_rank(self, rank):
        self.rank = rank

    def set_title(self, title):
        self.title = title

    def get_rank(self):
        return self.rank

    def get_title(self):
        return self.title