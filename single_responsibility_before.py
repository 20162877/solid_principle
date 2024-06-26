class Order:
    
    def __init__(self):
        self.items: list[str]=[]
        self.quantities: list[str]=[]
        self.prices: list[float]=[]
        self.payment_status: bool = False
        
    def add_item(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self)-> float:
        
        total: float = 0
        for i in range(len(self.prices)):
            total += self.quantities[i]*self.prices[i]
            
        return total
    
    def payment_process(self, payment_type, security_code):
        
        if payment_type == 'debit':
            print(f"Initializig Debit Payment type: ")
            print(f"Verifying Secirity Code: {security_code}")
            self.payment_status = True
            print("Payment Success")
        elif payment_type == 'credi':
            print(f"Initializig Credi Payment type: ")
            print(f"Verifying Secirity Code: {security_code}")
            self.payment_status = True
            print("Payment Success")
        
        else:
            print("Invalid Payment Method")
        
order = Order()
order.add_item('Laptop', 2, 45000)
order.add_item('HDD', 1, 2000)

order.payment_process('debit', '90r3434')