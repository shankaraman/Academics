import random,math
class HEAP:
    def heapify(self,array,i):
        left, right,n = 2*i, 2*i+1, len(array)
        if left <= n and array[left] > array[i]:
            maxm = left
        else:
            maxm = i
        if right <= n and a[right] > a[maxm]:
            maxm = right
        if maxm != 1:
            array[i],array[maxm] = array[maxm],array[i]
            self.heapify(array,maxm)

    def buildheap(self,array):
        i = int(math.floor(len(array)/2))
        while i > 1:
            self.heapify(array,i)

    def heapsort(self,array):
        self.buildheap(array)
        n,i = len(array)-1,n
        while i > 0:
            array[1],array[i] = array[i],array[1]
            n-=1
            self.heapify(array,1)
            i-=1

# Main
obj = HEAP()
random_numbers = [7,2,5,8,1,4,6,0]
obj.heapsort(random_numbers)
