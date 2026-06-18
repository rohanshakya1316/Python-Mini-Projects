size = 5
mid = size // 2

for i in range(size):
    for j in range(size):
        if i == mid or j == mid:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
