import random
def generate_grid() -> list[list[str]]:
    """
    None -> list[list[str]]
    Generates list of lists of letters - i.e. grid for the game.
    Each row contains at least one vowel and at least one consonant.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    result = []
    while True:
        row = []
        vowels = 0
        consonants = 0
        for _ in range(3):
            letter = chr(random.randint(ord('A'), ord('Z')))
            if letter in 'AEIOU':
                vowels += 1
            elif letter in 'BCDFGHJKLMNPQRSTVWXYZ':
                consonants += 1
            row.append(letter)
        if vowels >= 1 and consonants >= 1:
            result.append(row)
            if len(result) == 3:
                return result
def get_pure_user_words(user_words: list[str], allowed_letters: list[str], dictionary_words: list[str]) -> list[str]:
    """
    (list[str], list[str], list[str] -> list[str]
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    result = []
    for word in user_words:
        if len(word) < 4 or not allowed_letters[4] in word or word in result or word in dictionary_words:
            continue
        count = 0
        for letter in word:
            if allowed_letters.count(letter) < word.count(letter):
                count = 1
                break
        if not count:
            result.append(word)
    return result

def get_user_words() -> list[str]:
    """
    None -> list[str]
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    result = []
    while True:
        try:
            result.append(input())
        except EOFError:
            return result

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    (str, list[str] -> list[str])
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r', encoding = 'utf-8') as file:
        result = []
        correct = file.readlines()[3:]
        for word in correct:
            word = word.lower().strip()
            if len(word) < 4 or not letters[4] in word or word in result:
                continue
            check = 0
            for letter in word:
                if letters.count(letter) < word.count(letter):
                    check += 1
                    break
            if not check:
                result.append(word)
        return result


def main():
    '''
    Realises the actual game by utilising all other functions
    '''
    letters = generate_grid()
    print(f'Your board is {letters}\nPlease, suggest your words here:')
    new_letters = []
    for row in letters:
        for letter in row:
            new_letters.append(letter.lower())
    user_words = get_user_words()
    words_from_dict = get_words('sadge.txt', new_letters)
    count = 0
    other_words = []
    for word in words_from_dict:
        if word in user_words:
            count += 1
        else:
            other_words.append(word)
    print(f'Number of the right words: {count}')
    print(f'All possible words:\n {words_from_dict}')
    print(f'You missed the following words:\n {other_words}')
    print(f"You suggest, but we don't have them in the dictionary: \
{get_pure_user_words(user_words, new_letters, words_from_dict)}")