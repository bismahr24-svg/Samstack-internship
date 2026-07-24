# Day 11 Task: Payment Gateway System using Abstract Classes in Python.

from abc import ABC ,abstractmethod 

class PaymentGateway(ABC) :
  @abstractmethod
  def process_payment(self,amount) :
    pass 

class StripeGateway(PaymentGateway) :
      def process_payment(self,amount) :
        print(f"processing ${amount} via Stripe ")


class PayPalGateway(PaymentGateway) :
  def process_payment(self,amount) :
        print(f"processing ${amount} via PayPal ")

def checkout(gateway_obj ,amount):
    gateway_obj.process_payment(amount)

stripe = StripeGateway()
paypal = PayPalGateway()
checkout(stripe, 500)
checkout(paypal, 600)
