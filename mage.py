from personnage import Personnage
from armure import Armor
import  random
class Mage(Personnage):
    def __init__(self, nom : str, pv : int, attaque : int, mana : int):
        super().__init__(nom, pv, attaque, Armor("armure magique", 7))
        self._mana = mana

        self.mana = self._mana
        self._max_mana = mana

    def __str__(self):
        return f"{self.nom}:\nclass: Mage\nhp: {self.pv}\nattack: {self.attaque}\nMana: {self.mana}"
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, amount : int):
        if amount <= 0:
            self._mana = 0
        elif amount >= 100:
            self._mana = 100
        else:
            self._mana = amount

    @property
    def max_mana(self):
        return self._max_mana
    
    @max_mana.setter
    def max_mana(self, amount):
        self._max_mana = amount

    def attaquer(self):
        damage = self.attaque
        if self.mana >= 0:
            damage += 60
            self.diminuer_mana()
        return damage
    
    def diminuer_mana(self):
        self.mana -= random.randint(-25, -15)

    def reset(self):
        self.pv = self.max_life
        self.mana = self.max_mana
