#!/usr/bin/env python

import math
from sympy import mod_inverse


def elliptic_curve_order(a, b, p):
    """Compute the order of the elliptic curve y² = x³ + a x + b over F_p."""

    def is_point_on_curve(x, y):
        return (y * y) % p == (x**3 + a * x + b) % p

    def point_add(P, Q):
        if P == (0, 0):
            return Q
        if Q == (0, 0):
            return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and (y1 + y2) % p == 0:
            return (0, 0)  # Point at infinity
        if P == Q:
            m = (3 * x1 * x1 + a) * mod_inverse(2 * y1, p) % p
        else:
            m = (y2 - y1) * mod_inverse(x2 - x1, p) % p
        x3 = (m * m - x1 - x2) % p
        y3 = (m * (x1 - x3) - y1) % p
        return (x3, y3)

    def point_mul(k, P):
        R = (0, 0)  # Identity (point at infinity)
        while k > 0:
            if k % 2 == 1:
                R = point_add(R, P)
            P = point_add(P, P)
            k = k // 2
        return R

    # Find a point on the curve (brute-force)
    P = None
    for x in range(p):
        y_sq = (x**3 + a * x + b) % p
        # Check if y_sq is a quadratic residue
        if pow(y_sq, (p - 1) // 2, p) == 1:
            y = pow(y_sq, (p + 1) // 4, p)  # Works if p ≡ 3 mod 4
            P = (x, y)
            break
    if not P:
        return p + 1  # Trivial case (no points except infinity)

    # Hasse bounds
    lower = p + 1 - 2 * int(math.isqrt(p))
    upper = p + 1 + 2 * int(math.isqrt(p))

    # Baby-step Giant-step to find N in [lower, upper]
    m = int(math.isqrt(upper - lower)) + 1
    table = {}
    for j in range(m):
        Q = point_mul(j, P)
        table[Q] = j

    for i in range(m):
        k = lower + i * m
        Q = point_mul(upper - k, P)
        if Q in table:
            j = table[Q]
            N = upper - (i * m + j)
            return N

    return p + 1  # Fallback (should not happen for valid curves)


# Example usage (replace p, a, b with your values)
p = 12367421061176848768684533636337012942827498222925115102470375051908167461970749519894302227559427687524022981597290
a = 408179155510362278173926919850986501979230710105776636663982077437889191180248733396157541580929479690947601351140
b = 8133402404274856939573884604662224089841681915139687661374894548183248327840533912259514444213329514848143976390134

order = elliptic_curve_order(a, b, p)
print("Order of the curve:", order)
