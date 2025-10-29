"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Steven Thorpe Jr.]
Date: [10/27/2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """"
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold

    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    create_character = input()
    char = create_character

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
    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

    if character_class.lower() = "academic weapon":
        name = "Academic Weapon"
        class = "brainiac"
        level = 1
        strength = 2
        magic == 8
        health == 80
        gold == 80
    elif character_class.lower() == "social butterfly":
        name == "Social Butterfly"
        class == "charmer"
        level == 1
        strength == 5
        magic == 6
        health == 50
        gold == 25
    elif character_class.lower() == "student athlete":
        name == "Student Athlete"
        class == "jock"
        level == 1
        strength == 8
        magic == 3
        health == 100
        gold == 75
    elif character_class.lower() == "hustler":
        name = "Hustler"
        class = "go-getter"
        level = 1
        strength = 6
        magic = 10
        health = 20
        gold = 100

    return name, class, level, strength, magic, health, gold

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
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):
        print("Error: FIle not found.")
        return None
    
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
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
            print(f"Error: Missing key '{key}' in file.")
            return None
    
    return character
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

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
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")

