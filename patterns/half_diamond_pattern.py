rows = int(input("Enter the rows: "))

print("\nLeft-Angled Half Diamond")
for i in range(1, rows + 1):
    print("* " * i, end="")
    print("\r")

for i in range(rows - 1, 0, -1):
    print("* " * i, end="")
    print("\r")

print("\nRight-Angled Half Diamond")
for i in range(1, rows + 1):
   print("  " * (rows - i) + "* " * i, end="")
   print("\r")

for i in range(rows - 1, 0, -1):
   print("  " * (rows - i) + "* " * i, end="")
   print("\r")
