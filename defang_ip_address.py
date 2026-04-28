'''' A defanged IP address is a modified version of a standard IP address (e.g., changing 192.168.1.1 to 192[.]168[.]1[.]1) created by replacing periods with special characters like [.]'''

def ip_address(address): 
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

IPad = input("Enter your IP address: ")

defang_ip = ip_address(IPad)

print(defang_ip)