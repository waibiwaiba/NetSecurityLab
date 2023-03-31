import time
from typing import Union
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from typing import Union, Tuple


def sha512(s: Union[str, bytes], string=True):
    if isinstance(s, str):
        s = s.encode('utf-8')
    digest = hashes.Hash(hashes.SHA512())
    digest.update(s)
    if string:
        return digest.finalize().hex()
    else:
        return digest.finalize()


def sha256(s: Union[str, bytes], string=True):
    if isinstance(s, str):
        s = s.encode('utf-8')
    digest = hashes.Hash(hashes.SHA256())
    digest.update(s)
    if string:
        return digest.finalize().hex()
    else:
        return digest.finalize()


def password_hash(username, password, salt):
    return sha512(sha512(username + password) + salt)


def create_login_request(username: str, password: str, salt: Union[str, bytes] = None) -> dict:
    if not salt:
        salt = os.urandom(16).hex()
    if isinstance(salt, bytes):
        salt = salt.hex()
    assert isinstance(username, str)
    assert isinstance(password, str)
    assert isinstance(salt, str)
    return {
        'user': username,
        'request': password_hash(username, password, salt),
        'code': salt
    }


def validate_user(client_request: dict, userpass_hash: str) -> bool:
    """
    Validate user password.
    :param client_request: the client's raw request json.
    :param userpass_hash: the hash stored in the database.
    :return: if the user is validated.
    """
    salt = client_request.get('code')
    actual = client_request.get('request')
    if not isinstance(salt, str) or len(salt) != 32:
        raise ValidationError('bad salt')
    if not isinstance(actual, str) or len(actual) != 128:
        raise ValidationError(f'bad sha512 request: {actual}')
    expected = sha512(userpass_hash + salt)
    # fixed time comparison
    acc = 0
    for j, k in zip(actual, expected):
        acc += (ord(j) - ord(k)) ** 2
    return not acc


def encrypt(data: bytes, k: Union[str, bytes]) -> Tuple[bytes, bytes]:
    if isinstance(k, str):
        k = k.encode('utf-8')
    if not isinstance(k, bytes):
        raise ValueError(f'bad key type: {type(k)}')
    if isinstance(data, str):
        data = data.encode('utf-8')
    if not isinstance(data, bytes):
        raise ValueError(f'bad data type: {type(data)}')
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(sha256(k, string=False)), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return iv, ciphertext


def decrypt(data: bytes, k: Union[str, bytes], iv: bytes) -> Tuple[bytes, bytes]:
    if isinstance(k, str):
        k = k.encode('utf-8')
    key = hashes.Hash(hashes.SHA256(), backend=default_backend())
    key.update(k)
    key = key.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize(), iv


class ValidationError(Exception):
    pass
