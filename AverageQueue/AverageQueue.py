from Queue import Queue

class AverageQueue(Queue):
    def __init__(self, elements = []):
	Queue.__init__(self, elements)
	self._sum = float(self.__get_sum())
	self._size = float(self.__get_size())

    def __str__(self):
	return str(self._elements)

    def __get_sum(self):
	return sum(self._elements)

    def __get_size(self):
	return len(self._elements)

    def avg_push(self, value):
	self.push(value)
	self._sum += value
	self._size += 1

    def avg_pop(self):
	value = self.pop()
	self._sum -= value
	self._size -= 1

    def get_avg(self):
	if(self._size == 0):
	    return 0
	return self._sum / self._size

