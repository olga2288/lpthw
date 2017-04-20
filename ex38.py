ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that"

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Songs', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']
print '\n'
while len(stuff) != 10:
  next_one = more_stuff.pop()
  print 'Addind: ', next_one
  stuff.append(next_one)
  print 'There are %d items now' % len(stuff)

print "\nThere we go: ", stuff
print "Let's do some things with stuff"

print stuff
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print ' '.join(stuff[3:5])
