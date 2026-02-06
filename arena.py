from personnage import Personnage
from detailCombat import DetailCombat


class Arena:

    character_lst = []
    historique_combat = []

    @classmethod
    def add_character(cls, character : Personnage):
        """func pour import des characters

        Args:
            character (Personnage): Un personnage
        """
        Arena.character_lst.append(character)

    @classmethod
    def view_characters(cls):
        """Func pour voir les personnages dans l'arene
        """
        string = "\nPersonnages"
        index = 0
        for i in Arena.character_lst:
            string += f"\n({index}) {i.__str__()}"
            index += 1
        print(string)

    @classmethod
    def combat(cls, attacker1 : int, attacker2 : int):
        """ func pour faire combattre deux personnages

        Args:
            attacker1 (int): index du premier attaquant
            attacker2 (int):  index du deuxieme attaquant
        """
        fight = 0
        attacker = 0
        defenser = 0
        tour = 0
        combat_info = ""
        while fight >= 0:
            fight +=1
            if fight % 2 != 0:
                attacker = attacker1
                defenser = attacker2
            elif fight % 2 == 0:
                attacker = attacker2
                defenser = attacker1
            damage = Arena.character_lst[attacker].attaquer()
            Arena.character_lst[defenser].take_damage(damage)
            tour +=1
            combat_info += f"Tour {tour}\n{Arena.character_lst[attacker].nom} fait {damage} degat a {Arena.character_lst[defenser].nom}\n"
            if Arena.character_lst[defenser].pv <= 0:
                combat_info += f"{Arena.character_lst[attacker].nom} gagne le combat"
                print(combat_info)
                Arena.historique_combat.append(DetailCombat(combat_info, Arena.character_lst[attacker].nom, Arena.character_lst[defenser].nom))
                Arena.historique_combat[len(Arena.historique_combat) - 1].define_winner(Arena.character_lst[attacker].nom)
                Arena.character_lst.pop(defenser) #tue le personnage (il est mort)
                break
            
    def view_fight(index : int):
        """permet de revoir un combat precedent

        Args:
            index (int): index du combat dans la liste
        """
        print(Arena.historique_combat[index].combat)

    def list_combat():
        """Voir la liste d'hitorique de combat
        """
        string = "\nCombats precedent:"
        for i in range(len(Arena.historique_combat)):
            string += f"\n({i}) {Arena.historique_combat[i].__str__()}"
        print(string)