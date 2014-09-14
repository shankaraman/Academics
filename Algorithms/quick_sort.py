class Quicksort:
    def Partition(self,array,start,end):
        # Assigning last element of the array as pivot
        pivot,pIndex,i = array[end],start,start
#        print pivot
        while i < end:
            print i,"<",end
            if array[i] <= pivot:
                print array[i],"<=",pivot
                print "i:",i,"pIndex:",pIndex
#                print "Before swapping:",array[i],array[pIndex]
                array[i],array[pIndex] = array[pIndex],array[i]
#                print "After swapping:",array[i],array[pIndex]
                pIndex+=1
            i+=1
            array[pIndex],array[end] = array[end],array[pIndex]
            return pIndex

    def Quick(self,array,start,end):
        if start < end:
            pIndex = self.Partition(array,start,end)
            print pIndex
            self.Quick(array,start,pIndex-1)
            self.Quick(array,pIndex+1,end)
            print array

# Main
obj = Quicksort()
lst = [7,2,1,6,8,5,3,4]
obj.Quick(lst,0,len(lst)-1)
