from personnage import Personnage
from armure import Armor

class Soldier(Personnage):
    def __init__(self, nom, pv, attaque):
        super().__init__(nom, pv, attaque, Armor("Cote de maille", 15))

    def __str__(self):
        return f"{self.nom}:\nclass: Soldier\nhp: {self.pv}\nattack: {self.attaque}"

    def take_damage(self, amount : int):
        if amount - self.armor.armor_class >= 0:
            self.pv -= round((amount - self.armor.armor_class) * 0.9)