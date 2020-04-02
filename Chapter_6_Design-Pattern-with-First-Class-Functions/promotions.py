def fidelity_promo(invoice):
    '''customers with at least 1000 loyalty points are discounted for 5%'''
    if invoice.customer.fidelity >= 1000:
        return invoice.total() * 0.05
    return 0

def bulk_item_promo(invoice):
    '''items with quantity >= 20 are discounted for 10%'''
    discount = 0
    for item in invoice.item_list:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_order_promo(invoice):
    '''invoices with >= 10 different items are discounted for 7%'''
    return invoice.total() * 0.07 if len(invoice.item_list) >= 10 else 0
