class Quicksort:
    def Partition(self,array,start,end):
        # Assigning last element of the array as pivot
        pivot,pIndex = array[end],array[start]
        i = start
        while i < end:
            if array[i] <= pivot:
                array[i],array[pIndex] = array[pIndex],array[i]
                pIndex+=1
            i+=1
        if pIndex != len(array):
            array[pIndex],array[end] = array[end],array[pIndex]
            print pInde
            return pIndex

    def Quick(self,array,start,end):
        print start,end
        if start < end:
            pIndex = self.Partition(array,start,end)
            print pIndex
            # Left of Pivot
            Quick(array,start,pIndex-1)
            # Right of Pivot
            Quick(array,pIndex+1,end)
        print array

# Main
obj = Quicksort()
lst = [9,7,5,55,1,2,4,5,33,66,6,2,22]
obj.Quick(lst,0,len(lst)-1)
