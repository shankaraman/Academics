fd = open("2_cipher.txt","r")
cipher_text = fd.read()
frequent_words, text_con  = {}, ''
for i in cipher_text:
    text_con+=i
unique_string = set(text_con)
unique_string = list(unique_string)
unique_string.remove(' ')
unique_string.remove('.')
unique_string.remove('\n')
for i in unique_string:
    count = 0
    for j in cipher_text:
        if i == j:
            count+=1
    frequent_words[i] = count
print frequent_words.values()
