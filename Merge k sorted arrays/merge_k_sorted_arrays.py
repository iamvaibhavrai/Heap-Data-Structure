temp = []
class MinHeap:
    h_size = 0
    def __init__(self,a,n):
        self.h_size = n

    def extractMin(self):

    def getMin(self):
        global temp
        return temp[0]

    def left(self,i):
        return (2*i)+1

    def right(self,i):
        return (2*i)+2

    def heapify(self,i):
        global temp
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l<self.h_size and temp[l]<temp[i]:
            smallest = l
        if r<self.h_size and temp[r]<temp[smallest]:
            smallest = r
        if smallest != i:
            temp[i],temp[smallest] = temp[smallest],temp[i]
            heapify(smallest)
