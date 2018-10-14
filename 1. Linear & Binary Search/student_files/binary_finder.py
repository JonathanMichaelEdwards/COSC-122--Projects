"""
Author = Jonathan Edwards
Email = jon.michael.edwards13@gmail.com
"""

def simple_binary_plate_finder(stolen_list, sighted_list):
    """ Takes two lists of NumberPlates, returns a list and an integer.
    You can assume the stolen list will be in ascending order.
    You must assume that the sighted list is unsorted.

    The returned list contains stolen number plates that were sighted,
    in the same order as they appeared in the sighted list.
    The integer is the number of NumberPlate comparisons that
    were made.

    You can assume that each input list contains only unique plates,
    ie, neither list will contain more than one copy of any given plate.
    This fact will be very helpful in some special cases - you should
    think about when you can stop searching.    """
    result_list = []
    total_comparisons = 0 

    for plate in sighted_list:
        comparisons = search(stolen_list, plate, result_list)
        total_comparisons += comparisons

    return result_list, total_comparisons


def search(stolen_list, sighted, result_list):
    """
    Takes 2 Inputs list inputs and a int value.
    Loops throgh all of the stolen_list items and 
    and trys to match it with the sighted value.
    Keeps comparing values with a counter until match
    is made and returns the number of comparisons made
    and the result list.
     
    Values in the stolen list are divided by half each time
    until nothing left to divide.
    returns comparisons complexity O(log n)  
    """
    comparisons = 0
    lower_bound = 0
    upper_bound = len(stolen_list)-1
     
    index = (lower_bound + upper_bound) // 2
    while lower_bound < upper_bound:
        comparisons += 1
        if stolen_list[index] < sighted:
            lower_bound = index + 1
        else:
            upper_bound = index  
        
        index = (lower_bound + upper_bound) // 2
    
    comparisons += 1   
    if stolen_list[index] == sighted: 
        result_list.append(stolen_list[index])

    return comparisons


# ------------------------------------------------
# Extra stuff for your personal testing regime
# You can leave this stuff out of your submission


def run_tests():
    """ Use this function to run some simple tests 
    to help with developing your awesome answer code.
    You should leave this out of your submission """
    from utilities import read_dataset
    file_name = './test_data/0s-5-0-a.txt'
    stolen_list, sighted_list, matches = read_dataset(file_name)

    result_list = []
    total_comparisons = 0 

    for plate in sighted_list:
        comparisons = search(stolen_list, plate, result_list)
        total_comparisons += comparisons

    return result_list, total_comparisons


if __name__ == '__main__':
    # This won't run when your module is imported from.
    # Use run_tests to try out some of your own simple tests.

    print(run_tests())