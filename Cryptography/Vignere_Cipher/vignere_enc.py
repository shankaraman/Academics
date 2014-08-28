alphabets,rev_alphabets, vignere_table = {},{},[]
#cipher, key, encrypted = "WEAREDISCOVERED", "DECEPTIVEDECEPT",''
cipher,key = open("2_cipher_1.txt","r"), raw_input("Enter the key:")
new_cipher, padded_key, encrypted = cipher.read(),'',''

#Padding the key
if len(new_cipher) == len(key):
    pass
elif len(new_cipher) < len(key):
    print "Insufficient cipher length"
    exit
elif len(new_cipher) == len(key):
    pass
else:
    new_cipher = new_cipher.replace(" ","")
    for i in range(len(new_cipher)-len(key)):
        padded_key+=key
    padded_key = padded_key[:len(new_cipher)-1]

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
for i in range(len(new_cipher)):
    if new_cipher[i] == '\n':
        pass
    else:
        encrypted+=vignere_table[rev_alphabets[new_cipher[i]]][rev_alphabets[padded_key[i]]]
#print "KEY:", padded_key
#print "ENCRYPTED TEXT:",encrypted
print alphabets
print rev_alphabets
