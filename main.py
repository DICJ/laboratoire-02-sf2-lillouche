from mage import Mage
from guerrier import Guerrier
from archer import Archer
from arena import Arena
from personnage import Personnage
from soldier import Soldier


def create_char()-> Personnage:
    """func pour cree un personnage

    Returns:
        Personnage: return le personnage creer
    """
    classe = int(input("(0) Warrior\n(1) Mage\n(2) Archer\n(3) Soldat\nChoix de la classe: "))
    name = input("Nom du personnage: ")
    hp = int(input("pv du personnage: "))
    attack = int(input("attaque du personnage: "))
    if classe == 0:
        spc_stat = int(input("Force du personnage: "))
        char = Guerrier(name, hp, attack, spc_stat)
    elif classe == 1:
        spc_stat = int(input("Mana du personnage: "))
        char = Mage(name, hp, attack, spc_stat)
    elif classe == 2:
        spc_stat = int(input("Dexterite du personnage: "))
        char = Archer(name, hp, attack, spc_stat)
    elif classe == 3:
        char = Soldier(name, hp, attack)
    return char

playing = True
while playing == True:
    print("----Jeu d'arene----\n(1) Ajouter un personnage\n(2) Voir les personnages dans l'arene d'arene\n(3) Faire combattre deux personnages\n(4) Revoir des combats\n(5) heal un perso\n(6) Nombre de perso dans l'arene\n(7) Battle royale\n(8) Quitter")
    choix = int(input("Votre choix: "))
    match choix:
        case 1:
            Arena.add_character(create_char())
        case 2:
            Arena.view_characters()
        case 3:
            Arena.view_characters()
            choix1 = int(input("Quel premier personnage voulez vous voir se battre?: "))
            choix2 = int(input("Quel deuxieme personnage voulez vous voir se battre?: "))
            Arena.combat(choix1,choix2)
        case 4:
            Arena.list_combat()
            choix = int(input("Quel combat voulez vous voir?: "))
            Arena.view_fight(choix)
        case 5:
            Arena.view_characters()
            choix = int(input("Quel personnage voulez vouz soigner"))
            Arena.heal_char(choix)
        case 6:
            print(f"il y a {len(Arena.character_lst)} personnages dans l'arene")
        case 7:
            Arena.battle_royale()
        case 8:
            playing = False
        case _:
            print("choix invalide reessayez")