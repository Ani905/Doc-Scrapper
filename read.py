import os, sys 

class MaxHeap:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [None] * (self.maxsize + 1)
		self.Heap[0] = [None, -float("inf")]
		self.FRONT = 1

	def parent(self, pos):
		
		return pos // 2


	def leftChild(self, pos):
		
		return 2 * pos


	def rightChild(self, pos):
		
		return (2 * pos) + 1


	def isLeaf(self, pos):
		
		if pos >= (self.size//2) and pos <= self.size:
			return True
		return False

	
	def swap(self, fpos, spos):
		
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], 
											self.Heap[fpos])

	
	def maxHeapify(self, pos):

		if not self.isLeaf(pos):
			if (self.Heap[pos][1] < self.Heap[self.leftChild(pos)][1] or
				self.Heap[pos][1] < self.Heap[self.rightChild(pos)][1]):


				if (self.Heap[self.leftChild(pos)][1] > 
					self.Heap[self.rightChild(pos)][1]):
					self.swap(pos, self.leftChild(pos))
					self.maxHeapify(self.leftChild(pos))

				else:
					self.swap(pos, self.rightChild(pos))
					self.maxHeapify(self.rightChild(pos))


	def insert(self, element):
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = element
		current = self.size

		while self.Heap[current][1] > self.Heap[self.parent(current)][1]:
			self.swap(current, self.parent(current))
			current = self.parent(current)
        


	def Print(self):
		
		for i in range(1, (self.size // 2) + 1):
			print("PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " + str(self.Heap[2 * i]) + " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))


	def extractMax(self):

		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.maxHeapify(self.FRONT)
		
		return popped
	
	def removeMax(self):
		if self.size == 0:
			return None
		root = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1

		self.maxHeapify(self.FRONT)

		return root
       

path = r"/Users/anirudhan.s/Projects/ADS package/Docs"

os.chdir(path) 

maxHeap = MaxHeap(25)
def read_text_file(file_path, keyword="crypt"):
    global maxHeap
    with open(file_path, 'r') as f:
        text = f.read()
        prio = search(keyword, text, (10**9)+7)
        maxHeap.insert([os.path.basename(file_path), prio])

		
d = 256

def search(pat, txt, q): #Rabin Karp
	pat = pat.lower()
	txt = txt.lower()
	global d
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 
	t = 0 
	h = 1
	count = 0

	for i in range(M-1):
		h = (h*d) % q

	for i in range(M):
		p = (d*p + ord(pat[i])) % q
		t = (d*t + ord(txt[i])) % q

	for i in range(N-M+1):
		if p == t:
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else:
					j += 1

			if j == M:
				count += 1

		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

			if t < 0:
				t = t+q
	return count
		
#main
keyword = input("Enter keyword to be searched: ")
keyword = keyword.lower()
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = os.path.join(path, file)
        read_text_file(file_path, keyword)

# print('The maxHeap is ')
# maxHeap.Print()
#print("The Max val is " + str(maxHeap.extractMax()))

for i in range(5):
	print(maxHeap.removeMax()[0])