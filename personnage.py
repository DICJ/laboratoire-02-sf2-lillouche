from armure import Armor
class Personnage:
    def __init__(self, nom : str, pv : int, attaque : int, armor : Armor):
        self.nom = nom
        self._pv = pv
        self._attaque = attaque
        self.armor = armor
        

        self.attaque = self._attaque
        self.pv = self._pv
        self._max_life = self.pv

    def __eq__(self, other : "Personnage"):
        if self.nom == other.nom and self.pv == other.pv:
            return True
        else:
            return False


    @property
    def pv(self):
        return self._pv
    @pv.setter
    def pv(self, amount : int):
        if amount <= 0:
            self._pv = 0
        elif amount >= 500:
            self._pv = 500
        else:
            self._pv = amount
    @property
    def attaque(self):
        return self._attaque
    
    @attaque.setter
    def attaque(self, amount : int):
        if amount <= 0:
            self._attaque = 0
        elif amount >= 50:
            self._attaque = 50
        else:
            self._attaque = amount

    @property
    def max_life(self):
        return self._max_life
    
    @max_life.setter
    def max_mana(self, amount):
        self._max_life = amount

    def take_damage(self, amount : int):
        if amount - self.armor.armor_class >= 0:
            self.pv -= amount - self.armor.armor_class
        

    def attaquer(self):
        return self.attaque
    
    def reset(self):
        self.pv = self.max_life

