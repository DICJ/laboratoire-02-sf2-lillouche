
class DetailCombat:

    def __init__(self, combat : str, char_name1 : str, char_name2 : str):
        self.combat = combat # String des tours du combat
        self.char_name1 = char_name1
        self.char_name2 = char_name2
        self.winner = ""
        self.turns = 0

    def __str__(self):
        return f"Combat entre {self.char_name1} et {self.char_name2}" #nom du combat
    
    def define_winner(self, winner : str):
        """defini le vainqueur

        Args:
            winner (str): vainqueur du combat
        """
        self.winner = winner

    def increment_turns(self):
        """Func qui incremente 1 au tour
        """
        self.turns += 1

