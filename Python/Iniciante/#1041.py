entrada = input("").split()
X = float(entrada[0])
Y = float(entrada[1])

# x > 0 and y > 0: Q1 xxxxx
# x < 0 and y > 0: Q2 xxxxx
# x < 0 and y < 0: Q3 xxxxx
# x > 0 and y < 0: Q4 xxxxx
# x == 0 and y == 0: Origim xxxx
# x == 0 and y != 0: Eixo X
# x != 0 and y != 0: Eixo Y

if X == 0 and Y == 0:
    print("Origem")
elif X == 0:
    print("Eixo Y")
elif Y == 0:
    print("Eixo X")
elif X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 and Y < 0:
    print("Q4")
