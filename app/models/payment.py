class PaymentMessage:
    def __init__(self, sender, receiver, amount, currency):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.currency = currency