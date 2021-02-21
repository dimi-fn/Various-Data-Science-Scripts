class Car:
  '''
  * Creating a class called "Car"

  * Properties/attributes: brand, colour, horses, country production, current speed 
    * "current_speed" is set to 0, unless other value is assigned

  * Method definitions: 
    * def move_car() moves the car by 10
    * def accelerate_car() accelerates the car by the given value and adds that speed to "current_speed"
    * def stop_car() sets "current_speed" to 0
    * def car_details() returns the properties of the "Car" class
  '''

  def __init__(self, brand, colour, horses, country_production, current_speed = 0):
    self.brand = brand
    self.colour= colour
    self.horses = horses
    self.country_production = country_production
    self.current_speed = current_speed
    

  def move_car(self):
    self.current_speed += 10

  def accelerate_car(self, value):
    self.current_speed += value

  def stop_car(self):
    self.current_speed = 0

  def car_details(self):
    print ("Brand: {}\nColour: {}\nHorses: {}\nCountry production: {}\nCurrent speed: {}\n".format(
        self.brand, self.colour, self.horses, self.country_production, self.current_speed))