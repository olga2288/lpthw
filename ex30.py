people = int(raw_input("\nType people: >"))
cars = int(raw_input("Type cars: >"))
trucks = int(raw_input("Type trucks: >"))
print "\n"

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide"

if trucks > cars:
    print "That's too many truck"
elif trucks < cars:
    print "Maybe we could take the trucks"
else:
    print "We still can't decide"

if people > trucks:
    print "Alright, let's just take the trucks"
else:
    print "Fine, let's stay home then"
