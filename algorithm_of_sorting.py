class SortingAlgorithms:
    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
            if not swapped:
                break
        return self.arr