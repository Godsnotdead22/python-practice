# New Python file

import random

print("Welcome To Monster Slayer\n")

player_name = input("Whats Your Name Knight: ")
player_health = 100
player_attack = 20
player_xp = 0
xp_reward = 25
#POTION INVENTORY
potions = {
  "Small Health Potion": 3,
  "Large Health Potion": 0,
  "Strength Potion": 0,
  "Shield Potion": 0
}
#POTION EFFECTS
strength_attacks_left = 0
sheild_potion_hits_left = 0
#WEAPONS INVENOTRY
weapons = {
  "Rusty Sword": 20
}

equipted_weapon = "Rusty Sword"

player_attack = weapons[equipted_weapon]

while True:

    # MAIN MENU
    print("\n===== MONSTER SLAYER =====")
    print("1. Fight Monster")
    print("2. Visit Sword Shop")
    print("3. View Stats")
    print("4. Weapon Inventory")
    print("5. Quit Game")

    choice = input("Choose An Option: ")

    # START OF BATTLE SEQUENCE
    if choice == "1":

        print("\nStarting Monster Battle")
        print("Prepare For Battle!")

        monster_names = ["Skeleton", "Troll", "Spider", "Goblin"]
        monster_name = random.choice(monster_names)

        monster_health = random.randint(30, 80)
        monster_attack = random.randint(5, 15)

        print("\nA Wild", monster_name, "Has Appeared!")

        print("\nMonster Stats:")
        print("Monster Health:", monster_health)
        print("Monster Attack:", monster_attack)

        # BATTLE LOOP
        while player_health > 0 and monster_health > 0:

            print("\nWhat Do You Do?")
            print("1. Attack")
            print("2. Use Healing Potion")
            print("3. Run")

            battle_choice = input("\nChoose An Option: ")

            if battle_choice == "1":

                monster_health -= player_attack

                print("\nYou Attacked The Monster!")
                print("Monster Health:", max(0, monster_health))

            elif battle_choice == "2":

                if potions > 0:

                    player_health = min(player_health + potions_healing, 100)
                    potions -= 1

                    print("\nYou Used A Healing Potion!")
                    print("Your Health:", player_health)
                    print("Potions Remaining:", potions)

                else:
                    print("\nNo Potions Left!")
                    continue

            elif battle_choice == "3":

                print("\nYou Ran Away!")
                break

            else:
                print("\nInvalid Choice!")
                continue

            # MONSTER ATTACK
            if monster_health > 0:

                player_health -= monster_attack

                print("\nThe Monster Has Attacked You!")
                print("Your Health:", max(0, player_health))

        # CHECK BATTLE RESULTS
        if player_health <= 0:

            print("\nYou Have Been Defeated!")
            print("GAME OVER!")
            break

        elif monster_health <= 0:

            print("\nYou Have Slain The Monster!")
            print("You Win!")

            player_xp += xp_reward

            print("\nYou Earned", xp_reward, "XP!")
            print("Total XP:", player_xp)

    
    # SWORD SHOP
    elif choice == "2":

        print("\n===== SWORD SHOP =====")

        print("Your XP:", player_xp)

        print("\n1. Handmade Sword - 25 XP - 30 Damage")
        print("2. Battle Sword - 100 XP - 40 Damage")
        print("3. Knight Sword - 250 XP - 45 Damage")
        print("4. Kings Sword - 500 XP - 60 Damage")
        print("5. Exit Shop")

        shop_choice = input("\nWhat Would You Like To Purchase? ")

        # HANDMADE SWORD
        if shop_choice == "1":

            if player_xp >= 25:

                player_xp -= 25

                weapons["Handmade Sword"] = 30

                print("\nYou Purchased The Handmade Sword!")
                print("Your XP:", player_xp)

            else:
                print("\nYou Do Not Have Enough XP!")

        # BATTLE SWORD
        elif shop_choice == "2":

            if player_xp >= 100:

                player_xp -= 100

                weapons["Battle Sword"] = 40

                print("\nYou Purchased The Battle Sword!")
                print("Your XP:", player_xp)

            else:
                print("\nYou Do Not Have Enough XP!")

        # KNIGHT SWORD
        elif shop_choice == "3":

            if player_xp >= 250:

                player_xp -= 250

                weapons["Knight Sword"] = 45

                print("\nYou Purchased The Knight Sword!")
                print("Your XP:", player_xp)

            else:
                print("\nYou Do Not Have Enough XP!")

        # KINGS SWORD
        elif shop_choice == "4":

            if player_xp >= 500:

                player_xp -= 500

                weapons["Kings Sword"] = 60

                print("\nYou Purchased The Kings Sword!")
                print("Your XP:", player_xp)

            else:
                print("\nYou Do Not Have Enough XP!")

        # EXIT SHOP
        elif shop_choice == "5":

            print("\nLeaving Sword Shop...")

        else:
            print("\nInvalid Shop Choice!")


    # PLAYER STATS
    elif choice == "3":

        print("\nDisplaying Player Stats:")
        print("\nPlayer Name:", player_name)
        print("Player Health:", player_health)
        print("Player Attack:", player_attack)
        print("Player XP:", player_xp)
        print("Healing Potions:", potions)
        print("Current Sword:", equipted_weapon)

    # WEAPON INVENTORY
    elif choice == "4":

      print("\n===== WEAPON INVENTORY =====")

      for weapon, damage in weapons.items():

        print(weapon, "-", damage, "Damage")

    # QUIT GAME
      
    elif choice == "5":

        print("\nThanks For Playing Monster Slayer!")
        break

    else:

        print("\nInvalid Choice!")

print("\nGame Over. Thanks For Playing!")
