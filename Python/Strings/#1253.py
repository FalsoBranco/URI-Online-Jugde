

cases = int(input())
for case in range(cases):
    letters = input().upper()
    jumps = int(input())
    new_string = ""

    for letter in letters:
        ascii_ = ord(letter) - jumps
        if ascii_ < 65:
            new_string += chr(91 - (65 - ascii_))
        else:

            new_string += chr(ord(letter) - jumps)
    print(new_string)
