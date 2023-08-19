
from car_game import car
from car_game import racing as rc

myCarGame = rc.CarRacing()

car01 = car.Car('Car01', 'White', 250)
car02 = car.Car('Car02', 'Black', 200)
car03 = car.Car('Car03', 'Yellow', 220)
car04 = car.Car('Car04', 'Red', 280)
car05 = car.Car('Car05', 'Blue', 150)

myCarGame.addCar(car01)
myCarGame.addCar(car02)
myCarGame.addCar(car03)
myCarGame.addCar(car04)
myCarGame.addCar(car05)

myCarGame.startRacing()
