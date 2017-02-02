class BankAccount(object):

    def __init__(self, accountNumber, Balance):

        self.accountNumber = accountNumber

        self.balance = Balance

    def withdraw(self,withdrawalAmount):

        self.balance = self.balance - withdrawalAmount

        if self.balance < 0:

            print("Error: Your balance is less than 0")

    def deposit(self, depositAmount):

        self.balance = self.balance + depositAmount

    def get_balance(self):

        return self.balance

def main():

    my_account = BankAccount("BOA123", 1000)

    print("Current balance is: ", my_account.get_balance())

    my_account.deposit(100)

    print("Current balance is: ", my_account.get_balance())

    my_account.withdraw(500)

    print("Current balance is: ", my_account.get_balance())

    my_account.withdraw(1000) #prints an error message

main()
