def pyramid_pattern(n):
    for i in range(n, 0, -1):
        # prints leading spaces 
        for j in range(n - i):
            print('  ', end="")

        # prints stars 
        for k in range(2 * i - 1,): 
            print("* ", end="")
        print("\r")

rows = int(input("Enter number of rows:"))
pyramid_pattern(rows)

print("\n=============== Shortcut Method ================\n")

for i in range (rows, 0, -1):
    print("  " * (rows - i) + "* " * (2 * i - 1), end="")
    print("\r")