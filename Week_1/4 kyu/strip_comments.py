def strip_comments_generated(input_string, comment_markers):
    """
    Strips all text that follows any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.

    :param input_string: str, the input string to strip comments from
    :param comment_markers: list, a list of comment markers
    :return: str, the input string with comments stripped
    """

    lines = input_string.split('\n')
    stripped_lines = []

    for line in lines:
        for marker in comment_markers:
            if marker in line:
                line = line[:line.index(marker)].rstrip()
                break
        stripped_lines.append(line)

    return '\n'.join(stripped_lines)

"""
В цілому більшість тестів проходить, але не всі, тому що в даному випадку важливо врахувати, що коментарі можуть бути
всередині рядка, а не тільки на початку. Я виправив цю проблему, але, хоча всі тести проходить,
код став зовсім не похожий на згенерований спочатку. Також хотів підправити його в його чаті, але він тупив і видавав
попередні відповіді, не міняв нічого або взагалі робив ще гірше. Не знаю, як він себе показав на легших задачках, але на цій,
яка була не важка технічно і я вважав що бот зможе просто застріпити коменти (для цього не треба мати багато логіки), він не справився до кінця.
"""


def strip_comments_remarkered(string, markers):

    res = ""
    s = string.split('\n')

    for i in s:
        position = -1

        for j in range(len(i)):
            if i[j] in markers:
                position = j
                break

        if position != -1:
            i = i[0:position]

        res += i.rstrip() + "\n"

    return res[0:-1]