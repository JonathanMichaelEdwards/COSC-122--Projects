""" Module containing classes and functions for students to complete.
Read the notes with each question in the submission quiz for more
details on what to submit.
The submission quiz will open around a week before the due date
so you can check your code vs. the quiz server's pylint etc.
You should be using your own tests to help you debug your code
and the provided tests.py as final checks that your code works
with bigger data sets. Passing tests.py doesn't necessarily
mean that your code works so make sure you don't rely solely
on those tests...

Author: Jonathan Michael Edwards
Date: 09/24/2018

"""

import doctest
import utilities
from classes2 import NumberPlate
from stats import StatCounter


class ListTable:
    """ This is not really a hashtable.
        It stores (plate, value) tuples in a list.
        It uses a simple linear scan through the whole list
        to find a plate.
        When setting a plate's value it scans through the whole list
        to see if the plate is there first. If it is there it updates
        the plate's value, otherwise it appends a (plate, value) tuple
        to the end of the list.
    """

    def __init__(self, n_slots=0):
        """ Note n_slots is ignored it's there for compatability
        Each (plate, value) record/pair is stored as a tuple.
        Any new records should be simply appended to the data_list.
        The data_list isn't sorted.
        """
        self.data_list = []
        self.n_items = 0
        # NOTE:
        # The following two variables must be updated y your code
        self.n_plate_comparisons = 0   # update whenever number plates are compared
        # update whenever hash(number_plate) is called
        self.n_plate_hashes = 0
        # special note for this class no hashes are ever calculated...
        # the variable is left in for compatability with the testing code.

    def __setitem__(self, plate, value):
        """ Called when mylisttable[plate] = value assignment is used.
        Will update the value for the plate if the plate already in the list
        or will append a new record with (plate, flag) to the end of the list.
        """
        record = (plate, value)
        i = 0
        updated = False
        while i < len(self.data_list) and not updated:
            current_plate, value = self.data_list[i]
            if current_plate == plate:
                self.data_list[i] = record
                updated = True
            i += 1
            self.n_plate_comparisons += 1

        if not updated:
            self.data_list.append(record)
            self.n_items += 1

    def __contains__(self, plate):
        """ Called when doing plate in table expressions.
        Will return True if the plate is in the table, otherwise returns False
        """
        found = False
        i = 0
        while i < len(self.data_list) and not found:
            current_plate, _ = self.data_list[i]
            if current_plate == plate:
                found = True

            i += 1
            self.n_plate_comparisons += 1
            
        return found

    def __getitem__(self, plate):
        """ Returns the value for atable[plate], see examples below.
        """
        found = False
        i = 0
        while i < len(self.data_list) and not found:
            current_plate, current_value = self.data_list[i]
            if current_plate == plate:
                found = True

            i += 1
            self.n_plate_comparisons += 1

        if not found:
            current_value = None
        return current_value

    def items(self):
        """ Generator that yields all the (plate, value) tuples in the table.
            Note the value could be a flag or a list of time stamps, or any other
            thing that you would like to store in the table...
        """
        for record in self.data_list:
            if record:
                yield record

    def keys(self):
        """ Generator that yields all the plates/keys in the table """
        for record in self.data_list:
            if record:
                plate, _ = record
                yield plate

    def __len__(self):
        """ Returns the number of items stored in the hash table """
        return self.n_items

    def __str__(self):
        result = 'List Table:\n'
        for i, value in enumerate(self.data_list):
            result += '{}-> {}\n'.format(i, value)
        return result

    def condensed_str(self):
        """ The list has no gaps so it's already condensed :)
        The only thing different here is the title line...
        """
        result = 'List Table (condensed):\n'
        for i, value in enumerate(self.data_list):
            result += '{}-> {}\n'.format(i, value)
        return result
        
class LinearHashTable:
    """A simple Open Addressing HashTable with Linear Probing.
    Called simply LinearHashTable to make the name shorter...
    """

    def __init__(self, n_slots):
        if n_slots <= 0:
            raise ValueError('Come on! A hashtable needs at least 1 slot!')
        self.n_slots = n_slots
        self.table_list = [None] * n_slots  # make empty hash table
        self.n_items = 0
        # NOTE:
        # The following two variables must be updated by your code
        self.n_plate_comparisons = 0   # update whenever number plates are compared
        # update whenever hash(number_plate) is called
        self.n_plate_hashes = 0

    def __setitem__(self, plate, value):
        """
        Sets the value for the given plate. Basically stores the (plate, value) tuple
        at the appropriate index in the table_list.

        For example, the following will put a (plate, flag) tuple in the appropriate place
        in the table_list:
        my_table[plate] = flag

        Should raise IndexError('Hashtable is full!') if table is full.
        Note: Whilst you cannot add a new plate to a full table, it is still possible
        to update the value for a plate that is already in the table.
        """
        record = (plate, value)
        index = hash(plate) % self.n_slots

        if self.n_slots == self.n_items:
            raise IndexError('Hashtable is full!')

        self.n_plate_hashes += 1  
        while self.table_list[index] is not None:
            self.n_plate_comparisons += 1
            current_plate, _ = self.table_list[index]
            if current_plate == plate:                # Found plate
                self.table_list[index] = record
                return self.table_list
            else:                                     # Find next empty slot
                index += 1
                index %= self.n_slots

        self.table_list[index] = record
        self.n_items += 1

    def __contains__(self, plate):
        """ Returns True if the plate is in the table, otherwise False. """
        index = hash(plate) % self.n_slots

        self.n_plate_hashes += 1
        while self.table_list[index] is not None:
            self.n_plate_comparisons += 1
            current_plate, _ = self.table_list[index]
            if current_plate == plate:                # Found plate
                return True
            else:                                     # Find next empty slot
                index += 1
                index %= self.n_slots

        return False
                

    def __getitem__(self, plate):
        """ Returns the value associated with the given plate
            or None if the plate isn't in the table.
            Note the value could be a flag or a list of time stamps, or any other
            thing that you would like to store in the table...
            
            For example using the following will invoke this method:
            flag = my_linear_hashtable[plate]
        """
        index = hash(plate) % self.n_slots

        self.n_plate_hashes += 1
        while self.table_list[index] is not None:
            self.n_plate_comparisons += 1
            current_plate, current_value = self.table_list[index]
            if current_plate == plate:                # Found plate
                return current_value
            else:                                     # Find next empty slot
                index += 1
                index %= self.n_slots

        return None

    def items(self):
        """ Generator that yields all the (plate, value) tuples in the table.
        Note the value could be a flag or a list of time stamps, or any other
        thing that you would like to store in the table...
        Usage example:
        for key, value in my_table.items():
            print(key, value)
        """
        for record in self.table_list:
            if record:
                yield record

    def keys(self):
        """ Generator that yields all the plates/keys in the table """
        for record in self.table_list:
            if record:
                plate, _ = record
                yield plate

    def __len__(self):
        """ Returns the number of items stored in the table """
        return self.n_items

    def __str__(self):
        """ Returns a nice version of the table with one slot per line """
        result = 'Linear Hash Table:\n'
        for i, slot_record in enumerate(self.table_list):
            result += '{}-> {}\n'.format(i, slot_record)
        return result

    def condensed_str(self):
        """ Similar to the __str__ method by only includes
            slots that are not empty
        """
        result = 'Linear Hash Table (condensed):\n'
        for i, slot_record in enumerate(self.table_list):
            if slot_record:
                result += '{}-> {}\n'.format(i, slot_record)
        return result


class ChainingHashTable:
    """A simple HashTable.
    """

    def __init__(self, n_slots):
        self.n_items = 0  # starts out empty
        if n_slots <= 0:
            raise ValueError('Come on! A hashtable needs at least 1 slot!')
        self.n_slots = n_slots  # must provide the number of slots to be used
        # Note: each slot in the table_list contains the list/chain of items
        # that hash to that index. A simple Python list is used for this.
        self.table_list = [[] for _ in range(n_slots)]
        # The following two variables must be updated by your code
        self.n_plate_comparisons = 0   # update whenever number plates are compared
        # update whenever hash(number_plate) is called
        self.n_plate_hashes = 0

    def __setitem__(self, plate, value):
        """
        Sets the value for the given plate. Basically stores the (plate, value) tuple
        in the list at the appropriate index in the table_list.
        Note the value could be a flag or a list of time stamps, or any other
        thing that you would like to store in the table...
        
        Each slot in the table_list will contain a list of (plate, value) pairs.
        Using this table to store flags would mean the value for each plate would be a flag string.
        Using this table to store timestamps will mean the value for each plate will be a list
        of timestamps.
        For example, the following will put a (plate, timestamps) tuple in the appropriate place
        in the table_list:
        my_table[plate] = timestamps

        Note: Whilst you cannot add a new plate to a full table, it is still possible
        to update the value for a plate that is already in the table.
        """
        found = False
        record = (plate, value)
        index = hash(plate) % self.n_slots
        
        self.n_plate_hashes += 1
        for i, tup in enumerate(self.table_list[index]):
            self.n_plate_comparisons += 1
            if tup[0] == plate:
                self.table_list[index][i] = record
                found = True
 
        if not found:
            self.table_list[index].append(record)
            self.n_items += 1

    def __contains__(self, plate):
        """ Returns True if the plate is in the table, otherwise False. """
        index = hash(plate) % self.n_slots
        
        self.n_plate_hashes += 1
        for _, tup in enumerate(self.table_list[index]):
            self.n_plate_comparisons += 1
            if tup[0] == plate:
                return True
        return False

    def __getitem__(self, plate):
        """ Returns the value associated with the given plate
            or None if the plate isn't in the table.
            For example using the following will invoke this method:
            flag = my_linear_hashtable[plate]
        """
        index = hash(plate) % self.n_slots
        
        self.n_plate_hashes += 1
        for _, tup in enumerate(self.table_list[index]):
            self.n_plate_comparisons += 1
            if tup[0] == plate: 
                return tup[1]
        return None

    def items(self):
        """ Generator that yields all the (plate, value) tuples in the table.
        Note the value could be a flag or a list of time stamps, or any other
        thing that you would like to store in the table...
        Usage example:
        for key, value in my_table.items():
            print(key, value)
        """
        for slot_list in self.table_list:
            if slot_list:
                for record in slot_list:
                    yield record

    def keys(self):
        """ Generator that yields all the plates/keys in the table """
        for slot_list in self.table_list:
            if slot_list:
                for record in slot_list:
                    plate, _ = record
                    yield plate

    def __len__(self):
        """ Returns the number of items stored in the hash table"""
        return self.n_items

    def __str__(self):
        """ Returns a nice version of the table with one slot per line """
        result = 'Chaining Hash Table:\n'
        for i, slot_list in enumerate(self.table_list):
            result += '{}-> {}\n'.format(i, slot_list)
        return result

    def condensed_str(self):
        """ Similar to the __str__ method by only includes slots that are not empty """
        result = 'Chaining Hash Table (condensed):\n'
        for i, slot_list in enumerate(self.table_list):
            if slot_list:
                result += '{}-> {}\n'.format(i, slot_list)
        return result


def make_db_hash_table(database_list, n_slots, table_class=LinearHashTable):
    """ Makes a hash table of the given class from the (plate, flag) tuples
    in the database_list.
    The key used for storing the values should be the number_plate.
    The items from the database list should be added to the table in
    the order that they are given in the database list.
    """
    db_table = table_class(n_slots)
    for data in database_list:
        db_table.__setitem__(data[0], data[1])
    
    return db_table


def process_camera_stream(database_list, sightings, db_table_size, flagged_table_size):
    """
    Makes a LinearHashTable with db_table_size slots and adds all the plates to
    the database with their flags as (plate, flag) tuples. Even plates with
    empty flag strings should be added to the hash database table.

    Then makes a result table that is a ChaingingHashTable with flagged_table_size slots.
    The value stored for each plate with be a tuple containing (plate, list_of_timestamps).
    Then the function scans through the sightings and records the timestamps for flagged plates
    in the results table. NOTE: You only need to record the timestamps for number plates
    that have a flag in the database (ie, their flag is not just '').

    If a plate is already in the result table then the timestamp should be appended to the list
    of times for that plate.
    If a plate isn't aleady in the result table then it should be appended to the
    list of (plate, timestamps) tuples held in the list/chain in the slot that the plate
    hashes to.

    Check out some of the expected_results_table file files to get a feel for how the
    results table should look.
    """
    # make the database table using using your make_db_hash_table function
    db_table = make_db_hash_table(
        database_list, db_table_size, table_class=LinearHashTable)

    # make an empty chaning hash table to put results in
    results_table = ChainingHashTable(flagged_table_size)

    for sighted in sightings:
        if sighted[0] in db_table and db_table[sighted[0]] != '':
            if sighted[0] in results_table:
                results_table[sighted[0]].append(sighted[1])
            else:
                results_table[sighted[0]] = [sighted[1]]
    
    return db_table, results_table

def trial_hash_table(plate_str_list, table):
    for plate_str in ['ABC123', 'DUF721', 'EGG001', 'CSC001', 'ACC101', 'BIG404']:
        x = NumberPlate(plate_str)
        table[x] = 'Stolen' + str(x)
        assert table[x] == 'Stolen' + str(x)
    print(table)
    print()
    print(table.condensed_str())


def run_simple_tests():
    """ A nice place for your testing code """
    filename = './test_data/10s-10000-10-a.txt'
    db_list, sighted_list, matches_list = utilities.read_dataset(filename)
    
    table_db_make = make_db_hash_table(db_list, 10, LinearHashTable)
    table_process = process_camera_stream(db_list, sighted_list, 20, 5)
    
    # i = 0
    # while i < len(db_list):
    #     plate = NumberPlate(str(db_list[i][0]))
    #     table[plate] = db_list[i][1]
    #     i += 1


def example_list_table_stuff():
    table = ListTable()
    plate1 = NumberPlate('ABC123')
    table[plate1] = 'Banana 3'
    plate2 = NumberPlate('BOB456')
    table[plate2] = 'Banana 2'
    plate3 = NumberPlate('JOE234')
    table[plate3] = 'Orange 1'
    table[plate3] = 'Orange 1-update'

    print(plate1 in table)      # translates to table.__contains__(flag)
    print(table[plate3])        # translates to table.__get_item__(plate)
    print(table)


def example_linearhash_stuff():
    """ This example uses a linear hash table to store
    the flags for some number plates, ie, a small
    database of flags for plates.
    """
    plate = NumberPlate('AAA000')
    flag = 'Overdue fines'
    plate2 = NumberPlate('AAA001')
    flag2 = ''
    plate8 = NumberPlate('AAA001')
    flag8 = ''
    plate3 = NumberPlate('AAA002')
    flag3 = 'jonathan'
    plate4 = NumberPlate('AAA003')
    flag4 = 'jo'
    plate5 = NumberPlate('AAA004')
    flag5 = 'jo' 
    plate6 = NumberPlate('AAA004')
    flag6 = 'jo'
    plate7 = NumberPlate('AAA005')
    flag7 = 'jo'

    table = LinearHashTable(6)
    table[plate] = flag        # translates to table.__set_item__(flag)
    table[plate2] = flag2
    table[plate8] = flag8 + '-updated'
    table[plate3] = flag3
    table[plate4] = flag4 
    table[plate5] = flag5 + '-updated'
    table[plate6] = flag6 + '-pass'
    table[plate7] = flag7 + '-completed'

    print(plate in table)      # translates to table.__contains__(flag)
    print(table[plate])        # translates to table.__get_item__(plate)
    print(table)
    


def example_chaining_stuff():
    """ Example use of the chaingin hash table.
    This example uses a chaining hash table to store
    the flags for some number plates, ie, a small
    database of flags for plates.
    """
    plate1 = NumberPlate('BAA754')
    plate2 = NumberPlate('MOO123')
    plate3 = NumberPlate('WOF833')
    plate4 = NumberPlate('EEK001')

    table = ChainingHashTable(5)
    table[plate1] = 'Sheep'
    table[plate2] = 'Cow'
    table[plate3] = 'Dog'
    table[plate4] = 'Mouse'
    table[plate4] = 'Mouse-updated'
    print(table)

    print('plate1 in table:', plate1 in table)
    print('plate2 in table:', plate2 in table)
    print('plate3 in table:', plate3 in table)
    print('plate4 in table:', plate4 in table)
    print()
    print('Value for plate1:', table[plate1])
    print('Value for plate2:', table[plate2])
    print('Value for plate3:', table[plate3])
    print('Value for plate4:', table[plate4])
    print()
    # table[plate1] = 'new_flag'  # update the value for plate 1
    # plate5 = NumberPlate('BBB222')  # add in a new plate
    # table[plate5] = 'BBB222-flag'
    # print(table)
    # print('plate5 (BBB222) in table:', plate5 in table)
    # print('AAA000' in str(table))


if __name__ == '__main__':
    # uncomment the next line to run the ListTable doctests
    # doctest.testmod()

    # various examples for you to run and expand upon
    # run_simple_tests()
    # example_list_table_stuff()
    # example_linearhash_stuff()
    example_chaining_stuff()
