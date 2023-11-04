# Create a dictionary of rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Mississippi': 'United States'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
