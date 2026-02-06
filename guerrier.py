from personnage import Personnage
import random
class Guerrier(Personnage):
    
    
    def __init__(self, nom : str, pv : int, attaque : int, force : int):
        super().__init__(nom, pv, attaque)
        self._force = force

        self.force = self._force

    def __str__(self):
        return f"{self.nom}:\nclass: Warrior\nhp: {self.pv}\nattack: {self.attaque}\nStrenght: {self.force}"

    @property
    def force(self):
        return self._force
    @force.setter
    def force(self, amount : int):
        if amount <= 0:
            self._force = 0
        elif amount >= 50:
            self._force = 50
        else:
            self._force = amount

    def attaquer(self):
        return self.attaque - (self.force/2) + random.randint(-2,2)
