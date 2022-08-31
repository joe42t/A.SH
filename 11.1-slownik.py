countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals['Czech'] = "Prague"

# print(countries_and_capitals)
# for country, capital in countries_and_capitals.items():
#     print(country + "-" + capital)

# print(countries_and_capitals["USA"])
# print(countries_and_capitals.setdefault("USA", "Washington DC"))
# print(countries_and_capitals)

# countries_and_capitals["Poland"] = "Cracow"
# print(countries_and_capitals)

# countries_and_capitals.pop("Poland") 
# print(countries_and_capitals)

# print(countries_and_capitals.popitem())
# print(countries_and_capitals)

if "Berlin" in countries_and_capitals.values():
    print("Znaleziono")
else:
    print("Nie znaleziono")    

countries_and_capitals.clear()
print(countries_and_capitals)