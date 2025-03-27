#!/usr/bin/env python
#!CMD: ./solve.py
def solve_dragon_flight():
    # Read N and Q
    n, q = map(int, input().split())

    # Read initial wind effects
    wind_effects = list(map(int, input().split()))

    # Process operations
    for _ in range(q):
        op = input().split()

        if op[0] == 'U':
            # Update operation
            i, x = int(op[1]), int(op[2])
            wind_effects[i-1] = x  # Convert to 0-indexed

        elif op[0] == 'Q':
            # Query operation
            l, r = int(op[1]), int(op[2])

            # Convert to 0-indexed
            l, r = l-1, r-1

            # Find maximum subarray sum (Kadane's algorithm)
            max_sum = float('-inf')
            current_sum = 0

            for i in range(l, r+1):
                current_sum = max(wind_effects[i], current_sum + wind_effects[i])
                max_sum = max(max_sum, current_sum)

            print(max_sum)

# Run the solution
if __name__ == "__main__":
    solve_dragon_flight()
