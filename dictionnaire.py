car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
  "greeting":lambda x:print("hello "+x)
}

print(car)
print(car["brand"])
print(car["year"])
print(car["colors"][0])
print(car["colors"][1])
print(car["greeting"]("hamza"))
print(len(car))
print(type(car))
print(car.get("model"))
print(car.keys())
print(car.values())
car["model"]="BMW"
print(car.get("model"))
print(car.items())

for x in car:
  print(x)
for x in car.values():
  print(x)

for x in car:
  print(car[x])

for x, y in car.items():
  print(x, y)
#  passage par reference
truck=car
#car=None
#truck["model"]="Mercedes"
print(truck["model"])
# passage par valeur

truck1=car.copy()
truck1["model"]="Mercedes"
print(car["model"])
print(car.get("
