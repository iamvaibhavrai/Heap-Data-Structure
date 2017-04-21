temp = []
class MinHeap:
    h_size = 0
    def __init__(self,a,n):
        self.h_size = n
        i = (self.h_size-1)//2
        while i>0:
            self.minHeapify(i)
            i -= 1

    def minHeapify(self,i):
        global temp
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l<self.h_size and temp[l] < temp[i]:
            smallest = l
        if r<self.h_size and temp[r] < temp[smallest]:
            smallest = r
        if smallest != i:
            temp[i],temp[smallest] = temp[smallest],temp[i]
            self.minHeapify(smallest)

    def left(self,i):
        return (2*i) + 1

    def right(self,i):
        return (2*i) + 2

    def extractMin(self):
        global temp
        root = temp[0]
        if self.h_size > 1:
            temp[0] = temp[self.h_size-1]
            self.h_size -= 1
            self.minHeapify(0)
        return root

    def replaceMin(self,x):
        global temp
        root = temp[0]
        temp[0] = x
        if root<x:
            self.minHeapify(0)
        return root

def sort(a,n,k):
    global temp
    temp = [0]*(k+1)
    for i in range(n):
        if i<=k:
            temp[i] = a[i]
        else:
            break
    minHeapObj = MinHeap(temp,k+1)
    i = k+1
    for j in range(n):
        if i<n:
            a[j] = minHeapObj.replaceMin(a[i])
        else:
            a[j] = minHeapObj.extractMin()
        i += 1

def main():
    k = 3
    a = [2,6,3,12,56,8]
    n = len(a)
    sort(a,n,k)
    print(a)

if __name__ == '__main__':
    main()
