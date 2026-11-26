"""Problem 59: Menu-driven bank account simulator (scripted demo)"""


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit must be positive."
        self.balance += amount
        return f"Deposited {amount:.2f}."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount:.2f}."


def bank_menu():
    """Interactive menu version: call this from the console to try it."""
    acct = BankAccount("User")
    while True:
        print("\n1) Deposit  2) Withdraw  3) Balance  4) Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            print(acct.deposit(float(input("Amount: "))))
        elif choice == "2":
            print(acct.withdraw(float(input("Amount: "))))
        elif choice == "3":
            print(f"Balance: {acct.balance:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def p59():
    # The demo plays a scripted session. Run bank_menu() for the real thing.
    acct = BankAccount("Demo", 1000)
    for action, amount in [("deposit", 500), ("withdraw", 200),
                           ("withdraw", 5000), ("deposit", -10)]:
        print(getattr(acct, action)(amount))
    print(f"Final balance: {acct.balance:.2f}")


if __name__ == "__main__":
    p59()
