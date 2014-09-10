import sys
class SDES_KEY:

    # Since we are going to use KEY_1 and KEY_2 throughout the program, we are defining in
    # a constructor so that the variables defined here, can be accessed from other calsses
    def __init__(self):
        SDES_KEY.KEY_1 = ""
        SDES_KEY.KEY_2 = ""

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
        if len(key) == 0:
            return
        P10, mapped = [3,5,2,7,4,10,1,9,8,6],''
        for i in P10:
            mapped+=key[i-1]
        # 1st circular left shift by 1
        left_shift1 = self.SDES_shift(mapped,1)
        # Computes the KEY1
        SDES_KEY.KEY_1 = self.KEY_P8(left_shift1)
        # 2nd circular left shift by 2
        left_shift2 = self.SDES_shift(left_shift1,2)
        # Computes the KEY2
        SDES_KEY.KEY_2 = self.KEY_P8(left_shift2)


class SDES_ENC(SDES_KEY):
    def xor(self,op1,op2):
        if len(op1) != len(op2):
            return
        xored = ''
        for i in range(len(op1)):
            xored+=str(int(op1[i])^int(op2[i]))
        return xored

    def EP(self,text):
        table,enc = [4,1,2,3,2,3,4,1],''
        for i in table:
            enc+=text[i-1]
        return enc

    # Performs S-BOX operations and passes the result directly to P4 function.
    def S_BOX(self,left,right):
        S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
        S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
        # Computes the row and column value for the left string
        row,col = int((left[0]+left[3]),2),int((left[1]+left[2]),2)
        # Performs the binary conversion of the S0 table value.
        S0_result = "{0:b}".format(S0[row][col]) 
        if len(S0_result) == 1:
            S0_result = "0"+S0_result
        # Performs the binary conversion of the S1 table value.
        row,col = int((right[0]+right[3]),2),int((right[1]+right[2]),2)
        S1_result = "{0:b}".format(S1[row][col])
        if len(S1_result) == 1:
            S1_result = "0"+S1_result
        # Passes back to IP to compute P4.
        return (S0_result+S1_result)
    
    def P4(self,text):
        table,enc = [2,4,3,1],''
        for i in table:
            enc+=text[i-1]
        return enc
        
    def IP(self,text):
        table,mapped = [2,6,3,1,4,8,5,7],''
        for i in table:
            mapped+=text[i-1]
        return mapped

    def IP_INVERSE(self,text):
        table,mapped = [4,1,3,5,7,2,8,6],''
        for i in table:
            mapped+=text[i-1]
        return mapped


    def main(self,text):
        mapped = self.IP(text)
        # Calling P10 of SDES_KEY function since we are going to use the KEY_1
        # and KEY_2
        self.KEY_P10("") # I don't want to give the input again.
        # IP table result's left half and right half
        left1,right1 = mapped[:len(mapped)/2],mapped[len(mapped)/2:]
        # Expands right half using EP table.
        EP_right = self.EP(right1)
        # xor KEY1 and EP_right
        XOR = self.xor(SDES_ENC.KEY_1,EP_right)
        # XOR's left half and right half
        left2,right2 = XOR[:len(XOR)/2],XOR[len(XOR)/2:]
        # S-Box operation on left and right half of the xored output
        S_BOX_result = self.S_BOX(left2,right2)
        # Computes the P4 mapped string using the SBOX result.
        P4_result = self.P4(S_BOX_result)
        # Xoring the P4_result with left1
        XOR = self.xor(P4_result,left1)
        # Now concatenate right1 and above XOR's result
        R1_XOR = right1+XOR
        # Computing the E/P string for the right half of R1_XOR
        EP_right = self.EP(R1_XOR[len(R1_XOR)/2:])
        # Xoring the EP_right with KEY2
        EP_K2 = self.xor(SDES_KEY.KEY_2,EP_right)
        # Splitting EP_K2 into 2 halves for computing SBOX.
        left3,right3 = EP_K2[:len(EP_K2)/2],EP_K2[len(EP_K2)/2:]
        # Computing the SBOX mapping for the EP_K2 and computing P4
        S_BOX_result = self.S_BOX(left3,right3)
        P4_result = self.P4(S_BOX_result)
        # Xoring the P4_result and R1_XOR's left half
        XOR = self.xor(P4_result,R1_XOR[:len(R1_XOR)/2])
        # Calculating IP inverse by giving XOR and R1_XOR's right half
        IPInverse = self.IP_INVERSE(XOR+R1_XOR[len(R1_XOR)/2:])
        return IPInverse

    
#Main
# Get user inputs
plain,key = raw_input("Enter the 8 bit plain text:"),raw_input("Enter the 10 bit key:")
obj1,obj2 = SDES_KEY(),SDES_ENC()
# Computes the KEYS
obj1.KEY_P10(key)
# Encrypts the Plain text
final_result = obj2.main(plain)
#print "The key given for encryption:",key
print "Encrypted text:",final_result
