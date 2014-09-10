class SDES:
    # Makes all the left circular operations
    def SDES_shift(self,string,key):
        left,right = string[:len(string)/2],string[len(string)/2:]
        if key == 1:
            left = left[1:]+left[:1]
            right = right[1:]+left[:1]
        else: # key = 2
            left = left[2:]+left[:2]
            right = right[2:]+right[:2]
        return (left+right)

    # Maps strings to Permutation Table 8
    def KEY_P8(self,shifted_string):
        P8,KEY = [6,3,7,4,8,5,10,9],''
        for i in P8:
            KEY+=shifted_string[i-1]
        return KEY

    # Maps strings to P table 10 and computes P8 and performs
    # shift operations
    def KEY_P10(self,key):
        P10, mapped = [3,5,2,7,4,10,1,9,8,6],''
        for i in P10:
            mapped+=key[i-1]
        # 1st circular left shift by 1
        left_shift1 = self.SDES_shift(mapped,1)
        # Computes the KEY1
        KEY_1 = self.KEY_P8(left_shift1)
        # 2nd circular left shift by 2
        left_shift2 = self.SDES_shift(left_shift1,2)
        # Computes the KEY2
        KEY_2 = self.KEY_P8(left_shift2)
        print KEY_2

    
#Main
obj = SDES()
obj.KEY_P10("1010000010")
