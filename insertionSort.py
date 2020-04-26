#From book: A common sense guide to data structures and algorithms, by Jay Wengrow
# Insertion Sort Algorithm. Time Complexity: O(n^2) Quadratic

def insertion_sort(array):

    for index in range(1, len(array)):  # Start loop at index 1 that runs through entire array. Current idx is kept in variable index

        position = index            # Marks the position at whatever index currently is
        temp_value = array[index]   # Assigns value at the index to the temp value

        while position > 0 and array[position - 1] > temp_value:    # Checks whether the value to the left of position is greater than the temp value
            array[position] = array[position - 1]                   # If it is, we shift that value to the right
            position = position - 1                                 # And we decrement the position by 1

        array[position] = temp_value    # Drop the temp value into the gap in the array

    return array


#
array = [2, 3, 10, 5, 1]
print_statement = "Before Sort: {} \nAfter Sort: {}".format(array, insertion_sort(array))

print(print_statement)
