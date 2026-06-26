from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION (The Rules Template)
# ==========================================
class BankRules(ABC):
    @abstractmethod
    def process_transaction(self, amount):
        pass


# ==========================================
# 2. ENCAPSULATION (The Secure Account)
# ==========================================
class BankAccount(BankRules):
    def __init__(self, owner, initial_balance):
        self.owner = owner
        # Encapsulation: The '__' locks the balance. It is private.
        self.__balance = initial_balance 

    # Getter: Safe way to check the balance
    def get_balance(self):
        return self.__balance

    # Setter: Safe way to add money with rules
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"💰 Deposited ${amount}.")
        else:
            print("❌ Invalid amount!")

    # This satisfies the Abstraction rule
    def process_transaction(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False


# ==========================================
# 3. INHERITANCE (The Specialized Account)
# ==========================================
# SavingsAccount inherits everything from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, initial_balance, interest_rate=0.05):
        # super() sets up the owner and secure balance in the parent class
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Read the balance using the getter, calculate interest, and deposit it
        interest_money = self.get_balance() * self.interest_rate
        self.deposit(interest_money)
        print(f"📈 Interest of ${interest_money} added!")


# ==========================================
# 4. POLYMORPHISM (Different Behaviors)
# ==========================================
class BusinessAccount(BankAccount):
    # Overriding the parent's process_transaction to include a transaction fee
    def process_transaction(self, amount):
        fee = 5  # Business accounts pay a $5 fee per transaction
        total_deduction = amount + fee
        
        # Accesses parent logic to see if they have enough money for amount + fee
        if self.get_balance() >= total_deduction:
            # We call the parent's transaction logic to safely deduct the funds
            super().process_transaction(total_deduction)
            print(f"🏢 Business Transaction cleared! (Included a $5 corporate fee)")
            return True
        print("❌ Business transaction denied: Insufficient funds for amount + fee.")
        return False


# ==========================================
# 🧪 RUNNING THE BANK SYSTEM
# ==========================================

print("--- Testing Encapsulation & Inheritance ---")
lokesh_savings = SavingsAccount("Lokesh", 1000)
lokesh_savings.deposit(500)             # Inherited from parent
lokesh_savings.apply_interest()         # Child's unique method
print(f"Lokesh's Balance: ${lokesh_savings.get_balance()}") # Using the safe Getter

print("\n--- Testing Polymorphism ---")
corp_account = BusinessAccount("MegaCorp", 1000)
corp_account.process_transaction(100)  # Runs the custom business fee logic
print(f"MegaCorp's Balance: ${corp_account.get_balance()}")