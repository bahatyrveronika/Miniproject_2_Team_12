'''aliens'''
def read_file(file_path):
    '''
    Returns dictionary of persos and its iq.
    >>> read_file('smart_people.txt')
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, \
'Marilyn vos Savant': 186, 'Judith Polgar': 170, 'Quentin Tarantino': \
163, 'Bill Gates': 160, "Conan O'Brien": 160, 'Emma Watson': 132, \
'Barack Obama': 137}
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        content=file.read()[60:]
    lines=content.split('\n')
    names=[]
    iq=[]
    name=""
    tsifra=""
    for el in lines:
        name=""
        tsifra=""
        for l in el:
            if l.isalpha() or l=="'" or l==" ":
                name+=l
            if l.isdigit():
                tsifra+=l
        names.append(name)
        iq.append(int(tsifra))
    dictor=dict(zip(names, iq))
    return dictor

def rescue_people(smarties, limit_iq):
    '''
    Returns tuple of amount of travels and variants of possible travels.
    >>> rescue_people({'Elon Musk': 165, 'Mark Zuckerberg': 152, \
'Will Smith': 157, 'Marilyn vos Savant': 186, 'Judith Polgar': 170, \
'Quentin Tarantino': 163, 'Bill Gates': 160, "Conan O'Brien": 160, \
'Emma Watson': 132, 'Barack Obama': 137}, 500)
    (4, [['Marilyn vos Savant', 'Judith Polgar', 'Barack Obama'], ['Elon Musk', \
'Quentin Tarantino', 'Bill Gates'], ["Conan O'Brien", 'Will Smith', \
'Mark Zuckerberg'], ['Emma Watson']])
    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160, "Sir Isaac Newton": \
195, "Nikola Tesla": 189}, 500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    '''
    if len(smarties)==0:
        return (0,[])
    keep_keys=set()
    for item in smarties.items():
        if int(item[1])>130:
            keep_keys.add(item[0])
    dictor = {key: smarties[key] for key in keep_keys}
    sorted_dict = dict(sorted(dictor.items(), key=lambda item: (-item[1], item[0])))
    big_list=[]
    listok=[]
    a=limit_iq
    setik=set()
    while len(setik)<len(smarties):
        for item, value in sorted_dict.items():
            if a<value:
                for i, v in sorted_dict.items():
                    if i not in setik and v<=a:
                        a-=v
                        setik.add(i)
                        listok.append(i)
                big_list.append(listok)
                listok=[]
                a=limit_iq
            if a>=value and item not in setik:
                listok.append(item)
                setik.add(item)
                a-=value
    if len(listok)>0:
        big_list.append(listok)
    return (len(big_list), big_list)