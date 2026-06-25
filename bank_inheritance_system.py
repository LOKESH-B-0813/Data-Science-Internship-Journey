# =====================================================================
# 1. SINGLE INHERITANCE (1 Parent ➡️ 1 Child)
# =====================================================================
# WHY: To share baseline identity and balance tracking without rewrite.
# WHEN: When a specific account "is a" basic account.
class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        return f"👤 {self.account_holder} | Balance: ${self.balance}"

# SavingsAccount inherits directly from ONE parent (Account)
class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        return f"📈 Interest added! New Balance: ${self.balance}"


# =====================================================================
# 2. MULTILEVEL INHERITANCE (Grandparent ➡️ Parent ➡️ Child)
# =====================================================================
# WHY: To create layers of specialized accounts (tiers).
# WHEN: When a class is a modified version of an already modified class.
# PremiumSavingsAccount inherits from SavingsAccount, which inherits from Account
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_holder, balance, VIP_bonus=50):
        # super() passes data up the chain to SavingsAccount, then to Account
        super().__init__(account_holder, balance)
        self.VIP_bonus = VIP_bonus

    def give_seasonal_bonus(self):
        self.balance += self.VIP_bonus
        return f"🎁 VIP Bonus of ${self.VIP_bonus} applied!"


# =====================================================================
# 3. MULTIPLE INHERITANCE (Parent A + Parent B ➡️ 1 Child)
# =====================================================================
# WHY: To combine entirely different business features into a hybrid tool.
# WHEN: When an object needs traits from two completely separate parents.
class InvestmentPlan:
    def __init__(self, risk_level="Medium"):
        self.risk_level = risk_level
    
    def view_portfolio(self):
        return f"📊 Trading Portfolio Risk Status: {self.risk_level}"

# HybridAccount inherits from BOTH Account and InvestmentPlan
class HybridInvestmentAccount(Account, InvestmentPlan):
    def __init__(self, account_holder, balance, risk_level):
        # Initialize both parents explicitly to avoid confusion
        Account.__init__(self, account_holder, balance)
        InvestmentPlan.__init__(self, risk_level)


# =====================================================================
# 4. HIERARCHICAL INHERITANCE (1 Parent ➡️ Multiple Separate Children)
# =====================================================================
# WHY: To create branched variations from a single master standard.
# WHEN: When two completely different account types share the same root.
# (Both SavingsAccount above and CheckingAccount below inherit from Account)
class CheckingAccount(Account):
    def write_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✍️ Check cleared for ${amount}."
        return "❌ Check bounced! Insufficient funds."


# =====================================================================
# 🧪 LOGIC VERIFICATION (Running the Bank)
# =====================================================================
print("--- 1. Testing Single Inheritance ---")
savings = SavingsAccount("Alice", 1000)
print(savings.display_balance())  # Inherited method
print(savings.add_interest())     # Child method

print("\n--- 2. Testing Multilevel Inheritance ---")
premium = PremiumSavingsAccount("Bob", 5000)
print(premium.display_balance())   # From Grandparent (Account)
print(premium.add_interest())      # From Parent (SavingsAccount)
print(premium.give_seasonal_bonus()) # From Child itself

print("\n--- 3. Testing Multiple Inheritance ---")
hybrid = HybridInvestmentAccount("Charlie", 10000, "High")
print(hybrid.display_balance())    # From Parent A (Account)
print(hybrid.view_portfolio())     # From Parent B (InvestmentPlan)

print("\n--- 4. Testing Hierarchical Inheritance ---")
checking = CheckingAccount("Lokesh", 300)
print(checking.display_balance())  # Shared parent setup
print(checking.write_check(100))   # Checking unique branch action