# Nom(s) étudiant(s) / Name(s) of student(s): Amine Kobeissi, Arvind Nair

import sys

# Espace pour fonctions auxillaires :
# Space for auxilary functions :
def get_element(arr, idx, default_val):
    """
    Helper function to get element from an array with a default value.
    """
    if 0 <= idx < len(arr):
        return arr[idx]
    return default_val

# Fonction à compléter / function to complete:
def solve(list1, list2):
    """
    Find the median of two sorted lists using binary search.
    
    Key insight: The median divides the combined array into two equal halves.
    We can find this division by finding the right partition in both lists.
    
    Time complexity: O(log(min(n+m))) where n and m are lengths of the lists
    
    Args:
        list1: First sorted list
        list2: Second sorted list
    
    Returns:
        The median value of the combined lists
    """
    # Ensure list1 is the smaller array for more efficient binary search
    # Binary search on the smaller array reduces worst-case iterations
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    
    # Get dimensions of both arrays
    n, m = len(list1), len(list2)
    total_elements = n + m
    mid_idx = total_elements // 2
    
    # Edge case: if first array is empty
    if n == 0:
        if total_elements % 2 == 1:  # Odd number of elements
            return list2[mid_idx]
        else:  # Even number of elements
            return (list2[mid_idx-1] + list2[mid_idx]) / 2
    
    # Binary search on smaller array
    # Search range is [0, n] including n because we might need to place the partition after the last element of list1
    left, right = 0, n
    
    while left <= right:
        # Partition the smaller array - the number of elements to take from list1
        partition_x = (left + right) // 2
        
        # Calculate partition for larger array 
        partition_y = (total_elements + 1) // 2 - partition_x
        
        # These represent the elements around the partition point
        x_left = get_element(list1, partition_x - 1, float('-inf'))  # Last element in left part of list1
        x_right = get_element(list1, partition_x, float('inf'))      # First element in right part of list1
        y_left = get_element(list2, partition_y - 1, float('-inf'))  # Last element in left part of list2
        y_right = get_element(list2, partition_y, float('inf'))      # First element in right part of list2
        
        # The correct partition ensures all elements on the left side are <= all elements on the right side
        if x_left <= y_right and y_left <= x_right:
            # For odd number of elements
            if total_elements % 2 == 1:
                return max(x_left, y_left)
            
            # For even number of elements
            else:
                return (max(x_left, y_left) + min(x_right, y_right)) / 2
        
        # If partition is incorrect, adjust the search range
        elif x_left > y_right:
            # If x_left > y_right, elements in list1's left side are too large
            # So move partition to the left in list1
            right = partition_x - 1
        else:
            # If y_left > x_right, elements in list2's left side are too large
            # So move partition to the right in list1 (and consequently left in list2)
            left = partition_x + 1   

def _find_median_linear(list1, list2):
    """
    Find the median of two sorted arrays with O(n+m) time complexity.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
    
    Returns:
        Median value of the combined arrays
    """
    merged = []
    i, j = 0, 0
    
    # Merge the two sorted arrays with a while loop
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    # Calculate median
    n = len(merged)
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        return merged[n//2]

def _find_median_simple(list1, list2):
    """
    Find the median of two sorted arrays with O((n+m)log(n+m)) time complexity.
    
    Args:
        list1: First sorted array
        list2: Second sorted array
    
    Returns:
        Median value of the combined arrays
    """
    merged_list = list1 + list2
    merged_list.sort()  # O((n+m)log(n+m))
    
    n = len(merged_list)
    if n % 2 == 0: # Even number of elements
        return (merged_list[n//2 - 1] + merged_list[n//2]) / 2 # Average of two middle elements to find median
    else: # Odd number of elements
        return merged_list[n//2] # Middle element is the median


# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

# Ne pas modifier le code ci-dessous :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            lines = f.readlines() 
            l0 = list(map(int, lines[0].split()))    
            l1 = list(map(int, lines[1].split()))    

        return solve(l0,l1)
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Q6.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()