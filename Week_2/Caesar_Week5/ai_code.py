def caesar_encode(message: str, key: int) -> str:
    """
    Encodes a message using the Caesar code.

    Parameters:
    message(str): A message that has to be encoded.
    key(int): A key used to encode the message.

    Returns:
    str: The encoded message.

    >>> caesar_encode("i love cats", 25)
    "h knud bzsr"
    >>> caesar_encode("i love cats", 26)
    "i love cats"
    >>> caesar_encode("i love cats", 27)
    "j mpwf dbut"
    """
    if not isinstance(message, str) or not isinstance(key, int):
        return None

    key = key % 26
    result = []

    for char in message:
        if char == " ":
            result.append(char)
        else:
            encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
            result.append(encrypted_char)

    return "".join(result)

def caesar_decode(message: str, key: int) -> str:
    """
    Decodes a message using the Caesar code.

    Parameters:
    message(str): A message that has to be decoded.
    key(int): A key used to decode the message.

    Returns:
    str: The decoded message.

    >>> caesar_decode("h knud bzsr", 25)
    i love cats
    >>> caesar_decode("i love cats", 26)
    i love cats
    >>> caesar_decode("j mpwf dbut", 27)
    i love cats
    """
    key = key % 26
    lst = [chr((ord(i) - key - 97) % 26 + 97) if ord(i) in range(97, 123) else i for i in message]
    return "".join(lst)
