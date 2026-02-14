class Armor:

    def __init__(self, name : str, armor_class : int):
        self.name = name
        self._armor_class = armor_class

        self.armor_class = self._armor_class

    @property
    def armor_class(self):
        return self._armor_class
    
    @armor_class.setter
    def armor_class(self, amount : int):
        if amount >= 15:
            self._armor_class = 15
        elif amount <= 0:
            self._armor_class = 0
        else:
            self._armor_class = amount