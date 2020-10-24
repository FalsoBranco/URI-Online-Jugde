
cases = int(input())

for case in range(cases):

    string_ = input()
    meio = int(len(string_) / 2) - 1
    fix_string = string_[meio::-1] + string_[len(string_) - 1:meio:-1]
    print(fix_string)
