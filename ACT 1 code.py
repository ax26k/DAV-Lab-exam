import sympy as sp

# Roll number digits
W, X, Y, Z = 0, 3, 0, 2

# Step 1: Compute digital root R
total = W + X + Y + Z

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

R = digital_root(total)

# Step 2: Define function
x = sp.symbols('x')
f = x**3/3 - R*x**2 + (R**2 - 1)*x

# Step 3: Find derivative
f_prime = sp.diff(f, x)

# Step 4: Solve f'(x) = 0
critical_points = sp.solve(f_prime, x)

print("R =", R)
print("Function f(x):", f)
print("f'(x):", f_prime)
print("Critical Points:", critical_points)