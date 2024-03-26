# Open close principle stands for open for extension and close for modification
# In payment pocess We can't add new payment pethod without having to change existing code.
# Resulting violates open close principle

# Now IT dont' violates Open close principle.
# If we want to any new payment method such as Paypal, UPI , We have to just create new class.
# Start using it.

from abc import ABC, abstractmethod

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
 
class PaymentProcess(ABC):
    
    @abstractmethod
    def pay(self, order, security_code):
        pass
               
class DebitPaymentProcess(PaymentProcess):
    
    def pay(self, order, security_code):
        print(f"Initializig Debit Payment type: ")
        print(f"Verifying Secirity Code: {security_code}")
        order.payment_status = True
        print("Payment Success")
        
class CreditPaymentProcess(PaymentProcess):
    
    def pay(self, order, security_code):
        print(f"Initializig Credit Payment type: ")
        print(f"Verifying Secirity Code: {security_code}")
        order.payment_status = True
        print("Payment Success")
# Adding new payment method
class PayPalPaymentProcess(PaymentProcess):
    
    def pay(self, order, email_address):
        print(f"Initializig Pyapal Payment type: ")
        print(f"Verifying email Code: {email_address}")
        order.payment_status = True
        print("Payment Success")

        
order = Order()
order.add_item('Laptop', 2, 45000)
order.add_item('HDD', 1, 2000)
print(f"Total price: {order.total_price()}")
payment=PayPalPaymentProcess()
payment.pay(order, 'syedzaidahmad99@gmail.com')