import ctypes

class DynamicArray(object):

	def __init__(self):
		self.len = 0
		self.capacity = 1
		self.A = self.make_array(self.capacity)

	def __len__(self):
		return self.len

	def __getitem__(self,index):

		if not 0 <= k <self.n:
			return IndexError('index is out of bounds !')
		return self.A[index]

	def __setitem__(self,index,item):

		if not 0 <= k <self.len:
			# Check it k index is in bounds of array
			return IndexError('K is out of bounds !')
		self.A[index]=item

	def append(self,item):

		if self.len == self.capacity:
			self._resize(2 * self.capacity)

		self.A[self.len] = item
		self.len += 1


	def _resize(self, new_cap):

		B = self.make_array(new_cap)

		for k in range(self.len):
			B[k] = self.A[k]

		self.A = B
		self.capacity = new_cap # Reset the capacity 


	def make_array(self,new_cap):
		return (new_cap * ctypes.py_object)()




arr = DynamicArray()
arr.append(3)

li= [1,2,3]
print(len(li))
del li[-1]
print(len(li))