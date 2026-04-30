tallies = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

# Conversion of Roman Numeral to Decimal numbers 
def roman_to_decimal(roman):
    roman = roman.upper()  # handle lowercase input safely
    total = 0

    for i in range(len(roman) - 1):
        current = tallies[roman[i]]
        next_val = tallies[roman[i + 1]]

        if current < next_val:
            total -= current
        else:
            total += current

    total += tallies[roman[-1]]
    return total

# Conversion of Decimal Numbers to Roman Numerals
def decimal_to_roman(num):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    result = ""

    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]

    return result


number = int(input("Enter Decimal Number: "))
print("Roman Numeral:", decimal_to_roman(number))

roman = input("Enter Roman Numerals: ")
print("Decimal Value:", roman_to_decimal(roman))