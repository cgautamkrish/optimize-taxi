
class Fare:
	def __init__(self, amount, tips, toll, total, payment_type):
		self.amount = amount
		self.tips = tips
		self.toll = toll
		self.total = total
		self.payment_type = payment_type
 
	def getAmount(self):
		return self.amount

	def getTotal(self):
		return self.total