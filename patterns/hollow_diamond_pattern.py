def print_hollow_diamond(n):
    # Upper half of the diamond
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print the hollow star boundary
        for k in range(1, 2 * i):
            if k == 1 or k == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print the hollow star boundary
        for k in range(1, 2 * i):
            if k == 1 or k == (2 * i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Test the pattern with 5 levels
print_hollow_diamond(5)
