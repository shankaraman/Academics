# Building Initial Permutation Table
def initial_permutation_table(initial_table,start):
    for i in range(8):
        if i == 4:
            start = 57
        minus,temp_start = 8,start
        for j in range(8):
            initial_table.append(temp_start)
            temp_start-=8
        start+=2
    return initial_table

#Building Final Permutation Table
def final_permutation_table(final_table,start,second_element):
    for i in range(8):
        temp_start,temp_second_element = start,second_element
        for j in range(8):
            if j%2 == 0:
                final_table.append(temp_start)
                temp_start+=8
            else:
                final_table.append(temp_second_element)
                temp_second_element+=8
        start-=1
        second_element-=1
    return final_table

#Building the extended table



#Converting the hex characters to binary
def binary(text,initial_table):
    padded_binary,one_count,mapped_list = '',0,[]
    for i in text:
        if len(bin(int(i))[2:]) == 1:
            padded_binary+="000"+bin(int(i))[2:]
        elif len(bin(int(i))[2:]) == 2:
            padded_binary+="00"+bin(int(i))[2:]
        elif len(bin(int(i))[2:]) == 3:
            padded_binary+="0"+bin(int(i))[2:]
        else:
            padded_binary+=bin(int(i))[2:]
    for i in padded_binary:
        one_count+=1
        if i == "1":
        # Appending the (i's = 15,64) position from IP table
            mapped_list.append(initial_table.index(one_count))
    return padded_binary,mapped_list

#
def initial_permutation(mapped_list):
    encrypted_string = ''
    for i in range(64):
        if i in mapped_list:
            encrypted_string+="1"
    # Once mapped_list element is used then remove it, so that we can continue
    # directly from the next element.
            mapped_list.remove(i)
        else:
            encrypted_string+="0"
    return encrypted_string

#Main
initial_table = initial_permutation_table([],58)
final_table = final_permutation_table([],40,8)
# Converts the hex characters to binary and finds the position of 15,64(1's) 
#from initial permutation table.
padded_binary,mapped_list = binary("0002000000000001",initial_table)
encrypted_string = initial_permutation(mapped_list)
