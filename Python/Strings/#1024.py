from string import ascii_letters


def solution(string_):
    cript = first(string_)
    inverted = second(cript)
    return thirty(inverted)


def first(string_: str):
    code = []
    for letter in string_:
        if letter not in ascii_letters:
            code.append(letter)
            continue

        code.append(chr(ord(letter) + 3))
    return ''.join(code)


def second(cript_string: str):
    return cript_string[::-1]


def thirty(string_: str):
    middle = len(string_) // 2
    code = [chr(ord(letter) - 1) for letter in string_[middle:]]
    new = string_[:middle]
    return new + ''.join(code)


cases = int(input())
for case in range(cases):
    string_ = input()
    print(solution(string_))
