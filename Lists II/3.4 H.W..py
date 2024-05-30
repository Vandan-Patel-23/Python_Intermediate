countries = []
while True:
    country = input("Enter a country's name (type 'Done' to stop): ")
    if country == 'Done':
        break
    countries.append(country.title())
countries.sort()

while countries:
    current_country = countries.pop(0)
    print(current_country)
cities = ["Portland", "San Francisco", "Houston", "Boston"]
states = ["Oregon", "California", "Texas", "Massachusetts"]
city_state = []
for i in range(len(cities)):
    city_state.append(cities[i], states[i])

days = ["monday", "wednesday", "thursday"]
days.insert(1, "tuesday")
days.append("friday")
days.extend(["saturday", "sunday"])

print("\nCity State List:", city_state)
print("Days List:", days)
