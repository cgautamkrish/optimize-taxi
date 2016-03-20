
class Location:
	def __init__(self, latitude, longitude, cluster, type):
		self.latitude = latitude
		self.longitude = longitude
		self.cluster = cluster
		self.type = type

	def getLatitude(self):
		return self.latitude

	def getLongitude(self):
		return self.longitude

	def getCluster(self):
		return self.cluster

	def getLocationType(self):
		return self.type