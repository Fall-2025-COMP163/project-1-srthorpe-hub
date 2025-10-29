"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Steven Thorpe Jr.
Date: 10/27/2025

AI Usage:
AI helped with debugging and refining file I/O logic, character stat calculations,
and ensuring full functionality for level-up and save/load features.
"""

import os

# --------------------------
# CHARACTER CREATION
# --------------------------
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns a dictionary with keys: name, class, level, strength, magic, health, gold.
    """
    level = 1
    gold = 100

    if character_class.lower() == "academic weapon":
        strength = 30
        magic = 80
        health = 40
    elif character_class.lower() == "social butterfly":
        strength = 50
        magic = 40
        health = 90
    elif character_class.lower() == "student athlete":
        strength = 80
        magic = 20
        health = 80
    elif character_class.lower() == "hustler":
        strength = 60
        magic = 70
        health = 60
    else:
        strength = 50
        magic = 50
        health = 60

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
}
# --------------------------
# STAT CALCULATION
# --------------------------
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)
    """
    character_class = character_class.lower()
    if character_class == "academic weapon":
        strength = 2 + level
        magic = 8 + level * 3
        health = 80 + level * 5
    elif character_class == "social butterfly":
        strength = 5 + level * 2
        magic = 6 + level * 2
        health = 50 + level * 4
    elif character_class == "student athlete":
        strength = 8 + level * 3
        magic = 3 + level
        health = 100 + level * 6
    elif character_class == "hustler":
        strength = 6 + level * 2
        magic = 10 + level * 3
        health = 20 + level * 3
    else:
        # Default (balanced)
        strength = 5 + level * 2
        magic = 5 + level * 2
        health = 60 + level * 4
    return strength, magic, health

# --------------------------
# SAVE CHARACTER
# --------------------------
def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns True if successful, False if error occurred.
    """
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            return False
    if not filename or filename.isspace():
        return False

    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True

# --------------------------
# LOAD CHARACTER
# --------------------------
def load_character(filename):
    """
    Loads character from text file.
    Returns character dictionary if successful, None if file not found or invalid.
    """
    if not os.path.exists(filename):
        return None

    character = {}
    with open(filename, "r") as file:
        for line in file:
            if ": " not in line:
                continue
            key, value = line.strip().split(": ", 1)
            key = key.lower().replace("character name", "name")
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            character[key] = value

    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            return None

    return character

# --------------------------
# DISPLAY CHARACTER
# --------------------------
def display_character(character):
    """
    Prints formatted character sheet.
    """
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("========================\n")

# --------------------------
# LEVEL UP
# --------------------------
def level_up(character):
    """
    Increases character level by 1 and recalculates stats.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

# --------------------------
# MAIN PROGRAM (for manual testing)
# --------------------------
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===\n")
    char_name = input("Enter your character's name: ").strip()
    print("Choose a class: Academic Weapon, Social Butterfly, Student Athlete, Hustler")
    char_class = input("Enter your character's class: ").strip()

    char = create_character(char_name, char_class)
    display_character(char)

    # Level up example
    level_up(char)
    display_character(char)

    # Save and load example
    filename = f"{char_name}_character.txt"
    save_character(char, filename)
    loaded_char = load_character(filename)
    if loaded_char:
        display_character(loaded_char)
