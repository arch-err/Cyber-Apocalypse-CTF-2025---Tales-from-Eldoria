def max_energy(tokens):
    # Edge case: empty list
    if not tokens:
        return 0

    # Edge case: single token
    if len(tokens) == 1:
        return tokens[0]

    # Initialize variables to store the last two results
    prev = tokens[0]  # dp[0]
    curr = max(tokens[0], tokens[1])  # dp[1]

    # Iterate through the tokens starting from index 2
    for i in range(2, len(tokens)):
        # Calculate the maximum energy for the current token
        new_curr = max(curr, tokens[i] + prev)
        # Update prev and curr for the next iteration
        prev, curr = curr, new_curr

    # The final result is stored in curr
    return curr

print(max_energy(""))
