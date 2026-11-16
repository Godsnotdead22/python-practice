# New Python file

import random

print("Welcome To Monster Slayer\n")

player_name = input("Whats Your Name Knight: ")
player_health = 100
player_attack = 20
potions = 3
potions_healing = 25
player_xp = 0
xp_reward = 25

while True:

    # MAIN MENU
    print("\n===== MONSTER SLAYER =====")
    print("1. Fight Monster")
    print("2. Visit Sword Shop")
    print("3. View Stats")
    print("4. Quit Game")

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

        print("\nWelcome To The Sword Shop!")
        print("More Shop Features Coming Soon!")

    # PLAYER STATS
    elif choice == "3":

        print("\nDisplaying Player Stats:")
        print("\nPlayer Name:", player_name)
        print("Player Health:", player_health)
        print("Player Attack:", player_attack)
        print("Player XP:", player_xp)
        print("Healing Potions:", potions)

    # QUIT GAME
    elif choice == "4":

        print("\nThanks For Playing Monster Slayer!")
        break

    else:

        print("\nInvalid Choice!")

print("\nGame Over. Thanks For Playing!")
