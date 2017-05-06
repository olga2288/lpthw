class Other(object):

    def implicit(self):
        print "\nOther implicit"

    def override(self):
        print "Other override"

    def altered(self):
        print "Other altered"

class Child(object):

    def __init__(self):
        self.son = Other()

    def implicit(self):
        self.son.implicit()

    def override(self):
        print "Son override"

    def altered(self):
        print "\nSon altered"
        self.son.altered()
        print "**********"

son1 = Child()

son1.implicit()
son1.override()
son1.altered()
