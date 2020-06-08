# sorting algorithms
import random
import numpy as np
import matplotlib.pyplot as plt

class Sort():

    def __init__(self):
        self.func_call_count = 0

    def merge_sort(self, a_list):
        self.func_call_count = 0
        sorted_list = self.merge_sort_func(a_list)
        return {'func_call_count': self.func_call_count, 'sorted_list': sorted_list}

    def merge_sort_func(self, a_list):
        len_list = len(a_list)
        mid = len_list // 2
        if self.num_comp(1, len_list):
            aa_list = self.merge_sort_func(a_list[mid:])
            ab_list = self.merge_sort_func(a_list[:mid])

            i = 0
            while (aa_list or ab_list):
                if (len(aa_list) > 0):
                    if (len(ab_list) > 0):
                        if self.num_comp(aa_list[0], ab_list[0]):
                            a_list[i] = aa_list[0]
                            aa_list.pop(0)
                        else:
                            a_list[i] = ab_list[0]
                            ab_list.pop(0)
                    else:
                        a_list[i] = aa_list[0]
                        aa_list.pop(0)
                else:
                    a_list[i] = ab_list[0]
                    ab_list.pop(0)
                i += 1

            return a_list
        else:
            return a_list

    def bubble_sort(self, a_list, mode=0):
        self.func_call_count = 0
        if mode:
            sorted_list = self.bubble_sort_func(a_list)
        else:
            sorted_list = self.bubble_sort_func2(a_list)
        return {'func_call_count': self.func_call_count, 'sorted_list': sorted_list}

    def quick_sort_func(self, a_list, first=None, last=None):
            if first is None:
                first = 0
                last = len(a_list) - 1
            if first < last:
                pivot = self.partition(a_list, first, last)

                self.quick_sort_func(a_list, first, pivot - 1)
                self.quick_sort_func(a_list, pivot + 1, last)

    def partition(self, a_list, first, last):
        pivot = a_list[last]
        i = first - 1
        for j in range(first, last):
            if self.num_comp(a_list[j], pivot):
                i += 1
                a_list[j], a_list[i] = self.num_switch(a_list[j], a_list[i])
        a_list[last], a_list[i + 1] = self.num_switch(a_list[last], a_list[i + 1])
        return i + 1

    def quick_sort(self, a_list):
        self.func_call_count = 0
        self.quick_sort_func(a_list)
        return {'func_call_count': self.func_call_count, 'sorted_list': a_list}

    def bubble_sort_func2(self, a_list):
        for i in range(len(a_list) - 1, 0, -1):
            for j in range(i):
                self.func_call_count += 1
                if a_list[j] > a_list[j+1]:
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
        return a_list

    def bubble_sort_func(self, a_list):
        if len(a_list) > 1:
            for i in range(len(a_list) - 1):
                if self.num_comp(a_list[i+1], a_list[i]):
                    a_list[i + 1], a_list[i] = self.num_switch(a_list[i+1], a_list[i])
            return self.bubble_sort_func(a_list[:-1]) + [a_list[-1]]
        else:
            return a_list

    def num_comp(self, a, b):
        self.func_call_count += 1
        if a < b:
            return True
        else:
            return False

    def num_switch(self, a, b):
        self.func_call_count += 1
        return b, a


sorter = Sort()
# items = [0, 1, 0, 0, 2, 4, 7, 7, 4, 10, 7, 11, 3, 12, 14, 6, 6, 13, 10]
# items = [10, 80, 30, 90, 40, 50, 70]
# sorter.quick_sort(items)
#
# n = 100
# m = 100
# func_call_count_array = np.zeros((m * n, 2))
# func_call_count_array_2 = np.zeros((m * n, 2))
# sorter = Sort()
# j = 0
# for i in range(n):
#     k = 0
#     while (k < m):
#         items = [random.randint(0, k) for k in range(i)]
#         sorted_list = sorter.quick_sort(items)
#         func_call_count_array[j, 0] = i
#         func_call_count_array[j, 1] = sorted_list['func_call_count']
#         sorted_list = sorter.quick_sort(items)
#         func_call_count_array_2[j, 0] = i
#         func_call_count_array_2[j, 1] = sorted_list['func_call_count']
#         j += 1
#         k += 1
# x = func_call_count_array[:, 0]
# y_exp = (func_call_count_array[:, 1])
# y_exp_2 = (func_call_count_array_2[:, 1])
# y_true = x[x != 0] * np.log(x[x != 0])
# # y_true = func_call_count_array[:,0] ** 2
# C = y_exp[x != 0][y_true != 0] / y_true[y_true != 0]
# C = C[~(np.isnan(C) | np.isinf(C))]
# C = C.mean()
# C2 = y_exp_2[x != 0][y_true != 0] / y_true[y_true != 0]
# C2 = C2[~(np.isnan(C2) | np.isinf(C2))]
# C2 = C2.mean()
# # plt.scatter(x, y_exp)
# plt.scatter(x, y_exp_2)
# # plt.scatter(x[x != 0], C * y_true)
# plt.scatter(x[x != 0], C2 * y_true)
# plt.show()
