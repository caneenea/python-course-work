"""
Build a class thats a type of ticket, date number of ticket , server , and a list of the total of the items purchased.
Build a method that returns the sum of money
"""

class Ticket:
    def __init__(self, date, total, server, products):
        self.total = total
        self.date = date
        self.server = server
        self.products = products

        def total(self):
            s= 0
            for x in self.products:
                s = s + x
            return s

f1 = Ticket(1 ,
            )



