import getpass 

database = {
    "rohan": "987654", 
    "reigns": "130456", 
    "Kennith": "454578",
}

username = input("Enter the username: ")

password = getpass.getpass("Enter your password: ")

for i in database.keys(): 
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break
print("Verified")