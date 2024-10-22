def calculate_price(base_price, tax=0.05, discount=0):
    return base_price + (base_price * tax) - discount
print(calculate_price(100))
print(calculate_price(100, discount = 10))
print(calculate_price(100, tax=0.08,discount=5))

def func(a, b, c=10, d=20):
    return a + b + c + d
print(func(1, 2, 30))