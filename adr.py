import random

# Game constants
START_HP = 10
START_MANA = 2
MAX_MANA = 15

# Initialize players
player = {"hp": START_HP, "mana": START_MANA, "name": "You"}
computer = {"hp": START_HP, "mana": START_MANA, "name": "Computer"}

# Action mapping
ACTIONS = {1: "attack", 2: "defend", 3: "recharge"}

def show_status():
    print(f"\n{player['name']} - HP: {player['hp']} | Mana: {player['mana']}")
    print(f"{computer['name']} - HP: {computer['hp']} | Mana: {computer['mana']}\n")

def apply_actions(p_action, c_action):
    global player, computer
    
    # Check for attack validity
    if p_action == "attack" and player["mana"] <= 0:
        print(f"{player['name']} attacked with 0 mana! Automatic disqualification!")
        player["hp"] = 0
        return
    if c_action == "attack" and computer["mana"] <= 0:
        print(f"{computer['name']} attacked with 0 mana! Automatic disqualification!")
        computer["hp"] = 0
        return
    
    # Handle mana cost/gain
    if p_action == "attack":
        player["mana"] -= 1
    if c_action == "attack":
        computer["mana"] -= 1
    if p_action == "recharge":
        player["mana"] = min(player["mana"] + 2, MAX_MANA)
    if c_action == "recharge":
        computer["mana"] = min(computer["mana"] + 2, MAX_MANA)

    # Damage logic
    # Player attacks Computer
    if p_action == "attack":
        if c_action == "attack":
            player["hp"] -= 1
            computer["hp"] -= 1
        elif c_action == "defend":
            computer["hp"] -= 0.5
        elif c_action == "recharge":
            computer["hp"] -= 1

    # Computer attacks Player
    if c_action == "attack":
        if p_action == "defend":
            player["hp"] -= 0.5
        elif p_action == "recharge":
            player["hp"] -= 1

# Main game loop
print("Welcome to Attack–Defend–Recharge!")

show_status()

while True:
    # Player choice with corrected prompt
    try:
        choice = int(input("Choose 1 for Attack, 2 for Defend, 3 for Recharge, 0 to Quit: "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, 3, or 0.")
        continue

    if choice == 0:
        print("Game terminated by user.")
        break
    if choice not in ACTIONS:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue

    player_action = ACTIONS[choice]

    # Computer choice (random, avoids attack if no mana)
    possible_actions = ["attack", "defend", "recharge"]
    if computer["mana"] <= 0:
        possible_actions.remove("attack")
    computer_action = random.choice(possible_actions)

    print(f"You chose: {ACTIONS[choice]} | Computer chose: {computer_action}")

    # Apply actions
    apply_actions(player_action, computer_action)
    show_status()

    # Check for game over
    if player["hp"] <= 0 or computer["hp"] <= 0:
        if player["hp"] <= 0 and computer["hp"] <= 0:
            print("It's a draw!")
        elif player["hp"] <= 0:
            print("Computer wins!")
        else:
            print("You win!")
        break