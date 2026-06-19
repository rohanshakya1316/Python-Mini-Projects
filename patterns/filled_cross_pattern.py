rows = 5

# --- Top Half (Inverted Pyramid) ---
for i in range(rows, 0, -1):
    # Inner loop for leading spaces
    for j in range(0, rows - i):
        print("  ", end="")
    
    # Inner loop for asterisks
    for k in range(0, 2 * i - 1):
        print("* ", end="")
        
    print("\r")

# --- Bottom Half (Upright Pyramid) ---
for i in range(1, rows + 1):
    # Inner loop for leading spaces
    for j in range(0, rows - i):
        print("  ", end="")
        
    # Inner loop for asterisks
    for k in range(0, 2 * i - 1):
        print("* ", end="")
        
    print("\r")


print("============== SHORTCUT METHOD ==============")
for i in range (rows, 0, -1):
    print("  " * (rows - i) + "* " * (2 * i - 1), end="")
    print("\r")

for i in range (1, rows + 1):
    print("  " * (rows - i) + "* " * (2 * i - 1), end="")
    print("\r")