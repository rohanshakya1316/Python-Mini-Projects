size = 7

# Outer loop for rows
for i in range(size):
    # Inner loop for columns
    for j in range(size):
        # Check if current position is on either diagonal
        if i == j or i + j == size - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    # Move to the next line after finishing a row
    print()
