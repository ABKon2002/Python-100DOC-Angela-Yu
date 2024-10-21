tup = (0, 1, 2)
tup = list(tup)
tup[2] = (tup[2] + 314) % 255
print(tuple(tup))
print(314 - 255)