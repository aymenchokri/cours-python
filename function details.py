def my_function():
  print("Hello from a function")

def my_function1(a):
  print("Hello from a function",a*2)
my_function()
my_function1(10)

def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

def my_function(*kids):
  print(kids)
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def functiondectionairy(**kwargs):
    print(kwargs)
    print(kwargs.values())
    
functiondectionairy(name="alex",age=16)

def country(country="USA"):
    print(country)
    
country("tunisia")
country()