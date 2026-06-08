# wrong 

def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart 

alice = add_to_cart("shoes")
bob = add_to_cart("mango")
print(alice) # ['shoes','mango'] alice only added shoe to cart

# right 

def add(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
alice = add("shoes")
bob = add("mango")

print(alice) # returns only the item added to cart 