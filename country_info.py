from countryinfo import CountryInfo 

count = input("Enter your country: ")
country = CountryInfo(count)

print("Capital is: ", country.capital())
print("Curriencies is: ", country.currencies())
print("Language is: ", country.languages())
print("Borders are: ", country.borders())
print("Others name: ", country.alt_spellings())

