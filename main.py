from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item

#create black magic
fire = Spell ("fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
meteor = Spell("meteor", 15, 85, "black")
blizzard = Spell("Blizzard", 20, 100, "black")
quake = Spell("Quake", 14, 100, "black")

#create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item ("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


#
#
#       {"name": "Thunder", "Cost": 10, "dmg": 60},
#        {"name": "Blizzard", "Cost": 10, "dmg": 60}]

player_spells = [fire, thunder, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]


#instantiate People
player1 = Person("Valos", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot", 460, 65, 60, 34, player_spells, player_items)
enemy1 = Person("Magus", 1200, 65, 45, 25, [], [])

players = [player1,player2, player3]
enemies = [enemy1]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("====================")

    for player in players:
        print("\n\n")
        player.get_stats()
        print("\n)"
        player.choose_action()
        choice = int(input("    Choose action:")) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for: ", dmg, "points of damage. Enemy HP: ", enemy.get_hp())
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice == -1:
                continue

    #        magic_dmg = player.generate_spell_damage(magic_choice)
     #       spell = player.get_spell_name(magic_choice)
     #       cost=player.get_spell_mp_cost(magic_choice)

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print (bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue


            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print (bcolors.OKBLUE + "\n" + spell.name + "heals for ", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type =="black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage")
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.item[item_choice]["item"]

            if player.item[item_choice]["quantity"] == 0:
                print[bcolors.FAIL + "\n" +"None left" + bcolors.ENDC]
                continue

            player.item[item_choice]["quantity"] -= 1




            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" +item.name + "heals for", str(item.prop), "HP" +bcolors.ENDC)
            elif item.type =="elixer":
                player.hp = player.maxhp
                player.mp = player.maxhp
                print(bcolors.OKGREEN + "\n" +item.name + "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    #    enemy.take_damage(magic_dmg)
    #    print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)


    enemy_choice = 1



    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("enemy attacks for ", enemy_dmg, "Player HP:")

    print("------------------")
    print("enemy hp is:", bcolors.FAIL + str(enemy.get_max_hp())+ "/" + str(enemy.get_hp())+ bcolors.ENDC + "\n")

#    print("Your hp :", bcolors.OKGREEN + str(player.get_max_hp()) + "/" + str(player.get_hp())+ bcolors.ENDC)
#    print("your mp:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp())+ bcolors.ENDC + "\n")

    if enemy.get_hp() <= 0:
        print(bcolors.OKGREEN + "You win!" +bcolors.ENDC)
        running = False
    elif player.get_hp() <= 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" +bcolors.ENDC)
        running = False






