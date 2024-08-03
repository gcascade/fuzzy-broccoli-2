import configparser
import hashlib
import os
from unittest.mock import MagicMock

import pytest

from classes.character.character import Character
from core.data import get_initial_characters
from core.game_data import (
    GameData,
    decrypt_data,
    encrypt_data,
    generate_and_save_key,
    generate_checksum,
    generate_key,
    load_game_data,
    load_key_from_config,
    save_game_data,
    validate_checksum,
)


@pytest.fixture
def game_data():
    characters = get_initial_characters()
    return GameData(characters)


def test_generate_key():
    key = generate_key()
    assert isinstance(key, bytes)
    assert len(key) == 44  # 32 bytes base64 encoded


def test_encrypt_decrypt_data():
    key = generate_key()
    data = {"test": "data"}
    encrypted_data = encrypt_data(data, key)
    decrypted_data = decrypt_data(encrypted_data, key)
    assert decrypted_data == data


def test_save_load_game_data(game_data, tmpdir):
    key = generate_key()
    filename = os.path.join(tmpdir, "test_game_data.dat")

    save_game_data(game_data, filename, key)
    loaded_game_data = load_game_data(filename, key)

    assert isinstance(loaded_game_data, GameData)
    assert len(loaded_game_data.characters) == len(game_data.characters)
    for original, loaded in zip(game_data.characters, loaded_game_data.characters):
        assert original.to_dict() == loaded.to_dict()


def test_load_game_data_file_not_found(monkeypatch):
    key = generate_key()
    filename = "non_existent_file.dat"

    def mock_get_initial_characters():
        return [MagicMock(spec=Character)]

    monkeypatch.setattr("core.data.get_initial_characters", mock_get_initial_characters)
    game_data = load_game_data(filename, key)

    assert isinstance(game_data, GameData)
    assert len(game_data.characters) == 4
    assert isinstance(game_data.characters[0], Character)


def test_generate_checksum():
    data = b"test data"
    checksum = generate_checksum(data)
    assert hashlib.sha256(data).hexdigest() == checksum


def test_validate_checksum():
    data = b"test data"
    checksum = generate_checksum(data)
    assert validate_checksum(data, checksum)
    assert not validate_checksum(data, "invalid_checksum")


def test_generate_and_save_key(tmpdir):
    config_file = os.path.join(tmpdir, "config.ini")
    key = generate_and_save_key(config_file)

    config = configparser.ConfigParser()
    config.read(config_file)
    loaded_key = config["encryption"]["key"]

    assert key.decode() == loaded_key


def test_load_key_from_config(tmpdir):
    config_file = os.path.join(tmpdir, "config.ini")
    original_key = generate_and_save_key(config_file)

    key = load_key_from_config(config_file)
    assert key == original_key


def test_load_key_from_config_file_not_found(tmpdir):
    config_file = os.path.join(tmpdir, "config.ini")

    key = load_key_from_config(config_file)
    assert os.path.exists(config_file)
    assert key is not None


def test_load_key_from_config_no_key_in_file(tmpdir):
    config_file = os.path.join(tmpdir, "config.ini")

    config = configparser.ConfigParser()
    config["encryption"] = {}
    with open(config_file, "w") as f:
        config.write(f)

    with pytest.raises(KeyError):
        load_key_from_config(config_file)
