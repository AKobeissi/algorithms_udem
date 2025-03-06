from Q6 import process_numbers
import os

results = [48,2,42]
passed = 0

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    print("Looking for files in:", script_dir)

    for i in range(1, len(results) + 1):
        filename = os.path.join(script_dir, f"test{i}.txt")
        
        if not os.path.exists(filename):
            print(f"Error: {filename} does not exist.")
            continue
        
        res = process_numbers(filename)
        if res == results[i - 1]:
            passed += 1
            print(f"Test with {filename} passed")
        else:
            print(f"Test with {filename} failed")
            print(f"Expected {results[i-1]}, got {res}")
