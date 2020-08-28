# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

x = 1
y = 1
s = 0
while x < 40:
    s += x/y
    x += 2
    y *= 2
print("{:.2f}".format(s))
