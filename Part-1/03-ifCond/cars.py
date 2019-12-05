cars = ['audi', 'bmw', 'toyota', 'scorpio', 'tesla']

for car in cars:
    if len(car) <= 3:
        print(car.upper())
    else:
        print(car.title())

x = len(cars[0])
print(x)


