import random
print("Welcome To Monster Slayer\n")
player_name = input("Whats Your Name Knight: ")
player_health = 100
player_attack = 20
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
  print("2. Run")
  print()
  choice = input("Choose An Option: ")
  if choice == "1":
      monster_health = monster_health - player_attack

      print("You Attacked The Monster")
      print("Monster Health:", monster_health)

  elif choice == "2":
      print("You Ran Away")
      break

  else:
        print("Input Invalid, Try Agian.")