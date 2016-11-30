# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_elements(input_list):

    if type(input_list) is not list:
        raise TypeError('The parameter is not a list!')

    result_list = []

    for i in input_list:
        result_list.append(i * 2)
    return result_list

print(double_elements([1, 2, 3, 4, 5]))
