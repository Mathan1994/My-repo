
class Person:        # define parent class
   
   def __init__(self):
      print "Calling parent constructor"

   def personMethod(self):
      if m.maleMethod:
          print 'Male'
      else:
          print 'Female'

class Male(Person): # define child class
   def __init__(self):
      print "Calling Male constructor"

   def maleMethod(self):
      print 'Calling male method'
class Female(Person):
    def __init__(self):
        print "Calling Female Constructor"

    def femaleMethod(self):
        print 'Calling Female method'

m = Female()          # instance of child
m.femaleMethod()      # child calls its method
m.personMethod()     # calls parent's method
