# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


def python_heapq(nums: list[int], k: int):
    return heapq.nlargest(k, nums)[-1]


class MyMinHeapq:
    """
    A heapq is a complete binary tree, that is either a max or min heap.
    if it is a max heap - every child is smaller or equal to their parent.
    if it is a min heap - every child is bigger or equal to their parent.

    this order must be maintained during insertion and removal.
    This class implements a min heap complete binary tree for ints
    """

    def __init__(self, max_size: int) -> None:
        self.heap: list[int] = list()
        self.max_size: int = max_size

    def get_root(self) -> int:
        "Return value at root"
        return self.heap[0]

    def push(self, value: int) -> None:
        "Push the value into the heap and maintain order"

        if len(self.heap) < self.max_size:
            # Append to available slot and bubble up
            self.heap.append(value)
            self.bubble_up(len(self.heap) - 1)
        elif self.heap[0] < value:
            # Replace root and bubble down
            self.heap[0] = value
            self.bubble_down(0)

    def bubble_up(self, index: int) -> None:
        "Bubble up the value at index until it is in order"
        # For every item in index i, since the heap is a complete binary tree, its children
        # are at 2i+1 and 2i+2.

        # Accordingly, for every item in index i:
        # if i is even, its parent is in (i-2) / 2
        # if i is odd, its parent is in (i-1) / 2
        while index != 0:
            if index % 2 == 0:
                parent = (index - 2) // 2
            else:
                parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                index = parent  # Must bubble up parent now
            else:
                # Order has been achieved
                return

    def bubble_down(self, index: int) -> None:
        "Bubble down to maintain min-heap property"
        size = len(self.heap)

        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            smallest = index

            # Check if the left child exists and is smaller than current smallest
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check if the right child exists and is smaller than the current smallest
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest  # Continue bubbling down
            else:
                return  # Order has been achieved

    def swap(self, index1: int, index2: int) -> None:
        "Swap between index1 and index2"
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


def my_heapq(nums: list[int], k: int):
    min_heap = MyMinHeapq(k)

    for num in nums:
        min_heap.push(num)

    kth_max = min_heap.get_root()
    return kth_max
