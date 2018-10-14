"""
Author = Jonathan Edwards
Email = jon.michael.edwards13@gmail.com
"""


def simple_linear_plate_finder(stolen_list, sighted_list):
    """
    Takes two lists of NumberPlates as input. 
    Checks to see whether result from search 
    is not null which means we've found a value,
    therefore go to next sighting by breking out
    of current list. 
    Returns a list and an integer.
    """
    result_list = []
    total_comparisons = 0

    for plate in sighted_list:
        comparisons = search(stolen_list, plate, result_list)
        total_comparisons += comparisons

        if len(result_list) == len(stolen_list):
            break

    return result_list, total_comparisons


def search(stolen_list, sighted, result_list):
    """
    Takes 2 Inputs list inputs and a int value.
    Loops throgh all of the stolen_list items and 
    and trys to match it with the sighted value.
    Keeps comparing values with a counter until match
    is made and returns the number of comparisons made
    and the result list. 
    
    If we go through all of the
    values in the stolen list and dont find a match,
    return comparisons complexity O(n) and None.  
    """
    stolen_length = []
    comparisons = 0
    
    for i in range(len(stolen_list)):
        stolen_length.append(stolen_list[i])
        
        if stolen_list[i] == sighted:
            result_list.append(sighted)
            comparisons += i+1
            return comparisons
    
    comparisons += len(stolen_length)
    return comparisons


# ------------------------------------------------
# Extra stuff for your personal testing regime
# You can leave this stuff out of your submission


def run_tests():
    """ Use this function to run some simple tests 
    to help with developing your awesome answer code.
    You should leave this out of your submission """
    from utilities import read_dataset
    file_name = './test_data/0-0-0-a.txt'
    stolen_list, sighted_list, matches = read_dataset(file_name)

    result_list = []
    total_comparisons = 0

    for plate in sighted_list:
        comparisons = search(stolen_list, plate, result_list)
        total_comparisons += comparisons
        if len(result_list) == len(stolen_list):
            break

    return result_list, total_comparisons
    

# You can leave the following out of your submission
if __name__ == '__main__':
    # This won't run when your module is imported by the tests module.
    # Use run_tests to try out some of your own simple tests.
    print(run_tests())