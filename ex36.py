ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!from sys import exit

def choice_1():
    print "\nThis is sweet room"
    print "You can take some sweets"
    print "How many sweets do you take?"
    take = raw_input("> ")
    print take
    if int(take) <  10:
        print "\nDon't you like sweets?"
        print "The wind has blown and carried you here "
        choice_2()
    else:
        print "\nDo you have a sweet tooth"
        choice_3()

def choice_2():
    print "\nDo you like it?"
    print "It's seaside"
    print "You can stay here. Do you want to stay? "
    answr = raw_input("> ")
    if answr == 'yes':
        print "Ok. It is good choice"
        exit(0)
    else:
          choice_3()

def choice_3():
    print "\nThe wind has blown and carried you here. It's factory of sweets. "
    print "I'm very sorry, but ..."
    print "You must work in this factory two week to go back home"
    exit(0)



print "You is in room."
print "There are three doors: 1, 2, 3"
print "Choice any door"
choice = raw_input("> ")

if choice == "1":
    choice_1()
elif choice == "2":
    choice_2()
elif choice =="3":
    choice_3()
else:
    print "I'm very sorry, but you have to go out."
    exit(0)
