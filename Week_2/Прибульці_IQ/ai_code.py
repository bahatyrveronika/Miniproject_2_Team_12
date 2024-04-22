def read_file(file_path):
    '''
    Returns dictionary of persos and its iq.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()[60:].strip()
    lines = content.split('\n')
    return {line.split()[0]: int(line.split()[1]) for line in lines}

def rescue_people(smarties, limit_iq):
    '''
    Returns tuple of amount of travels and variants of possible travels.
    '''
    if not smarties:
        return (0, [])

    def is_qualified(person):
        return smarties[person] > 130

    qualified_smarties = [person for person in smarties if is_qualified(person)]
    qualified_smarties.sort(key=lambda x: (-smarties[x], x))

    current_list = []
    current_iq = 0
    big_list = []

    for person in qualified_smarties:
        if current_iq + smarties[person] <= limit_iq:
            current_list.append(person)
            current_iq += smarties[person]
        else:
            big_list.append(current_list)
            current_list = [person]
            current_iq = smarties[person]

    if current_list:
        big_list.append(current_list)

    return (len(big_list), big_list)