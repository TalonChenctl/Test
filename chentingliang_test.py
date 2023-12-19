class NDimensionalArray:
    def __init__(self, dimensions,default_value=0):
        self.dimensions = dimensions
        self.default=default_value    #数组初始化的默认值
        self.array = self.create_array(dimensions)

    def create_array(self, dimensions, level=0):    #时间复杂度取决于n的维度
        if level == len(dimensions):
            return self.default
        return [self.create_array(dimensions, level + 1) for i in range(dimensions[level])]

    def set_value(self, indices, value):     #赋值功能
        array = self.array
        for index in indices[:-1]:
            array = array[index]
        array[indices[-1]] = value

    def get_value(self, indices):   #index功能
        array = self.array
        for index in indices:
            array = array[index]
        return array

    def iterator(self, start_index):
        return NDArrayIterator(self, start_index)

class NDArrayIterator:
    def __init__(self, nd_array, start_index):
        self.nd_array = nd_array
        self.current_indices = list(start_index)
        self.done = False

    def _increment_indices(self):
        for i in reversed(range(len(self.current_indices))):
            self.current_indices[i] += 1
            if self.current_indices[i] < self.nd_array.dimensions[i]:
                return
            self.current_indices[i] = 0
            if i == 0:
                self.done = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration
        value = self.nd_array.get_value(tuple(self.current_indices))
        self._increment_indices()
        return value

#例子
dimensions = [3, 3, 2]
nd_array = NDimensionalArray(dimensions,1)
start_index = (0, 0, 1)  

exp = nd_array.iterator(start_index)
for value in exp:
    print(value)
