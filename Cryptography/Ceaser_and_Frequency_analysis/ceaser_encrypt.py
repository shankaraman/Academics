# User Inputs
plain_text, key = raw_input("Enter a message to encrypt:"), input("Enter the shfit value:")

# Variable intialization
alphabets, rev_alphabets, cipher_text = {}, {}, ''

# Mapping alphabets
for i in range(26):
    rev_alphabets[chr(i+97)] = i
    alphabets[i] = chr(i+97)

# Ceaser Cipher Encryption
for i in plain_text:
    cipher_text+=alphabets[(rev_alphabets[i]+key)%26]

print "The Cipher text for your key="+str(key),"is:",cipher_text
