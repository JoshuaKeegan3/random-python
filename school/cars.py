# Cars.py
# Author: Joshua Keegan
# Date: who cares
# Creates cars, check if they are traveling above speed limit of cameras
##


# Imports
import random


class Car():
   """ Car Class
   contains:

   number_plate
   speed
   """

   def __init__(self, number_plate="", speed=""):
      """ Initulise the Car """

      # If there is no number plate then give it a random one
      if number_plate == "":

         # Create number plate
         self.number_plate = ""

         # Add 3 letters
         for i in range(3):
            self.number_plate += chr(random.randint(65, 90))

         # Add 3 numbers
         for i in range(3):
            self.number_plate += str(random.randint(0, 9))

      # Otherwise keep it as the given numberplate
      else:
         self.number_plate=number_plate

      # If no speed is given give it a random speed (20 - 120)
      if speed == "":
         self.speed = random.randint(20, 120)

      # Otherwise keep the spped as it is
      else:
         self.speed = speed


class Camera():
   """ Camera Class
   contains:

   speed_limit
   ofenders

   read_speed()
   take_a_photo()
   """

   def __init__(self, limit):
      """ Initulise the camera """

      # Create the speed limit for the camera
      self.speed_limit = limit

      # Create a list of future offenders
      self.ofenders = []

   def read_speed(self, car):
      """ Method to check if a car is speeding"""

      # If the cars speed is greater than the speed limit
      if car.speed > self.speed_limit:
         
         # Record the cars number plate
         self.take_a_photo(car)

   def take_a_photo(self, car):
      """ Method record offending cars
      Adds cars number plate to ofenders list attribute
      """

      self.ofenders.append([car.number_plate, str(car.speed)])


def create_random_cars(amount):
   """ Function to create a list of random cars
   Takes a single variable, amount, for the number of cars to create
   Returns a list of random cars of length "amount"
   """
   # Predefine list
   cars = []

   # Fill list
   for i in range(amount):
      cars.append(Car())

   return cars

if __name__ == "__main__":
   # Create 50 random cars
   cars = create_random_cars(50)

   # Create cameras
   cameras = []
   cameras.append(Camera(50))
   cameras.append(Camera(80))
   cameras.append(Camera(100))

   # Check if a car is speeding
   for car in cars:
      for cam in cameras:
         cam.read_speed(car)

   # Show ofenders
   for cam in cameras:
      print('The offenders of the {}km/ph cammera were:'.format(cam.speed_limit))
      for ofender in cam.ofenders:
         print(' with a speed of: '.join(ofender))

      print('\n')
