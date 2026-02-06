class Personnage:
    def __init__(self, nom : str, pv : int, attaque : int):
        self.nom = nom
        self._pv = pv
        self._attaque = attaque

        self.attaque = self._attaque
        self.pv = self._pv

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

    def take_damage(self, amount : int):
        self.pv -= amount

