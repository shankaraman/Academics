fd = open("2_cipher.txt","r")
cipher_text = fd.read()
alphabets,rev_alphabets, frequent_words, text_con,possible_keys  ={},{},{}, '',[]

# Frequentkly occuring english alphabet's index
#frequent_seq ={'e':4,'t':19,'a':0,'o':14,'i':8,'n':13,'s':18,'r':17,'h':7,'l':11,'d':3,'c':2,'u':20,'m':12,'f':5,'p':15,'g':6,'w':22,'y':24,'b':1,'v':21,'k':10,'x':23,'j':9,'q':16,'z':25}
freq_list = [4,19,0,14,8,13,18,17,7,11,3,2,20,12,5,15,6,22,24,1,21,10,23,9,16,25]
# Mapping alphabets
for i in range(26):
    rev_alphabets[chr(i+97)] = i
    alphabets[i] = chr(i+97)

for i in cipher_text:
    text_con+=i

# Collecting unique characters
unique_string = set(text_con)
unique_string = list(unique_string)

# Removing special symbols
unique_string.remove(' ')
unique_string.remove('.')
unique_string.remove('\n')

# Counting and Mapping the occurence of the unique characters to the character
for i in unique_string:
    count = 0
    for j in cipher_text:
        if i == j:
            count+=1
    frequent_words[count] = i

# Finding out the possible keys as per the frequency
begin_here = len(frequent_words)-1
for i in frequent_words.keys():
    possible_keys.append(rev_alphabets[frequent_words[i]]-freq_list[begin_here])
    begin_here-=1
print "The possible keys are:",possible_keys,"\n"

# Shifting the cipher as per the possible keys
for i in possible_keys:
    plain = ''
    for j in cipher_text:
        if j == " " or j == "." or j == "\n":
            plain+=j
            pass
        else:
            plain+=alphabets[(rev_alphabets[j]  - i)%26]
    print "For key =",str(i)+str(':'),plain
