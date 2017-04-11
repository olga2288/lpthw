def add (a,b):
    print "Adding %d + %d" %(a,b)
    return a + b

def subtract (a, b):
    print "Subtracting  %d - %d" % (a, b)
    return a - b

def multiply (a, b):
    print "Muptiplyng %d * %d" % (a, b)
    return a * b

def divide (a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "\nLet's do some math with just functions!"

age = add(30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "Hire is puzzle"

what = add (age, subtract(multiply(weight, divide (iq, 2)),height))

print "That becomes: ", what, "Can you do it by hand?"

a = add (25, 5)
b = subtract (40, 10)
c = multiply (100, 5)
d = divide (1000, 100)
print " a = %d, b = %d, c = %d, d = %d" % (a, b, c, d)
