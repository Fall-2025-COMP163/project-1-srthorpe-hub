"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Steven Thorpe Jr.]
Date: [10/27/2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold

    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1,
    #                 "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    level = 1  # All new characters start at level 1
    strength, magic, health = calculate_stats(character_class, level)  # Get stats from helper function
    gold = 100  # Starting gold

    char = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return char

    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Academic Weapon: High magic, medium health, low strength
    - Social Butterfly: Balanced stats
    - Student Athlete: High strength, high health, low magic
    - Hustler: High magic, low health, high gold potential
    """
    character_class = character_class.lower()

    if character_class == "academic weapon":
        strength = 2 + (level * 1)
        magic = 8 + (level * 3)
        health = 80 + (level * 5)

    elif character_class == "social butterfly":
        strength = 5 + (level * 2)
        magic = 6 + (level * 2)
        health = 50 + (level * 4)

    elif character_class == "student athlete":
        strength = 8 + (level * 3)
        magic = 3 + (level * 1)
        health = 100 + (level * 6)

    elif character_class == "hustler":
        strength = 6 + (level * 2)
        magic = 10 + (level * 3)
        health = 20 + (level * 3)

    else:
        # Default (balanced)
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 60 + (level * 4)

    return strength, magic, health


import os

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"] 
    for key in required_keys:
        if key not in character:
            print(f"Error: Missing key '{key}' in character data.")
            return False
    
    if filename == "" or filename.isspace():
        print("Error: Invalid filename.")
        return False
    
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True

    # TODO: Implement this function
    # Remember to handle file errors gracefully
    

import os

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):
        print("Error: File not found.")
        return None

    # Read file contents
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        if ": " not in line:
            continue  # skip malformed lines

        key, value = line.strip().split(": ", 1)
        key = key.lower().replace("character name", "name")

        # Convert numeric fields to integers
        if key in ["level", "strength", "magic", "health", "gold"]:
            value = int(value)

        character[key] = value

    # Verify all required fields exist
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required_keys:
        if key not in character:
            print(f"Error: Missing key '{key}' in file.")
            return None

    return character


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
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


def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # Increase level by 1
    character["level"] += 1

    # Recalculate stats using the existing function
    strength, magic, health = calculate_stats(character["class"], character["level"])

    # Update the dictionary
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

    print(f"\n {character['name']} leveled up to level {character['level']}! ")


