countries = ["Belize", "United States", "Norway", "China", "England", "Wales", "Spain", "Russia", "Venezuela"]

print(sorted(countries))
countries.sort(reverse=True)
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
print(len(countries))

countries.insert(4, "Somalia")
print(countries)

countries.append("South Korea")
print(countries)

countries.remove("Somalia")
print(countries)

countries.insert(2, "Nigeria")

print(countries.pop())