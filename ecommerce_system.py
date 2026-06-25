from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION
# ==========================================
# We define a strict template for payments. 
# You can't create a generic 'PaymentGateWay', you must use a specific one.
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# ==========================================
# 2. ENCAPSULATION & 3. INHERITANCE
# ==========================================
class Customer:
    def __init__(self, username, initial_balance):
        self.username = username
        # Encapsulation: __balance is private. Code outside this class cannot touch it directly.
        self.__balance = initial_balance 

    # Getter: Safe way to read the private balance
    def get_balance(self):
        return self.__balance

    # Setter: Safe way to modify the private balance with rules
    def deduct_funds(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        print(block := f"❌ Denied: Insufficient funds for {self.username}.")
        return False


# INHERITANCE: VIPCustomer gets everything Customer has, plus unique features
class VIPCustomer(Customer):
    def __init__(self, username, initial_balance, discount_rate=0.10):
        # super() initializes the parent (Customer) class traits
        super().__init__(username, initial_balance)
        self.discount_rate = discount_rate

    # Custom VIP logic
    def get_discounted_price(self, price):
        return price * (1 - self.discount_rate)


# ==========================================
# 4. POLYMORPHISM
# ==========================================
# Both classes share the 'process_payment' name but execute completely different code.
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        return f"💳 Processing ${amount} securely through Visa/Mastercard networks."

class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        return f"🅿️ Redirecting to PayPal digital wallet to authorize ${amount}."


# ==========================================
# PUTTING IT TO WORK (The Real World System)
# ==========================================

# 1. Create our users
regular_joe = Customer("Joe", 100)
vip_valerie = VIPCustomer("Valerie", 500) # Inherits behavior

# 2. Setup checkout item price
item_price = 150

# 3. Simulate VIP Benefit (Inheritance & unique trait usage)
final_price_for_valerie = vip_valerie.get_discounted_price(item_price) # 150 - 10% = 135

# 4. Choose Payment Methods (Polymorphism in action)
card_processor = CreditCardPayment()
paypal_processor = PayPalPayment()

# 5. Run the transactions
print(f"--- Processing Valerie's Order ---")
if vip_valerie.deduct_funds(final_price_for_valerie): # Encapsulation checks funds safely
    print(paypal_processor.process_payment(final_price_for_valerie)) # Polymorphism
    print(f"Remaining Balance: ${vip_valerie.get_balance()}")

print(f"\n--- Processing Joe's Order ---")
if regular_joe.deduct_funds(item_price):
    print(card_processor.process_payment(item_price))