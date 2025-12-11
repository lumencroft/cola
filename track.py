import pandas as pd

def collatz_odd_path(n):
    """Generates the sequence of odd numbers in the Collatz path for n, stopping at 1."""
    path = []
    MAX_STEPS = 100000
    steps = 0
    
    while n != 1 and steps < MAX_STEPS:
        if n % 2 != 0:
            path.append(n)
            n = 3 * n + 1
        else:
            n //= 2
        steps += 1
    
    if n == 1:
        # Append the final 1 for consistency if it converged
        path.append(1)
        return path
    else:
        # Return empty list if it didn't converge to 1 within max steps
        return []

# Set the maximum odd number to test
N_MAX = 1000000
# Only test odd numbers greater than 1
odd_numbers = [n for n in range(3, N_MAX + 1) if n % 2 != 0]

total_tested = len(odd_numbers)

# Counters for the paths: keeping 5, 85, and adding 341 (4*85 + 1)
count_through_5 = 0
count_through_85 = 0
count_through_341 = 0

# Test the paths
for n in odd_numbers:
    path = collatz_odd_path(n)
    if not path:
        continue

    # Check if the number goes through the specified node on its way to 1.
    if 23 in path:
        count_through_5 += 1
    if 11 in path:
        count_through_85 += 1
    if 213 in path:
        count_through_341 += 1

# Calculate ratios relative to the total number of odd numbers tested
ratio_5 = count_through_5 / total_tested
ratio_85 = count_through_85 / total_tested
ratio_341 = count_through_341 / total_tested

# Combine results into a DataFrame
results = pd.DataFrame({
    'Path': ['5 (V5 subset)', '85 (V85 subset)', '341 (V341 subset)'],
    'Count (N <= 10000)': [count_through_5, count_through_85, count_through_341],
    'Ratio (Approx. Density)': [ratio_5, ratio_85, ratio_341]
})

print(results.to_markdown(index=False))