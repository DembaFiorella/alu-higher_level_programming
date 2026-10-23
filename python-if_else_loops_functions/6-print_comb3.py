#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if i != 8:
            print("{}{}".format(i, j), end=", ")
        elif j != 9:
            print("{}{}".format(i, j), end=", ")
print("{}{}".format(8, 9))
