import configparser
import hashlib
import json
import os

from cryptography.fernet import Fernet

from classes.character.character import Character
from core.data import get_initial_characters


def generate_key():
    return Fernet.generate_key()


def encrypt_data(data, key):
    fernet = Fernet(key)
    json_data = json.dumps(data)
    encrypted_data = fernet.encrypt(json_data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    json_data = decrypted_data.decode()
    return json.loads(json_data)


def save_game_data(game_data, filename, key):
    data_dict = game_data.to_dict()
    encrypted_data = encrypt_data(data_dict, key)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def load_game_data(filename, key):
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        data_dict = decrypt_data(encrypted_data, key)
        return GameData.from_dict(data_dict)
    except FileNotFoundError:
        return GameData(characters=get_initial_characters())


def generate_checksum(data):
    return hashlib.sha256(data).hexdigest()


def validate_checksum(data, checksum):
    return generate_checksum(data) == checksum


def generate_and_save_key(config_file):
    key = generate_key()
    config = configparser.ConfigParser()
    config["encryption"] = {"key": key.decode()}

    with open(config_file, "w") as configfile:
        config.write(configfile)

    return key


def load_key_from_config(config_file):
    if not os.path.exists(config_file):
        return generate_and_save_key(config_file)

    config = configparser.ConfigParser()
    config.read(config_file)

    key = config["encryption"]["key"]
    if not key:
        raise ValueError("Encryption key not found in config.ini")

    return key.encode()


class GameData:
    def __init__(self, characters):
        self.characters = characters

    def to_dict(self):
        return {
            "characters": [character.to_dict() for character in self.characters],
        }

    @staticmethod
    def from_dict(data):
        characters = [
            Character.from_dict(char_data) for char_data in data["characters"]
        ]
        return GameData(characters)
