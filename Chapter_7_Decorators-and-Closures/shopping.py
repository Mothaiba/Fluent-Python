'''
    This program implements the process of checking-out and applying discount
'''

import inspect
import promotions

class Customer:

    def __init__(self, name, fidelity):
        self.name = name
        self.fidelity = fidelity

class Item:

    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Invoice:

    def __init__(self, customer, item_list, promotion=None):
        self.customer = customer
        self.item_list = item_list
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.item_list)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return 'Invoice total: {:.2f}, due: {:.2f}'.format(self.total(), self.due())

def best_promo(invoice):
    '''Select the best promotion'''
    return max(promo(invoice) for promo in promotions.promos)

if __name__ == '__main__':
    tung = Customer('Tung Phung', 0)
    tony = Customer('Tony Bibi', 1200)

    cart = [Item('banana', 4, .5),
            Item('apple', 10, 1.5),
            Item('watermelon', 5, 5.0)]
    
    print(Invoice(tung, cart, best_promo))
    print(Invoice(tony, cart, best_promo))
    
    banana_cart = [Item('banana', 30, .5),
                   Item('apple', 10, 1.5)]
    print(Invoice(tung, banana_cart, best_promo))

    long_order = [Item(str(item_code), 1, 1.0)
                  for item_code in range(10)]
    print(Invoice(tung, long_order, best_promo))

