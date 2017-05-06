
class Parent(object):

    def hello(self):
        print "\nHello all!!!"

# implicite
    def bzz(self):
        print "\nI'm sleeping now!!!"
        print "Bz-z-z-z-z"

class Child(Parent):
# override
    def hello(self, name):
        self.name = name.title()
        print "\n\tHello %s" % self.name

class Child_2(Parent):
# alteted
    def hello(self,name):
        super(Child_2, self).hello()
        self.name = name.title()
        print "\n\tHello %s" % self.name



dad = Parent()
son = Child()
daughter = Child()
daughter_2 = Child_2()

dad.hello()
son.hello('ivan')
son.bzz()
daughter.hello('olga')
daughter_2.hello('dasha')
daughter_2.bzz()
