def diamond_pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(" ", end="")
        k = k - 1
        for j in range(0, i):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(" ", end="")
        k = k + 1
        for j in range(0, i):
            print("* ", end="")
        print("\r")

diamond_pattern(6)

print("\n================ SHORTCUT METHOD =================\n")

def print_diamond(n):
    # Upper half of the diamond (including the center line)
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
        
    # Lower half of the diamond
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

# Change this value to make the diamond larger or smaller
diamond_size = 6
print_diamond(diamond_size)
