from location import Location
from fare import Fare

class Transaction:
	def __init__(self, pickup_Location, dropoff_Location, fare, passengers, distance):
		self.pickup_Location = pickup_Location
		self.dropoff_Location = dropoff_Location
		self.fare = fare
		self.passengers = passengers
		self.distance = distance

	def getPickupLocation(self):
		return self.pickup_Location

	def getDropoffLocation(self):
		return self.dropoff_Location

	def getFare(self):
		return self.fare

