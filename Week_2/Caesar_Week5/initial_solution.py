def caesar_encode(message:str, key:int):
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
    key = key%26
    lst = []
    strin = ""
    for i in message:
        if ord(i) == 32:
            lst.append(ord(i))
        else:
            lst.append(ord(i) + key)
    for index, value in enumerate(lst):
        if value>122:
            lst[index] = value - 26
    for index, value in enumerate(lst):
        lst[index] = chr(value)
        strin = strin + lst[index]
    return strin

def caesar_decode(message:str, key:int):
    """
    Decodes a message using the Caeser code.

    Parameters:
    message(str): A message that has to be decoded.
    key(int): A key used to decode the message.

    Returns:
    str: The decoded message.

    >>> caeser_decode("h knud bzsr", 25)
    i love cats
    >>> caeser_decode("i love cats", 26)
    i love cats
    >>> caeser_decode("j mpwf dbut", 27)
    i love cats
    """
    key = key%26
    lst = []
    strin = ""
    for i in message:
        if ord(i) == 32:
            lst.append(ord(i))
        else:
            lst.append(ord(i) - key)
    for index, value in enumerate(lst):
        if value<97 and value != 32:
            lst[index] = value + 26
    for index, value in enumerate(lst):
        lst[index] = chr(value)
        strin = strin + lst[index]
    return strin
