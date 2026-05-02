import sympy as sp

# Given digits
W, X, Y, Z = 0, 3, 0, 2

# Step 1: Digital Root
sum_digits = W + X + Y + Z

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

R = digital_root(sum_digits)

print("R (Digital Root):", R)

# Step 2: Define variable
x = sp.symbols('x')

# Step 3: Define function
f = (x**3)/3 - R*(x**2) + (R**2 - 1)*x

print("\nFunction f(x):")
sp.pprint(f)

# Step 4: Differentiate
f_prime = sp.diff(f, x)

print("\nf'(x):")
sp.pprint(f_prime)

# Step 5: Solve f'(x) = 0
critical_points = sp.solve(f_prime, x)

print("\nCritical Points (where behavior changes):")
print(critical_points)

# Step 6: Interpretation
print("\nThese correspond to months:")
for point in critical_points:
    print(f"Month {point}")