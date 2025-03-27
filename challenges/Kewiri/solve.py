#!/usr/bin/env python
#!CMD: ./solve.py
from pwn import *

# from sympy import factorint


def is_generator(g, p, factors):
    """Check if g is a generator of F_p^* given the factorization of p-1."""
    if g == 0:
        return False
    # Check g^( (p-1)/q ) != 1 mod p for each prime factor q of p-1
    p_minus_1 = p - 1
    for q, _ in factors:
        exponent = p_minus_1 // q
        if pow(g, exponent, p) == 1:
            return False
    return True


p = remote("83.136.251.145", 55915)

p.recvuntil(b"p = ")

prime_p = int(p.recvuntil(b"\n").strip())
# print(prime_p)
prime_p_ans = prime_p.bit_length()

p.sendline(str(prime_p_ans).encode())

# order = 21214334341047589034959795830530169972304000967355896041112297190770972306665257150126981587914335537556050020788060
# factors = factorint(order)

# factorization = "_".join(f"{p},{e}" for p, e in sorted(factors.items()))
# print(factorization)
factorization = "2,2_5,1_635599,1_2533393,1_4122411947,1_175521834973,1_206740999513,1_1994957217983,1_215264178543783483824207,1_10254137552818335844980930258636403,1"
p_minus_1_factors = [
    (2, 2),
    (5, 1),
    (635599, 1),
    (2533393, 1),
    (4122411947, 1),
    (175521834973, 1),
    (206740999513, 1),
    (1994957217983, 1),
    (215264178543783483824207, 1),
    (10254137552818335844980930258636403, 1),
]

p.sendline(factorization.encode())


# p_minus_1_factors = [2, 5, 635599, 2533393, 4122411947, 175521834973, 206740999513, 1994957217983, 215264178543783483824207, 10254137552818335844980930258636403]

# def parse_factors(factor_str):
#     """Parse the factorization string into a list of (prime, exponent) tuples."""
#     factors = []
#     for part in factor_str.split("_"):
#         if not part:
#             continue
#         prime, exp = map(int, part.split(","))
#         factors.append((prime, exp))
#     return factors
# print(parse_factors(factorization))

p.recvuntil(b"0.\n")
g = p.recvuntil(b"?")
g = int(g[:-1])
# print(g)
ans_3 = int(is_generator(g, prime_p, p_minus_1_factors))
ans_3 = str(ans_3).encode()
# print(ans_3)
p.sendline(ans_3)

for i in range(16):
    # print(i)
    p.recvuntil(b"> ")
    g = p.recvuntil(b"?")
    g = int(g[:-1])
    # print(g)
    ans_3 = int(is_generator(g, prime_p, p_minus_1_factors))
    ans_3 = str(ans_3).encode()
    # print(ans_3)
    p.sendline(ans_3)

p.sendline(
    b"21214334341047589034959795830530169972304000967355896041112297190770972306665257150126981587914335537556050020788061"
)

p.sendline(
    b"21214334341047589034959795830530169972304000967355896041112297190770972306665257150126981587914335537556050020788061,4"
)

print(p.recvall().decode())


p.interactive()
# p.interactive()


## Step 4
# a = 408179155510362278173926919850986501979230710105776636663982077437889191180248733396157541580929479690947601351140
# b = 8133402404274856939573884604662224089841681915139687661374894548183248327840533912259514444213329514848143976390134
