import os
import pickle


# Function to save game data to a file
def save_game_data(data):
    save_dir = "save-data"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, "game_data.sav")
    with open(save_path, "wb") as file:
        pickle.dump(data, file)


# Function to load game data from a file
def load_game_data():
    save_path = os.path.join("save-data", "game_data.sav")
    if not os.path.exists(save_path):
        return None
    with open(save_path, "rb") as file:
        return pickle.load(file)


# Function to check if a save file already exists
def check_save_file():
    save_dir = "save-data"
    save_path = os.path.join(save_dir, "game_data.sav")
    if os.path.exists(save_path):
        return True
    return False
