from typing import Optional, Iterable
import random
import string


def generate_password(chars: int, punctuation: str, invalid_chars: Optional[Iterable[str]] = None) -> str:
    """Generates a random password.

    Args:
        chars (int): The number of characters
        punctuation (str): Characters used for punctuation.
        invalid_chars (Optional[Iterable[str]], optional): Invalid characters to be excluded from password. Defaults to None.

    Returns:
        str: Random password.
    """

   
    valid_chars = string.ascii_letters + string.digits

    #Add punctuation to valid characterset 
    if punctuation:
        valid_chars += string.punctuation

    # Remove invalid characters from characterset
    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    # Get a random set chars number of characters from valid_chars
    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
