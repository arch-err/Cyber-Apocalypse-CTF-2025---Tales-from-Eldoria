# Define the prime p
p = 21214334341047589034959795830530169972304000967355896041112297190770972306665257150126981587914335537556050020788061
# Define the coefficients a and b
a = 408179155510362278173926919850986501979230710105776636663982077437889191180248733396157541580929479690947601351140
b = 8133402404274856939573884604662224089841681915139687661374894548183248327840533912259514444213329514848143976390134

# Create the finite field F_p
F = GF(p)

# Define the elliptic curve E over F_p
E = EllipticCurve(F, [a, b])

# Compute the number of points over F_p
N_p = E.cardinality()

# Now compute the order over F_{p^3}
# Create the finite field F_{p^3}
F_p3 = GF(p^3)

# Define the elliptic curve E over F_{p^3}
E_p3 = EllipticCurve(F_p3, [a, b])

# Compute the number of points over F_{p^3}
N_p3 = E_p3.cardinality()

# Print the results
print("Order of the elliptic curve over F_p:", N_p)
print("Order of the elliptic curve over F_{p^3}:", N_p3)

# Factor the order over F_{p^3}
factorization = factor(N_p3)
print("Factorization of the order over F_{p^3}:", factorization)
