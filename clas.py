class Account:
    def __init__(self):
        self.deposits = [] 
        self.withdrawals = []  
        self.loan_balance = 0  

    def check_balance(self):
     
        deposits_total = sum(transaction["amount"] for transaction in self.deposits)
        withdrawals_total = sum(transaction["amount"] for transaction in self.withdrawals)
        balance = deposits_total - withdrawals_total
        return balance

    def deposit(self, amount):
     
        self.deposits.append({"amount": amount, "narration": "deposit"})

    def withdrawal(self, amount):

        self.withdrawals.append({"amount": amount, "narration": "withdrawal"})

    def print_statement(self):
  
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
      
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance += amount
                print("Loan approved!")
            else:
                print("Loan amount exceeds the limit.")
        else:
            print("Unable to borrow a loan.")

    def repay_loan(self, amount):

        if amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.deposit(overpayment)
            print("Loan fully repaid and overpayment added to the account balance.")
        else:
            self.loan_balance -= amount
            print("Loan partially repaid.")

    def transfer(self, amount, recipient_account):

        if amount <= self.check_balance():
            self.withdrawal(amount)
            recipient_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient funds for the transfer.")