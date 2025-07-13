word=input("enter a word: ")
counter=0
vowel="aeiouAEIOU"
for i in word:
    if i in vowel:
        counter +=1
print(counter)
