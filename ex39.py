# create a mapping of state to abbreviation
states = {
    'Oregon' : "OR",
    "Florida" : "FL",
    "California" : "CA",
    "New York" : "NY",
    "Michigan" : 'MI'
}

# create a basic set of states and some cities in them
cities ={
    'CA': 'San Francisco',
    'MI' : 'Detroit',
    'FL' : "Jaksonville"
}

# add some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

print "-" * 10
print 'NY State has: ', cities['NY']
print "OR State has: ", cities['OR']
print "-" * 10
print "\nMichigan's abbriviation is: ", states['Michigan']
print "Florida's abbriviation is: ", states['Florida']
print "\n"
print '-' * 10

# do it by using the state then cities dict
print "\n Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
print "\n"

# print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
    print "%s is abbriviated %s" % (state, abbrev)
print "\n"

#print every city in state
print "-" * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print "-" * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


print "-" *10

# safely get a abbreviation by state that might not be there
state = states.get('Texas')
print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', "Does not exist")
print "The city for the state 'TX' is: %s" % city
