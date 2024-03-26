#ISP Stand for instad of one generic interfate 
# we must have seperate interface deeling with single responsiblity.

#Issue
# Credit card paymet don't support sms authorization , BUt have implement sms_auth method.
# Since peyment process interface contains two method violates ISP.

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
    def sms_auth(self, code):
        pass
    
    @abstractmethod
    def pay(self, order):
        pass
               
class DebitPaymentProcess(PaymentProcess):
    
    def __init__(self, security_code, code) -> None:
        self.security_code: str = security_code
        self.verify: bool = False
    
    def sms_auth(self, code):
        print(f"Verifying sms code: {code}")
        self.verify = True
        
        
    def pay(self, order):
        
        print(f"Initializig Debit Payment type: ")
        
        if not self.verify:
            raise Exception("Not Authorised")
        
        print(f"Verifying Secirity Code: {self.security_code}")
        order.payment_status = True
        print("Payment Success")
       
        
class CreditPaymentProcess(PaymentProcess):
    
    def __init__(self, security_code) -> None:
        self.security_code: str = security_code
    
    def sms_auth(self, code):
        raise Exception("Credit card payment don't support sms authorization")
    
    def pay(self, order):
        print(f"Initializing Credit Payment type: ")
        print(f"Verifying Secirity Code: {self.security_code}")
        order.payment_status = True
        print("Payment Success")
        
        
class PayPalPaymentProcess(PaymentProcess):
    
    def __init__(self, email_address) -> None:
        self.email_address: str = email_address
        self.verify: bool = False
    
    def sms_auth(self, code):
        print(f"Verifying sms code: {code}")
        self.verify = True
        
    def pay(self, order):
        print(f"Initializig Pyapal Payment type: ")
        
        if not self.verify:
            raise Exception("Not Authorised")
        
        print(f"Verifying email Address: {self.email_address}")
        order.payment_status = True
        print("Payment Success")

        
order = Order()
order.add_item('Laptop', 2, 45000)
order.add_item('HDD', 1, 2000)
print(f"Total price: {order.total_price()}")
payment=PayPalPaymentProcess('syedzaidahmad99@gmail.com')
payment.sms_auth('934839')
payment.pay(order)