from heapq import heappush, heappop, heapify

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i):
        return (i-1)//2

    def insert(self,val):
        heappush(self.heap,val)

    def decreaseKey(self,i,val):
        self.heap[i] = val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]

    def extractMin(self):
        return heappop(self.heap)

    def delete(self,i):
        self.decreaseKey(i,float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

def main():
    heapObj = MinHeap()
    heapObj.insert(3)
    heapObj.insert(2)
    heapObj.delete(1)
    heapObj.insert(15)
    heapObj.insert(5)
    heapObj.insert(4)
    heapObj.insert(45)

    print(heapObj.getMin())
    print(heapObj.extractMin())
    print(heapObj.getMin())

if __name__ == '__main__':
    main()
