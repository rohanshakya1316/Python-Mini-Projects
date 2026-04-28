names = []

phone_numbers = []

num = int(input("Enter number of contact you want to save: "))

for i in range(num):
    name = input("Name: ").strip()
    phone_number = input("Phone Number: ").strip()
    print()
    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number")
print("----------------------------------------")

for i in range(num): 
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search term (name): ")

print("Search result: ")

if search_term in names: 
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

else: 
    print("Name Not Found.")