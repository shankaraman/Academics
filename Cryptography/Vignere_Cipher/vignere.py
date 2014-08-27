alphabets,rev_alphabets, vignere_table = {},{},[]
#cipher, key = "WEAREDISCOVERED", "DECEPTIVEDECEPT"
cipher,key = open("2_cipher_1.txt","r"), raw_input("Enter the key:")

# Alphabets Mapping
for i in range(65,65+26):
    alphabets[i-65] = chr(i)
    rev_alphabets[chr(i)] = i-65

# Building Vignere table
for i in range(27):
    temp = []
    for j in range(65,65+26):
        temp.append(alphabets[(rev_alphabets[chr(j)]+i)%26])
    vignere_table.append(temp)

#Vignere Encryption
for i in range(len(cipher)):
    print vignere_table[rev_alphabets[cipher[i]]][rev_alphabets[key[i]]]
