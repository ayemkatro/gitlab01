print("Hello, world!")
print("My", "name", "is", "Monty", "Python.", sep="-")
print()
print(0o123)
print(0x123)
print(3e8)
print(0.0000000000000000000001)
print('I\'m Monty Python.')



x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

z=type(y)
print(z)


#var = 3
#print("anak gw", var)
#print("anak gw {0}".format(var))
#print("anak gw" + var)


# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of a square root.
print("c =", c)

