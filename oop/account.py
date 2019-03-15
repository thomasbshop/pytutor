import datetime
import pytz


class Account:
    """Simple account class to implement a bank account"""

    # a static method is shared by all instances of the class.underscore indicates that the method is nonpublic.
    # rename all sensitive data attributes using underscore to avoid manipulation.
    # python mangle all the data attributes beginning with 2 underscores and ending with not more than 1 underscore.
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for {0} with \"int: {1:d};  hex: {1:x};  oct: {1:o};  bin: {1:b}\" balance.".
              format(name, balance))

    def deposit(self,  amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
            self.show_balance()

    def show_balance(self):
        print("The balance is: {:,}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawal"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":  # run if the program is executed as a script.
    thomas = Account("Thomas Account", 435)
    thomas.show_balance()

    thomas.deposit(345635656)

    thomas.withdraw(356635)

# A client is anything that uses a particular class.
    thomas.show_transactions()

    francis = Account("Francis Account", 1435)
    francis.__balance = 200
    francis.show_balance()

    francis.deposit(5656)

    francis.withdraw(635)

    # A client is anything that uses a particular class.
    francis.show_transactions()
    print(francis.__dict__)

# NB: _Account__balance - python generates the variable.
