def add_item(item, order=None):

    if order is None:
        order = []

    order.append(item)

    return order


customer1 = add_item("Tea")
customer1 = add_item("Vada", customer1)

customer2 = add_item("Coffee")
customer2 = add_item("Samosa", customer2)

customer3 = add_item("Juice")


print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# Positional parameters

def total(a, b):
    return a + b

print(total(10, 20))


# Keyword parameters

def student(name, age):
    print(name, age)

student(age=16, name="Arun")


# Default parameters

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Arun")


# Returning multiple values

def calculate(a, b):

    total = a + b
    gst = total * 0.18

    return total, gst


amount, tax = calculate(1000, 200)

print("Total:", amount)
print("GST:", tax)


# Global variable

count = 0

def update():

    global count
    count += 1

update()

print("Count:", count)


# Nonlocal variable

def outer():

    x = 10

    def inner():

        nonlocal x
        x = 20

    inner()

    print(x)


outer()