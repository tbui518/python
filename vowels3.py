vowels = ['a', 'e', 'i', 'o', 'u']
word = input("proviide a word to search for vowels: ")
found = []
for le in word:
    if le in vowels:
        if le not in found:
            found.append(le)
for vowel in found:
    print(vowel)
 
