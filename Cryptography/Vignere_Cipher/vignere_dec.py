alphabets,rev_alphabets, vignere_table = {},{},[]
cipher,key = open("Lab2_1_cipher.txt","r"), "ourmission"
new_cipher, padded_key, final = cipher.read(),'',''
#new_cipher, padded_key, final= "ZICVTWQNGRZGVTW", "DECEPTIVEDECEPT", ''

#Padding the key
if len(new_cipher) == len(key):
    pass
elif len(new_cipher) < len(key):
    print "Insufficient cipher length"
    exit
else:
    if new_cipher.find(" ") == 1:
        new_cipher = new_cipher.replace(" ","")
# The Worst way to pad key!
    else:
        for i in range(len(new_cipher)-len(key)):
            padded_key+=key
    padded_key = padded_key[:len(new_cipher)-1]

# Alphabets Mapping
for i in range(97,97+26):
    alphabets[i-97] = chr(i)
    rev_alphabets[chr(i)] = i-97

# Building Vignere table
for i in range(27):
    temp = []
    for j in range(97,97+26):
        temp.append(alphabets[(rev_alphabets[chr(j)]+i)%26])
    vignere_table.append(temp)

#Decryption
for i in range(len(padded_key)):
    for j in range(26):
        if vignere_table[rev_alphabets[padded_key[i]]][j] == new_cipher[i]:
            final+=alphabets[j]
print final
