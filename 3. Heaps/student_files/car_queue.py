"""
File: car_queue.py
Author: your name should probably go here

Implements a car queue using a min-d-heap that sorts cars based on their priority.

"""

from classes3 import Car
# from stats import StatCounter, PRIORITY_COMPS  # if you want to use them


class CarHeapQueue():
    """ Implement a queue structure using a 0-indexed d-heap.
        This particular type of queue holds Cars
    """

    def __init__(self, num_children=2, start_data=None, fast=False):
        """ Create the vehicle priority queue that uses
            a d-heap as the underlying data structure.
            num_children = the d factor with the default being 2.
            Your heap should handle any d from 1 onwards.
        """
        self.num_children = num_children
        if start_data is None:
            start_data = []
        self.comparisons = 0
        self._data = []
        if fast:
            self._fast_heapify(start_data)
        else:
            self._heapify(start_data)

    def __len__(self):
        """ Returns the number of items in the heapy queue """
        return len(self._data)

    def __str__(self):
        """ Returns you know what """
        result = '-' * 40 + '\n'
        result += 'CarHeapQueue:\n'
        result += '-' * 40 + '\n'
        if self._data:
            for i, item in enumerate(self._data):
                result += '{}-> {}\n'.format(i, repr(item))
        else:
            result += '  Empty\n'
        result += '-' * 40
        return result
        # return "PQ[{}]".format(", ".join(repr(p) for p in self._data))

    def __repr__(self):
        return "CarHeapQueue([{}])".format(", ".join(repr(car) for car in self._data))

    def _swap(self, i, j):
        """ Swap the cars at indices i and j. """
        # ---start student section---
        pass
        # ===end student section===

    def _index_of_parent(self, index):
        """ Determine the parent index of the current index.
        Return None if index is the root index, ie, 0.
        """
        # ---start student section---
        pass
        # ===end student section===

    def _indices_of_children(self, index):
        """ The child indices for the current index.
            Returns a list containing the indices for all the children
            of the node at the given index.
            Note: Only valid child indices should be returned.
            This will be used by the unit tests so you need to define it.
        """
        # ---start student section---
        pass
        # ===end student section===

    def _index_of_min_child(self, child_indices):
        """ Find the child among the child_indices list that has the lowest priority value.
            Returns the index of the first child with the minimum priority value.
            If an index is not valid, do not consider it.
            If no indices are valid, then return None.
            Assumes the child_indices are in order.
            This method should expect a list such as that generated by _indices_of_children.
        """
        index_of_min = None
        # ---start student section---
        pass
        # ===end student section===
        return index_of_min

    def _sift_up(self, index):
        """ If needed, swap with parent.
            If swapped then continue sifting up from the parent.
            Base case is where there is no parent.
            Don't forget to count any Priority comparisons that are made here.
        """
        # ---start student section---
        pass
        # ===end student section===

    def _sift_down(self, index):
        """ Swap with smallest child if needed
        and sift_down from that child index if swapped.
        Don't forget to count any Priority comparisons that are made here.
        """
        # ---start student section---
        pass
        # ===end student section===

    def _heapify(self, start_data):
        """ Turn the existing data into a heap in O(n log n) time. """
        for car in start_data:
            self.enqueue(car)

    def _fast_heapify(self, data):
        """ Turn the existing data into a heap in O(n) time. """
        # ---start student section---
        pass
        # ===end student section===

    def enqueue(self, car):
        """ Add a car to the queue. """
        # We first make sure that we're only including Cars
        assert isinstance(car, Car)
        # ---start student section---
        pass
        # ===end student section===

    def dequeue(self):
        """ Take the min priority Car off the queue and return the Car object

        Must raise IndexError("Can't dequeue from empty queue!") if the queue is empty.
        """
        # ---start student section---
        pass
        # ===end student section===

    def __contains__(self, plate):
        """ Searches based on plate
        Note: This is a linear search which isn't great.
        The EditableCarHeapQueue will improve on this.
        """
        for car in self._data:
            if car.plate == plate:
                return True
        return False


class EditableCarHeapQueue(CarHeapQueue):
    """ Implement a queue structure using a 0-indexed heap.
        This particular type of queue holds car information.
        Additionally, we can remove cars not at the top of
        the heap in O(log n) time.
    """

    def __init__(self, num_children=2, start_data=None, fast=False):
        self._indices = {}  # plate -> index;

        # Keep track of initial indices for cars
        # if start_data has cars in it
        if start_data is not None:
            for (i, car) in enumerate(start_data):
                self._indices[car.plate] = i
        super().__init__(num_children, start_data, fast)

    def __str__(self):
        """ Returns you know what """
        result = '-' * 40 + '\n'
        result += 'EditableCarHeapQueue:\n'
        result += '-' * 40 + '\n'
        if self._data:
            for i, item in enumerate(self._data):
                result += '{}-> {}\n'.format(i, repr(item))
        else:
            result += '  Empty\n'
        result += '-' * 40
        return result
        # return "PQ[{}]".format(", ".join(repr(p) for p in self._data))

    def __repr__(self):
        return "EditableCarHeapQueue([{}])".format(", ".join(repr(car) for car in self._data))

    def __len__(self):
        """ Returns the number of items in the heapy queue """
        return len(self._data)

    def _swap(self, i, j):
        """ Swap cars at index i and j. Don't forget to change
            their position in self._indices as well!
        """
        # ---start student section---
        pass
        # ===end student section===

    def enqueue(self, car):
        """ Add a car to the queue. Let the superclass do
            most of the work.
        """
        # ---start student section---
        pass
        # ===end student section===

    def dequeue(self):
        """ Remove a car from the front of the queue and return it.
            Again, let the superclass do most of the work.
        """
        # ---start student section---
        pass
        # ===end student section===

    def update(self, updated_car):
        """ Replace the car with the same plate as updated car with the updated car
        and, if needed, do some sifting to return the heap back to a valid state.
        """
        # check that the new_car is a car
        assert isinstance(updated_car, Car)
        # ---start student section---
        pass
        # ===end student section===

    def remove(self, plate):
        """ Removes car with given plate from the queue.
        If the plate isn't in the queue then
            raises the IndexError("Can't remove a plate that isn't in the queue!")
        """
        index = self._indices.get(plate, None)
        if index is not None:
            last = len(self._data) - 1
            if len(self._data) == 1 or index == last:
                self._data.pop()
                self._indices.pop(plate)
            else:
                self._swap(index, last)  # moves plate to remove to end
                self._data.pop()
                self._indices.pop(plate)
                parent = self._index_of_parent(index)
                if parent is not None:
                    self.comparisons += 1
                    if self._data[index].priority < self._data[parent].priority:
                        self._sift_up(index)
                        return
                self._sift_down(index)
        else:
            raise IndexError("Can't remove plate that isn't in the queue!")

    def __contains__(self, plate):
        """ Returns True if a car with the given plate is in the queue,
        otherwise returns False.
        Using the _indices dictionary is the quickest way to do this :)
        """
        return plate in self._indices


# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# NOTE:
# Don't submit any of the test code below to the quiz server
# pylint will cry ;)


def run_simple_car_heap_tests():
    """ Runs some simple tests on a CarHeapQueue
    Students should add more tests, of course!
    """
    queue = CarHeapQueue(
        2)   # binary heap but do try other numbers of children!
    car1 = Car('AAA001', (1000, 2000), 40)
    car2 = Car('AAA002', (1000, 2000), 60)
    car3 = Car('AAA003', (1000, 2000), 50)
    queue.enqueue(car1)
    print(queue)
    queue.enqueue(car2)
    print(queue)
    queue.enqueue(car3)
    print(queue)
    print()
    # uncomment the following when you are ready to test dequeue
    # print('Dequeued ', queue.dequeue())
    # print(queue)
    # print('Dequeued ', queue.dequeue())
    # print(queue)
    # print()
    # print('Dequeued ', queue.dequeue())
    # print(queue)
    # print('Dequeued ', queue.dequeue())  # note this should raise an error
    # print(queue)


def run_test_file_with_fast_enqueue():
    """ Runs a test file with fast enqueue """
    # Note this import will break pylint so don't include this code
    # in your submission to the quiz server
    from utilities import run_heap_tests
    run_heap_tests('./test_data/10-10-20-0-0-a.txt',
                   CarHeapQueue, 2, fast=True)


def run_simple_editable_heap_tests():
    """ Some starter tests, students should add more! """
    print('\n' * 3)
    # binary heap but do try other numbers of children!
    queue = EditableCarHeapQueue(2)
    car1 = Car('AAA001', (1000, 2000), 40)
    car2 = Car('AAA002', (1000, 2000), 60)
    car3 = Car('AAA003', (1000, 2000), 50)
    queue.enqueue(car1)
    queue.enqueue(car2)
    queue.enqueue(car3)
    print(queue)
    print()
    print('Dequeued ', queue.dequeue())
    car4 = Car('AAA003', (2000, 3000), 80)
    queue.update(car4)
    print('Updated', car4)
    print(queue)
    print()
    print('Dequeued ', queue.dequeue())
    print(queue)
    print('Dequeued ', queue.dequeue())
    print(queue)


if __name__ == '__main__':
    run_simple_car_heap_tests()
    # run_simple_editable_heap_tests()
