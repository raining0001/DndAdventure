print("Somewhere up ahead, you hear the sound of battle.")
print("As you reach the fight, three goblins remain standing, and the last guard falls.")

# Initialize goblin HPs using a dictionary
goblin_hp = {
    'goblin_raider1': 6,
    'goblin_raider2': 4,
    'goblin_raider3': 4
}

adventurer = 16
adventurer_attack = 8

first_choice = input("Choose an action: Attack (A), Speak (S), or Run (R): ")

if first_choice == "A":
    for goblin in goblin_hp:
        goblin_hp[goblin] -= adventurer_attack
    print(f"Goblins Hp = {goblin_hp}")    
    print("You have slain all the goblins ! You Won!")
elif first_choice == "S":
    first_choice_speak = input("Choose: Intimidate(I), Flirt(F), or Tell a joke(T): ")
    if first_choice_speak == 'I':
        adventurer -= 1
        print(f"The goblins are laughing at you! You lost 1 HP. Your HP is {adventurer}.")
    elif first_choice_speak == 'F':
        for goblin in goblin_hp:
            goblin_hp[goblin] -= 1
        adventurer -= 3
        print(f"The goblins are blushing due to embarrassment; they each lose 1 HP {goblin_hp}.\nYou also lose 3 HP.")
        print(f"Your HP is {adventurer}.")
    elif first_choice_speak == 'Tell a joke':
        print("You manage to dissipate the tension! You can continue your adventure.")
    else:
        print("Invalid choice! Game Over!")
else:
    print("You chose to run. Game Over!")