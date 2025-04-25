class Animal:
  def eat(self):
    print('Animal is eating')

  def walk(self):
    print('Animal is walking')

class Feline(Animal):
  def lick(self):
    print('Feline is licking his fur')

class Lion(Feline):
  def roar(self):
    print('Lion is roaring')

class Person:
  def watch(self, animal: Animal):
    animal.eat()


jhon = Person()


animal = Animal()
feline = Feline()

animal.eat()
feline.eat()


# If the results are always the same, not matter wich animal jhon watches, the Liskov substitution principle is being
# respected and applied
jhon.watch(feline)