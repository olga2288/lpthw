from sys import argv
script, filename = argv

print "\nWe're going to read %r" % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN"
raw_input("?")
print "Opening the file..."
target = open(filename, 'r')

print target.read()

print "Now I'm going to ask you for three lines "

line1 = raw_input("line 1: ")


print "Now I'm going to write these to file"
target.write(line1)
target.write("\n")
print target.read()
print "and finally, we close it"


target.close()
