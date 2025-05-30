def tuple_average(t):
    """Calculate the average of elements in a tuple."""
    if len(t) == 0:
        return None  # Return None if the tuple is empty to avoid division by zero
    return sum(t) / len(t)

# Example tuple
numbers = (10, 20, 30, 40, 50)
avg = tuple_average(numbers)

print(f"The average of the tuple {numbers} is {avg}")
