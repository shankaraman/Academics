import random
class Quicksort:
    def Partition(self,array,start,end):
        # Assigning last element of the array as pivot
        pivot,pIndex = array[end],start
        # Push all the elements which are less than pivot to left
        for i in range(start,end):
            if array[i] <= pivot:
                array[i],array[pIndex] = array[pIndex],array[i]
                pIndex+=1
        # Swap the pivot to the appropriate position
        array[pIndex],array[end] = array[end],array[pIndex]
        return pIndex

    def Quick(self,array,start,end):
        if start < end:
            pIndex = self.Partition(array,start,end)
            # Left of Pivot
            self.Quick(array,start,pIndex-1)
            # Right of Pivot
            self.Quick(array,pIndex+1,end)
            return array

# Main
obj = Quicksort()
random_numbers = []
for i in range(1000000):
    random_numbers.append(random.randint(0,i))
#print random_numbers
sorted_lst = obj.Quick(random_numbers,0,len(random_numbers)-1)

#print sorted_lst
