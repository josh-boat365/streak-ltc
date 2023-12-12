def is_streak(a, b):
    # Function to check if the set of numbers in b forms a streak in array a
    a_set = set(a)
    sorted(b)
    # Check if all numbers in b are present in a
    if not all(num in a_set for num in b):
        return False
    # Find the index of the first element of b in a
    start_index = a.index(b[0])
    
    # Create a circular array based on array a
    circular_a = a + a #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Check if b forms a streak starting from start_index in circular_a
    for i in range(len(b)):
        if circular_a[start_index + i] != b[i]:
            return False
    
    return True

# Example usage:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [ 7,8,0,9,1] # 0,1,7,8,9
c = [9,0,1,2,3] #1,2,3,4,5
d = [2,3,6,5,7]
e = [0,2,8,7,9]

# Check if b and c form a streak in array a
is_b_streak = is_streak(a, b)
is_c_streak = is_streak(a, c)
is_d_streak = is_streak(a, d)
is_e_streak = is_streak(a, e)

print(f"b isStreak: {is_b_streak}")  # Output: b isStreak: True
print(f"c isStreak: {is_c_streak}")  # Output: c isStreak: True
print(f"d isStreak: {is_d_streak}")  # Output: c isStreak: True
print(f"e isStreak: {is_e_streak}")  # Output: c isStreak: True
