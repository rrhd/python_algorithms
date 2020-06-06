# sorting algorithms
class Sort():

    def __init__(self):
        self.func_call_count = 0

    def bubble_sort(self, a_list, mode=0):
        self.func_call_count = 0
        if mode:
            sorted_list = self.bubble_sort_func(a_list)
        else:
            sorted_list = self.bubble_sort_func2(a_list)
        return {'func_call_count': self.func_call_count, 'sorted_list': sorted_list}


    def bubble_sort_func(self, a_list):
        if len(a_list) > 1:
            for i in range(len(a_list) - 1):
                if self.num_comp(a_list[i+1], a_list[i]):
                    a_list[i + 1], a_list[i] = self.num_switch(a_list[i+1], a_list[i])
            return self.bubble_sort_func(a_list[:-1]) + [a_list[-1]]
        else:
            return a_list

    def bubble_sort_func2(self, a_list):
        for i in range(len(a_list) - 1, 0, -1):
            for j in range(i):
                self.func_call_count += 1
                if a_list[j] > a_list[j+1]:
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
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
sorted_list = sorter.bubble_sort([4, 3, 2, 1])

