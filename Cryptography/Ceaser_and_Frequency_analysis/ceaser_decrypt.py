#Intialization
fd = open('1_cipher.txt','r')
cipher_text = fd.read()
alphabets,rev_alphabets, key, plain_list = {}, {}, 1, []

# Mapping alphabets
for i in range(26):
    rev_alphabets[chr(i+97)] = i
    alphabets[i] = chr(i+97)

#Ceaser Cipher
while key <= 26:
    plain = ''
    for i in cipher_text:
        if i == " " or i == '.' or i == '(' or i ==')' or i == ',' or i == '\n':
            plain+=i
            pass
        else:
            plain+=alphabets[(rev_alphabets[i]  - key)%26]
    plain_list.append(plain)
    key+=1

for i in range(len(plain_list)):
    print "For key:"+str(i+1), plain_list[i]
