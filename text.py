para=input("Enter the para")
words=para.split(" ")
print(len(words))
sentence_count = para.count('.') + para.count('!') + para.count('?')
print(sentence_count)
vowels="aeiouAEIOU"
vowel_count=0
for i in para:
    if i in vowels:
        vowel_count+=1
print("Vowel Count is",vowel_count)        
frequent={}
print(words)
for i in "!.?":
    para=para.replace(i," ")
word=para.split()
print(word)
for i in word:
    if i in frequent:
        frequent[i]+=1
    else:
        frequent[i]=1    
sorted_words=sorted(frequent.items(),key=lambda item : item[1],reverse=True)
print(sorted_words[:3])
