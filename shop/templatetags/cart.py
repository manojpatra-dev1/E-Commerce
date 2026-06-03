from django import template

register = template.Library()


# GET ITEM FILTER
@register.filter(name='get_item')
def get_item(cart, key):
    item = cart.get(str(key))
    if item:
        return item['quantity']
    return 0


# CART TOTAL FILTER
@register.filter(name='cart_total')
def cart_total(products, cart):
    total = 0

    for product in products:
        item = cart.get(str(product.id))
        if item:
            total += product.price * item['quantity']

    return total


# MULTIPLY FILTER
@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg