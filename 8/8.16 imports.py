import car

print(car.make_car('RAM', '1500', trim='limited', color='black'))

from car import make_car

print(make_car('Toyota', 'Corolla', trim='DE'))

from car import make_car as mc

print(mc('Ford', 'F150'))

import car as c
print(c.make_car('Mitsubishi', 'Lancer'))

from car import *
print(make_car('Toyota', 'Tacoma', year=2008))