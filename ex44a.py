
class Parent(object):

    def implicit(self):
        print "Parent implicit()"

class Child(Parent):
    pass

father = Parent()
son = Child()

father.implicit()
son.implicit()




        
