import random

class AlgorithmOfSorting:
    def __init__(self, l_to_sort):
        self.l_to_sort = l_to_sort
    def bubble_sort(self):
        for i in range(len(self.l_to_sort)):
            completion_of_sorting = 0
            for k, k_value in enumerate(self.l_to_sort):
                if  k < len(self.l_to_sort) - 1 and k_value > self.l_to_sort[k + 1]:
                    completion_of_sorting = 1
                    k_temp = k_value
                    self.l_to_sort[k] = self.l_to_sort[k + 1]
                    self.l_to_sort[k + 1] = k_temp
            if completion_of_sorting == 0:
                break