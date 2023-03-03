class Person:
  def __init__(loco, name, age):
    loco.name = name
    loco.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
  
  def __myfunct__(loco):
    print(f"Hello my name is {loco}")

p1 = Person("John", 36)

p1.__myfunct__()
