class Car:
     def __init__(self, max_speed, unit):
         self.max_speed = max_speed
         self.unit = unit

     def unit_logic(self):
         if self.max_speed >= 120:
             self.unit = "km/h"
             return self.unit
         else:
             self.unit = "mph"
             return self.unit

     def __str__(self):
         t1 = self.unit_logic()
         return "Car with maximum speed of {0} {1}".format(self.max_speed, t1)

car = Car(94, "km/h")
print(car)
car = Car(394, "km/h")
print(car)