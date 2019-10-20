def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    # new_list = [expression(i) for i in old_list if filter(i)]
    return [i for i in numbers if i > 0 and i % 2 == 0]