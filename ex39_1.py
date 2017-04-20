my_country = {
"cap_city" : "Minsk",
"cities" : ['G', 'GR', "B", 'V', "M"]
}

city = {
"G" : "Gomel",
"GR" : "Grodno",
"B" : "Brest",
"V" : "Vitebsk",
"M" : "Mogilev"
}

print my_country
print city
print "\n"


print city[my_country['cities'][1]]



for cabbr in my_country['cities']:
    print city[cabbr]

abbr = raw_input('> ')
print city.get(abbr, "not found")
GR = "GR"
print city.get(GR)
