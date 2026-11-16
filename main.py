import random
print("Welcome To Monster Slayer\n")
player_name = input("Whats Your Name Knight: ")
player_health = 100
player_attack = 20
potions = 3
potions_healing = 25
player_xp = 0
xp_reward = 25
print()
print("=====MONSTER SLAYER=====")
print("Welcom", player_name)
print()
print("Your Stats:")
print("Player Health:", player_health)
print("Player Attack:", player_attack)
print()
print("Prepare For Battle!")
monster_names = ["Skeleton", "Troll", "Spider", "Goblin"]
monster_names = random.choice(monster_names)
monster_health = random.randint(30, 80)
monster_attack = random.randint(5, 15)
print("A Wild", monster_names, "Has Appeared")
print()
print("Monster Stats:")
print("Monster Health:", monster_health)
print("Monster Attack:", monster_attack)
while player_health > 0:
  if monster_health <= 0:
    print("\nYou Defeated The Monster")
    print("You Win!")
    break
  print("\nWhat Do You Do?")
  print("1. Attack")
  print("2. Use Healing Potion")
  print("3. Run")
  print()
  choice = input("Choose An Option: ")
  if choice == "1":
      monster_health = monster_health - player_attack

      print("You Attacked The Monster")
      print("Monster Health:", monster_health)
    
  if monster_health > 0:
    
      player_health = player_health - monster_attack
    
      print("The Monster Has Attacked You")
      print("Your Health:", player_health)

  if monster_health <= 0:

    print()
    print("You Have Slayn The Monster!")
    player_xp = player_xp + xp_reward
    print("\nYou Earned", xp_reward, "XP!")
    print("Total XP:", player_xp)
    break

  elif choice == "2":

    if potions > 0:
      player_health = min(player_attack + potions_healing, 100)
      potions = potions - 1
      print("You Used A Healing Potion!")
      print("Your Health:", player_health)
      print("Potions Remaining:", potions)
    else:
      print("No Potions Left")

  elif choice == "3":
    print("You Ran Away")
    break

  else:
        print()