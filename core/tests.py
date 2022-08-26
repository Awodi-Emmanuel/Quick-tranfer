from django.test import TestCase

# Create your tests here.

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

pop_model = car.pop("model")

print(car)