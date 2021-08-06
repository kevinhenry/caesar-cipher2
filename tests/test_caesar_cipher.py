import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_encrypt_shift():
    actual = encrypt("Hello world", 7)
    expected = "Olssv dvysk"
    assert actual == expected


def test_decrypt_shift():
    actual = decrypt("Olssv dvysk", 7)
    expected = "Hello world"
    assert actual == expected


def test_encrypt_shift_upper_case():
    actual = encrypt("Hello world", 7)
    expected = "Olssv dvysk"
    assert actual == expected


def test_encrypt_spec_char_and_white_space():
    actual = encrypt("Hello.    World!", 7)
    expected = "Olssv.    Dvysk!"
    assert actual == expected


def test_crack():
    code = encrypt("It was the best of times, it was the worst of times. ", 5)
    actual = crack(code)
    expected = "Ny bfx ymj gjxy tk ynrjx, ny bfx ymj btwxy tk ynrjx. "
    assert actual == expected
