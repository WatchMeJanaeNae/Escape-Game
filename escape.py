import random
# House map
#             |----------|-----------|
# (unlock w/  |          | (unlock w/| 
#     Key 2)  |          |   Key 1)  | 
#    Backyard | Bedroom  X Bathroom  | 
#             |          |   *Key 2* |
#   |----X----|---    ---|-----------|
#   |         |          |           |
#   | Kitchen   Hallway     Living     Driveway (opens w/sister's permission)
#   |         |   *Key 1*|    Room   |
#   |---------|----------|-----------|

rooms = {
    "Bedroom": {"pathways": {"d": "Bathroom", "s": "Hallway"}, "open_with": ""},
    "Hallway": {"pathways": {"w": "Bedroom", "a": "Kitchen", "d": "Living Room"}, "open_with": ""},
    "Bathroom": {"pathways": {"a": "Bedroom"}, "open_with": "Key 1"},
    "Kitchen": {"pathways": {"d": "Hallway", "w": "Backyard"}, "open_with": ""},
    "Backyard": {"pathways": {"s": "Kitchen"}, "open_with": "Key 2"},
    "Living Room": {"pathways": {"a": "Hallway", "d": "Driveway"}, "open_with": "Correct"}
}

pickable_objects = {
    "Key 1": {"location": "Hallway", "picked": False},
    "Key 2": {"location": "Bathroom", "picked": False}
}

START_LOCATION = "Bedroom"

def print_location(location: str) -> None:
    """
    Print the description of the current location.
    
    Update this function to check whether the room exists in the rooms dictionary.
    
    If the room exists, print the current location (e.g., "You are in the Kitchen.")
    
    Otherwise, print "Unknown location."
    """
    if location == 'Bedroom':
        if 'Bedroom' in rooms.keys():
            print(f'You are in the Bedroom.')
    elif location == 'Hallway':
        if 'Hallway' in rooms.keys():
            print(f'You are in the Hallway.')
    elif location == 'Bathroom':
        if 'Bathroom' in rooms.keys():
            print(f'You are in the Bathroom.')
    elif location == 'Kitchen':
        if 'Kitchen' in rooms.keys():
            print(f'You are in the Kitchen.')
    elif location == 'Living Room':
        if 'Living Room' in rooms.keys():
            print(f'You are in the Living Room.')
    else:
        print('Unknown location.')   
        
def get_directions(location: str) -> dict[str, str]:
    """
    Return possible directions to move from the current location.
    
    Update this function to read the pathways from the dictionary and return
    the pathways dictionary without printing.
    
    Example return value: {'d': 'Hallway', 'w': 'Outside'}
    
    If the room is unknown, return an empty dict: {}
    """
    if location == 'Bedroom':
        return rooms['Bedroom']['pathways']
    elif location == 'Hallway':
        return rooms['Hallway']['pathways']
    elif location == 'Bathroom':
        return rooms['Bathroom']['pathways']
    elif location == 'Kitchen':
        return rooms['Kitchen']['pathways']
    elif location == 'Living Room':
        return rooms['Living Room']['pathways']

    return {}


def find_room_by_direction(location: str, direction: str) -> str:
    """
    Determine the new location based on the current location and direction.
    
    Modify this function to search the dictionary for the next room to navigate to based
    on the current location and direction provided.
    
    Return the new location after moving in the specified direction.
    
    If the current location is unknown, print "Unknown location." and return the
    original location. If the direction is invalid, print an error message and
    return the current location.
    """
    if location not in rooms:
        print('Unknown location.')
        return location

    paths = rooms[location]['pathways']

    if direction in paths:
        return paths[direction]

    print('Invalid direction. Try again.')
    return location
    

    

def has_key_for_room(room_id: str) -> bool:
    """
    Check if the player has the key to enter a specified room.
    
    Modify this function to consult the rooms and pickable_objects dictionaries to
    determine whether the destination room requires a key and if that key has been picked.
    
    Return True if the player can enter the room, False otherwise.
    """

    if room_id == 'Bathroom':
        if pickable_objects['Key 1']['picked'] is False:
            return False
        elif pickable_objects['Key 1']['picked'] is True:
            return True
    elif room_id == 'Backyard':
        if pickable_objects['Key 2']['picked'] is False:
            return False
        elif pickable_objects['Key 2']['picked'] is True:
            return True
    elif room_id == 'Unknown':
        return False
    else:
        return True

def mom_there() -> bool:
    mom_chance = random.randint(1,20)
    mom_present = (2, 5, 6, 8, 9, 10, 13, 18, 19)

    if mom_chance in mom_present:
         return True
    else:
        return False
    

mom_in_room = mom_there()
    
def explore_room(location: str) -> None:
    """
    Handle picking up objects in the current room.

    This function checks the current room against the `pickable_objects`
    dictionary. If an unpicked object is located in the room, it marks that
    object as picked and prints the corresponding "You found <Key>." message.
    
    If there is no matching object, or it was already picked up, the function
    should do nothing.
    
    Modify this function to search the pickable_objects dictionary. When the player
    enters a room containing an unpicked key, update the `picked` flag to True and
    print the message indicating the key was found. This should work through the
    dictionary data rather than hardcoded room checks.
    """
    if location == 'Hallway':
        if pickable_objects['Key 1']['picked'] is False:
            pickable_objects['Key 1']['picked'] = True
            print('You found Key 1.')
            if pickable_objects['Key 1']['picked'] is True:
               return None
    if location == 'Bathroom':
        if pickable_objects['Key 2']['picked'] is False:
            pickable_objects['Key 2']['picked'] = True
            print('You found Key 2.')
            if pickable_objects['Key 2']['picked'] is True:
                return None
    

def game_loop(location: str) -> None:
    """
    Main game loop handling room navigation.
    Parameters:
    location (str): The starting location of the player.
    The function continuously prints the current location, retrieves possible directions,
    and prompts the player to choose a direction to move. The loop continues until the 
    player decides to exit by entering 'x'. The location is updated based on the player's 
    chosen direction.
    The function relies on the following helper functions:
    - print_location(location): Prints the current location.
    - get_directions(location): Retrieves possible directions from the current location (no printing).
    - The game loop is responsible for printing: "You can go: {<pathways dict>}" using the value returned by get_directions.
    - find_room_by_direction(location, chosen_direction): Finds the next room based on the current location and chosen direction.
    When the player exits, a message "Exited the game." is printed.
    """

    while True:    
        print_location(location)
        explore_room(location)
        available_directions = get_directions(location)
        print(f"You can go: {available_directions}")
        chosen_direction = input("Where do you want to go? ('x' to exit) ").lower()
        if chosen_direction  == 'x':
            print("Exited the game.")
            break
        
        next_room = find_room_by_direction(location, chosen_direction)

        if next_room == 'Living Room' and mom_in_room:
            print("You can't go in. Your mom's in there!")
            continue
        if has_key_for_room(next_room):
            location = next_room
        else:
            print("You don't have the key to enter this room.")
        
        if location == "Backyard":
            print("You have escaped!")
            break

        if location == "Driveway":
            print("You have escaped!")
            break


def start_game() -> None:
    """
    Start the game.

    This function initializes the Escape Game by printing the game title to the console.
    It serves as the entry point for the game.
    """

    print("Escape the House")
    print()
    print("You're grounded, but you wanna go play GTA VI at your friend's house.\nEscape, or miss out on the game you've been waiting YEARS to play.")
    print()

if __name__ == "__main__":
    start_game()
    game_loop(START_LOCATION)