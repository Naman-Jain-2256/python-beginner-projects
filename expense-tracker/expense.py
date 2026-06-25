class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {'category':self.category, 'amount':self.amount}
    
    def __str__(self):
        return f"{self.category} - ₹{self.amount}"
    
