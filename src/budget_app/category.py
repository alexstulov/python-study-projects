class Category:
    name = ""
    ledger = []
    # fix one same ledger for all categories problem
    def make_a_ledger(self):
        return []
    
    def __init__(self, category_name):
       self.name = category_name
       self.ledger = self.make_a_ledger()
    
    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description,
        })
    
    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            'amount': -amount,
            'description': description,
        })
        return True
    
    def transfer(self, amount, another_category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, "Transfer to " + another_category.name)
        another_category.deposit(amount, "Transfer from " + self.name)
        return True
    
    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            total += transaction['amount']
        return total
    
    def get_deposits_total(self):
        total = 0
        for transaction in self.ledger:
            amount = transaction['amount']
            if amount > 0:
                total += amount
        return total
    
    def get_withdrawals_total(self):
        total = 0
        for transaction in self.ledger:
            amount = transaction['amount']
            if amount < 0:
                total += amount
        return total
    
    def check_funds(self, amount):
        total = self.get_deposits_total()
        return True if total >= amount else False
    
    def generate_first_line_for_str(self, max_length):
        name_length = len(self.name)
        asterisk_amount = max_length - name_length
        first_line = ""
        asterisk_block = "*" * int(asterisk_amount / 2)
        first_line = asterisk_block + self.name + asterisk_block
        if asterisk_amount % 2:
            first_line += "*"
        return first_line
    
    def generate_transaction_line_for_str(self, transaction, max_length):
        name = transaction['description'][:23]
        amount = str("{:.2f}".format(transaction['amount']))[:7]
        characters_amount = len(name) + len(amount)
        spacer = ""
        if (characters_amount < max_length):
            spacer = " " * abs(characters_amount - max_length)
        return name + spacer + amount
    
    def __str__(self):
        max_length = 30
        first_line = self.generate_first_line_for_str(max_length) + "\n"
        lines = []
        for transaction in self.ledger:
            lines.append(self.generate_transaction_line_for_str(transaction, max_length))
        result = first_line + "\n".join(lines) + "\n"
        total = "Total: " + str(self.get_balance())
        return result + total
