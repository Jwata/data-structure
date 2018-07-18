"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    
    start = 0
    end = len(input_array)-1
    
    step = 0
    while end > start:
        step += 1
        target_index = (end + start) // 2
        print('Step {}: Start {} End {} Center {}'.format(step, start, end, target_index))

        if value == input_array[target_index]:
            return target_index
        elif value == input_array[target_index+1]:
            return target_index+1 
        elif value < input_array[target_index]:
            end = target_index
        elif value > input_array[target_index+1]:
            start = target_index+1
        else:
            return -1

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)# 