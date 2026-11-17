# New Python file

import random

print("================================")
print("       MONSTER SLAYER")
print("================================\n")

player_name = input("What's Your Name Knight? ")

# PLAYER STATS
player_health = 100
player_max_health = 100
player_xp = 0
xp_reward = 25

# POTION INVENTORY
potions = {
    "Small Health Potion": 3,
    "Large Health Potion": 0,
    "Strength Potion": 0,
    "Shield Potion": 0
}

# POTION EFFECTS
strength_attacks_left = 0
shield_potion_hits_left = 0

# WEAPON INVENTORY
weapons = {
    "Rusty Sword": 20
}

equipped_weapon = "Rusty Sword"
player_attack = weapons[equipped_weapon]

# MONSTERS
monster_names = ["Skeleton", "Troll", "Spider", "Goblin"]

# GAME LOOP
while True:

    # MAIN MENU
    print("\n========== MONSTER SLAYER ==========")
    print("1. Fight Monster")
    print("2. Visit Sword Shop")
    print("3. View Stats")
    print("4. Weapon Inventory")
    print("5. Quit Game")

    choice = input("\nChoose An Option: ")

    # =================================
    # BATTLE
    # =================================

    if choice == "1":

        monster_name = random.choice(monster_names)
        monster_health = random.randint(30, 80)
        monster_max_health = monster_health
        monster_attack = random.randint(5, 15)

        print("\nA Wild", monster_name, "Has Appeared!")
        print("Monster Health:", monster_health)
        print("Monster Attack:", monster_attack)

        escaped = False

        # BATTLE LOOP
        while player_health > 0 and monster_health > 0:

            print("\n========== BATTLE ==========")
            print("Your Health:", player_health)
            print("Monster Health:", monster_health)
            print("Your Weapon:", equipped_weapon)
            print("Your Attack:", player_attack)

            print("\n1. Attack")
            print("2. Use Potion")
            print("3. Run")

            battle_choice = input("\nChoose An Option: ")

            turn_used = False

            # PLAYER ATTACK
            if battle_choice == "1":

                damage = player_attack

                if strength_attacks_left > 0:

                    damage *= 2
                    strength_attacks_left -= 1

                    print("\nStrength Potion Increased Your Damage!")

                monster_health -= damage

                print("\nYou Attacked The", monster_name)
                print("Damage:", damage)
                print("Monster Health:", max(0, monster_health))

                turn_used = True

            # POTION MENU
            elif battle_choice == "2":

                print("\n========== YOUR POTIONS ==========")

                for potion, amount in potions.items():
                    print(potion, "-", amount)

                potion_choice = input("\nWhich Potion Would You Like To Use? ")

                if potion_choice not in potions:

                    print("\nInvalid Potion!")
                    continue

                if potions[potion_choice] <= 0:

                    print("\nYou Don't Have Any Of Those Potions!")
                    continue

                # SMALL HEALTH POTION
                if potion_choice == "Small Health Potion":

                    if player_health == player_max_health:
                        print("\nYour Health Is Already Full!")
                        continue

                    potions[potion_choice] -= 1

                    player_health = min(
                        player_health + 25,
                        player_max_health
                    )

                    print("\nYou Restored 25 Health!")
                    print("Your Health:", player_health)

                # LARGE HEALTH POTION
                elif potion_choice == "Large Health Potion":

                    if player_health == player_max_health:
                        print("\nYour Health Is Already Full!")
                        continue

                    potions[potion_choice] -= 1

                    player_health = min(
                        player_health + 50,
                        player_max_health
                    )

                    print("\nYou Restored 50 Health!")
                    print("Your Health:", player_health)

                # STRENGTH POTION
                elif potion_choice == "Strength Potion":

                    potions[potion_choice] -= 1
                    strength_attacks_left = 3

                    print("\nYour Next 3 Attacks Deal DOUBLE DAMAGE!")

                # SHIELD POTION
                elif potion_choice == "Shield Potion":

                    potions[potion_choice] -= 1
                    shield_potion_hits_left = 3

                    print("\nYour Next 3 Hits Will Be Blocked!")

                turn_used = True

            # RUN AWAY
            elif battle_choice == "3":

                print("\nYou Ran Away!")
                escaped = True
                break

            else:

                print("\nInvalid Choice!")
                continue

            # MONSTER ATTACK
            if monster_health > 0 and turn_used:

                if shield_potion_hits_left > 0:

                    shield_potion_hits_left -= 1

                    print("\nYour Shield Blocked The Attack!")
                    print("Shield Blocks Remaining:", shield_potion_hits_left)

                else:

                    player_health -= monster_attack
                    player_health = max(0, player_health)

                    print("\nThe", monster_name, "Attacked You!")
                    print("Damage Taken:", monster_attack)
                    print("Your Health:", player_health)

        # BATTLE RESULTS
        if player_health <= 0:

            print("\nYou Have Been Defeated!")
            print("GAME OVER!")
            break

        elif monster_health <= 0:

            print("\nYou Have Slain The", monster_name, "!")
            print("YOU WIN!")

            player_xp += xp_reward

            print("\nYou Earned", xp_reward, "XP!")
            print("Total XP:", player_xp)

        elif escaped:

            print("\nYou Escaped Safely!")

    # =================================
    # SWORD SHOP
    # =================================

    elif choice == "2":

        print("\n========== SWORD SHOP ==========")
        print("Your XP:", player_xp)

        shop_weapons = {
            "1": ("Handmade Sword", 30, 25),
            "2": ("Battle Sword", 40, 100),
            "3": ("Knight Sword", 45, 250),
            "4": ("Kings Sword", 60, 500)
        }

        print("\n1. Handmade Sword - 25 XP - 30 Damage")
        print("2. Battle Sword - 100 XP - 40 Damage")
        print("3. Knight Sword - 250 XP - 45 Damage")
        print("4. Kings Sword - 500 XP - 60 Damage")
        print("5. Exit Shop")

        shop_choice = input("\nWhat Would You Like To Purchase? ")

        if shop_choice in shop_weapons:

            weapon_name, damage, cost = shop_weapons[shop_choice]

            if weapon_name in weapons:

                print("\nYou Already Own This Sword!")

            elif player_xp >= cost:

                player_xp -= cost
                weapons[weapon_name] = damage

                print("\nYou Purchased The", weapon_name, "!")
                print("Remaining XP:", player_xp)

            else:

                print("\nYou Do Not Have Enough XP!")

        elif shop_choice == "5":

            print("\nLeaving Sword Shop...")

        else:

            print("\nInvalid Shop Choice!")

    # =================================
    # PLAYER STATS
    # =================================

    elif choice == "3":

        print("\n========== PLAYER STATS ==========")

        print("Player Name:", player_name)
        print("Player Health:", player_health)
        print("Player Attack:", player_attack)
        print("Player XP:", player_xp)
        print("Current Sword:", equipped_weapon)

        print("\n========== POTIONS ==========")

        for potion, amount in potions.items():
            print(potion, "-", amount)

        print("\nStrength Attacks Remaining:", strength_attacks_left)
        print("Shield Blocks Remaining:", shield_potion_hits_left)

    # =================================
    # WEAPON INVENTORY
    # =================================

    elif choice == "4":

        print("\n========== WEAPON INVENTORY ==========")

        weapon_list = list(weapons.items())

        for index, (weapon, damage) in enumerate(weapon_list, 1):

            equipped_text = ""

            if weapon == equipped_weapon:
                equipped_text = " (EQUIPPED)"

            print(
                str(index) + ".",
                weapon,
                "-",
                damage,
                "Damage" + equipped_text
            )

        print("\n0. Exit Inventory")

        weapon_choice = input("\nWhich Weapon Would You Like To Equip? ")

        if weapon_choice.isdigit():

            weapon_index = int(weapon_choice)

            if weapon_index == 0:
                print("\nLeaving Inventory...")

            elif 1 <= weapon_index <= len(weapon_list):

                equipped_weapon = weapon_list[weapon_index - 1][0]
                player_attack = weapons[equipped_weapon]

                print("\nYou Equipped The", equipped_weapon, "!")
                print("Your Attack Damage:", player_attack)

            else:

                print("\nInvalid Weapon Choice!")

        else:

            print("\nInvalid Weapon Choice!")

    # =================================
    # QUIT GAME
    # =================================

    elif choice == "5":

        print("\nThanks For Playing Monster Slayer!")
        break

    else:

        print("\nInvalid Choice!")

print("\nGame Over. Thanks For Playing!")
