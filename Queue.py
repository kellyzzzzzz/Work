class Queue:
    def __init__(self, elements = []):
	self._elements = elements

    def pop(self):
	if(self.__size == 0):
	    return None

	return self._elements.pop(0)

    def front(self):
	if(self.__size == 0):
	    return None

	return self._elements[0]

    def push(self, entry):
	self._elements.append(entry)

    def __size(self):
	return len(self._elements)
