# Nom(s) étudiant(s) / Name(s) of student(s): Amine Kobeissi, Arvind Nair

import sys
from collections import Counter

# Espace pour fonctions auxillaires :
# Space for auxilary functions :
def find_median(nums):
    """
    Calculate the median of a sorted list of numbers.
    
    Args:
        numbers: A sorted list of integers
    
    Returns:
        The median value
    """
    n = len(nums)
    if n % 2 == 0:  # Even length
        return (nums[n//2 - 1] + nums[n//2]) / 2
    else:  # Odd length
        return nums[n//2]

# Fonction à compléter / function to complete:
def solve(nums):
    """
    Find the number of distinct pairs in the array that sum to the median.
    
    Time complexity: O(n) where n is the length of the numbers list
    
    Args:
        nums: A sorted list of integers representing exam scores
    
    Returns:
        A list of distinct pairs whose sum equals the median
    """
    # Edge case: need at least 2 elements to form a pair
    if len(nums) < 2:
        return []
    
    # Find the median of the sorted list
    median = find_median(nums)
    
    # Count frequencies of each number
    freq = Counter(nums)
    
    # Store distinct pairs that sum to median
    pairs = []
    visited = set()
    
    # Iterate through unique numbers in the list
    for num in freq:
        complement = median - num
        
        # Skip if we already processed this pair
        if num in visited or complement in visited:
            continue
            
        # Case 1: When num equals median/2 (we need at least 2 occurrences)
        if num == complement:
            if freq[num] >= 2:
                pairs.append((num, num))
                visited.add(num)
        # Case 2: When we have a distinct pair
        elif complement in freq:
            pairs.append((min(num, complement), max(num, complement)))
            visited.add(num)
            visited.add(complement)
    
    return pairs

# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            content = f.read()
        
        # Convert content into a list of integers
        numbers = list(map(int, content.split()))

        pairs = solve(numbers)

        return(len(pairs))

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q3.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()