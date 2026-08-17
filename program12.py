car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

del car["color"]

print("Key-Value Pairs:")
for key, value in car.items():
    print(key, ":", value)


if "model" in car:
    print("The key 'model' exists.")
else:
    print("The key 'model' does not exist.")