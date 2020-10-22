import re


remove = re.compile(r'\D')

cases = int(input())
for case in range(cases):
    string_ = input()

    a = sum([int(x) for x in re.split(remove, string_) if x != ''])
    print(a)
