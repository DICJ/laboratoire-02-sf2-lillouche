from personnage import Personnage
import random
class Archer(Personnage):
    def __init__(self, nom, pv, attaque, dext : int):
        super().__init__(nom, pv, attaque)
        self._dext = dext

        self.dext = self._dext


    def __str__(self):
        return f"{self.nom}:\nclass: Archer\nhp: {self.pv}\nattack: {self.attaque}\ndexterity: {self.dext}"
    
    @property
    def dext(self):
        return self._dext
    @dext.setter
    def dext(self, amount : int):
        if amount <= 50:
            self._dext = 50
        elif amount >= 100:
            self._dext = 100
        else:
            self._dext = amount

    def attaquer(self)-> int:
        """func pour faire des degats

        Returns:
            int: les degats
        """
        num = random.randint(0,100)
        damage = self.attaque + 15
        if num < self.dext:
            return damage*2
        else:
            return damage

