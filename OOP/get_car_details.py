# from car.py import the class "Car"
from car import Car

print("The doc string of the above class is:\n")
print(Car.__doc__)

new_car = Car(brand="Mercedes", colour="black", horses= 200, country_production= "Germany")
new_car

new_car.car_details()

new_car.move_car()
new_car.current_speed

new_car.accelerate_car(80)
new_car.current_speed

new_car.stop_car()
new_car.current_speed

new_car.move_car()
new_car.current_speed

new_car.accelerate_car(280)
new_car.car_details()