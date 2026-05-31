rows = int(input("Enter the rows: "))

print("\nLeft-Angled Half Pyramid")
for i in range(1, rows + 1):
    print("* " * i, end="")
    print("\r")

print("\nInverted Left-Angled Half Pyramid")
for i in range(rows, 0, -1):
    print("* " * i, end="")
    print("\r")

print("\nRight-Angled Half Pyramid")
for i in range(1, rows + 1):
   print("  " * (rows - i) + "* " * i, end="")
   print("\r")
