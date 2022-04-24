class Item:
	pay_rate = 0.8
	all = []
	def __init__(self, name: str, price: float, quantity=0):
		assert price >= 0, f'Price {price} is not greater to or equal to zer0'
		assert quantity >= 0, f'Quantity {quantity} is not greater to or equal to zer0'
		
		self.name = name
		self.price = price
		self.quantity = quantity
		
		Item.all.append(self)
		
	def calculate_total_price(self):
		return self.price * self.quantity
		