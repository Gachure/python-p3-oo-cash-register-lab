class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.transactions = []
    
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.transactions.append(price * quantity)
        self.items.extend([title] * quantity)
    
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Format the total as integer if it's an integer value
            if self.total.is_integer():
                total_str = f"{int(self.total)}"
            else:
                total_str = f"{self.total:.2f}"
            print(f"After the discount, the total comes to ${total_str}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
