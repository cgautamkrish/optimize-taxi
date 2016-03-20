from location import Location

class Transaction:
   def __init__(self, pickup_Location, dropoff_Location):
      self.pickup_Location = pickup_Location
      self.dropoff_Location = dropoff_Location

   def getPickupLocation(self):
      return self.pickup_Location

   def getDropoffLocation(self):
      return self.dropoff_Location