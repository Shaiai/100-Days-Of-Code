def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get['make']
        self.model = kw.get['model']
        self.color = kw.get['color']
        self.seats = kw.get['seats']


my_car = Car(make='Nissan', model='Skyline', color='Orange')
print(my_car)